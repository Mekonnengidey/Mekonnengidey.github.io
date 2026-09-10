/**
 * =========================================================================
 * BAHIR DAR UNIVERSITY - DEPARTMENT OF GEOGRAPHY & ENVIRONMENTAL STUDIES
 * Course: Advanced Remote Sensing | Student: Mekonnen Gidey (ID: BDU1806929)
 * Project: Bi-Temporal Flood Mapping via Sentinel-1 SAR (Awash Floodplain)
 * =========================================================================
 */

// 1. GEOGRAPHIC CONSTRAINTS
 var aoi = table.geometry(); // please import the provided AOI_used_in_SNAP_Polygon
 // or use aoi below
//var aoi = ee.Geometry.Polygon([[[38.60,8.70],[38.60,8.92],[38.21,8.92],[38.21,8.70]]], null, false);
 Map.centerObject(aoi, 12);
 Map.setOptions('SATELLITE');

// 2. SENTINEL-1 INGESTION & CORE FILTERING
var s1Collection = ee.ImageCollection('COPERNICUS/S1_GRD')
  .filterBounds(aoi)
  .filter(ee.Filter.eq('instrumentMode', 'IW'))
  .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VV'))
  .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VH'));

// 3. BI-TEMPORAL TIMEFRAMES & ORBIT TRACK ALIGNMENT
var preFloodColl = s1Collection.filterDate('2025-07-24', '2025-07-27');
var postFloodColl = s1Collection.filterDate('2025-08-07', '2025-08-09');

// Enforce identical track angles using the primary crisis image metadata
var firstPostImage = ee.Image(postFloodColl.first());
var matchingOrbit  = firstPostImage.get('relativeOrbitNumber_start');
var matchingPass   = firstPostImage.get('orbitProperties_pass');

var orbitFilter = ee.Filter.and(
  ee.Filter.eq('relativeOrbitNumber_start', matchingOrbit),
  ee.Filter.eq('orbitProperties_pass', matchingPass)
);

// Generate spatial mosaics clipped to the study area (VV Band Only)
var preVV_raw  = preFloodColl.filter(orbitFilter).mosaic().clip(aoi).select('VV');
var postVV_raw = postFloodColl.filter(orbitFilter).mosaic().clip(aoi).select('VV');

// 4. ADAPTIVE LOCAL STATISTICS SPECKLE FILTER (Refined Reflected Code)
var applySpeckleFilter = function(image) {
  var linear = ee.Image(10).pow(image.divide(10)); // DB to linear conversion
  var kernel = ee.Kernel.square(3, 'pixels'); // try 1 for3x3;3for7x7; moving window   
  
  var localMean     = linear.reduceNeighborhood(ee.Reducer.mean(), kernel);
  var localVariance = linear.reduceNeighborhood(ee.Reducer.variance(), kernel);
  var noiseVariance = 0.25; // selected to match actual Sentinel-1 multilooking and speckle characteristics.
  
    // CALIBRATION ADJUSTMENT: test by increasinf from 0.04 to 1 
  //var noiseVariance = 0.04; //resulted 112.3345852761005kmsq
   // var noiseVariance = 0.25;// resulted 87.09379531558267
    // var noiseVariance = 0.5; // resulted 85.24767501784169
     // var noiseVariance = 1; //resulted 84.44188657308364
   
   // Higher values (0.25 - 1.0) increase smoothing resulting low area 
    // Compute weight matrices (Lee adaptive scalar) to
   // increase smoothing of background noise while preserving sharp boundaries.
  var weight = localVariance.subtract(localMean.pow(2).multiply(noiseVariance)).divide(localVariance);
  weight     = weight.clamp(0, 1);
  
  var filteredLinear = localMean.add(weight.multiply(linear.subtract(localMean)));
  return filteredLinear.log10().multiply(10); // Return to logarithmic scale (dB)
};

var preVV  = applySpeckleFilter(preVV_raw);
var postVV = applySpeckleFilter(postVV_raw);

// 5. BINARY THRESHOLDING & CONCURRENT SURFACE MASKING
var waterThreshold = -12; // Backscatter physical threshold cutoff for specular water reflections
var changeRatio    = postVV.subtract(preVV);

var preWater  = preVV.lt(waterThreshold);  // Baseline water footprint
var postWater = postVV.lt(waterThreshold); // Post-crisis water footprint

// Isolate transient emergency waterbodies [Post-Water AND NOT Pre-Water]
var floodMask    = postWater.and(preWater.not());
var floodMapOnly = floodMask.updateMask(floodMask); // Suppress dry background matrices

// 6. PLANAR CARTESIAN METRIC AREA ESTIMATION
var floodAreaImage = floodMapOnly.multiply(ee.Image.pixelArea());

var areaStats = floodAreaImage.reduceRegion({
  reducer: ee.Reducer.sum(),
  geometry: aoi,
  scale: 10,              // Sentinel-1 native spatial resolution tracking
  crs: 'EPSG:32637',      // Enforce local UTM Zone 37N Planar Cartesian projection
  maxPixels: 1e9
});

// Dynamic array index extraction bypassing structural dictionary band name shifts
var floodAreaM2  = ee.Number(areaStats.values().get(0));
var floodAreaKM2 = floodAreaM2.divide(1e6);

// Console Diagnostic Metrics Output Logging
print('=====================================================');
print('      BDU SAR LAB METRIC PROCESSING RESULTS          ');
print('=====================================================');
print('Calculated Inundated Flood Area (Square Kilometers):', floodAreaKM2);
print('=====================================================');

// 7. CARTO-RENDERING & MAP DISPLAY LAYERS
var sarVis = {min: -25, max: 0};
Map.addLayer(preVV, sarVis, '1. Pre-Flood Baseline (July 2025) [dB]');
Map.addLayer(postVV, sarVis, '2. Flood Event Crisis (August 2025) [dB]');
Map.addLayer(changeRatio, {min: -10, max: 10}, '3. Change Detection Ratio (Post minus Pre)', false);
Map.addLayer(preWater.updateMask(preWater), {palette: ['#0000FF']}, '4. Permanent Water Bodies', false);
Map.addLayer(floodMapOnly, {palette: ['#FF0000']}, '5. Final Binary Flood Extent Map');


// 8. CLOUD SYSTEM RASTER EXPORT
Export.image.toDrive({
  image: floodMapOnly,
  description: 'Awash_River_Flood_Mask_2025_Final_Mekonnen',
  scale: 10,
  crs: 'EPSG:32637', // Preserves strict local GIS vector alignment compatibility
  region: aoi,
  fileFormat: 'GeoTIFF',
  maxPixels: 1e9
});

