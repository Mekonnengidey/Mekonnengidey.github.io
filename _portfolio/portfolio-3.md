---
title: "UAV Photogrammetry and Object-Based Forest Mapping (Gulele, Addis Ababa)"
excerpt: "From 162 drone images to orthomosaic, DSM, DTM, 3D model and a five-class land-cover map, with an honest account of what worked and what did not."
collection: portfolio
---

## Summary

I processed a UAV image block over a forested hillside in the Gulele area of Addis Ababa into an orthomosaic, a digital surface model (DSM), a digital terrain model (DTM), a dense point cloud and a textured 3D model. I then used the DSM together with the orthomosaic to map land cover (including forest) with object-based image analysis (OBIA) in Google Earth Engine. I also use this workflow when teaching MSc laboratory sessions.

## Context and my role

- **Course term project** in Advanced Remote Sensing (MSc, Bahir Dar University), completed May 2026.
- **Data:** the UAV dataset was provided by the course instructor and was collected in August 2017 by earlier cohorts, not by me. It contains 162 nadir RGB images (DJI FC330, 4000 x 3000 px) over about 11 ha, plus a GCP file with 9 ground control points.
- **How the course works:** each student sets up and teaches one component to classmates, and every student then runs all workflows independently. I ran the full pipeline below on my own computer.
- **Credits:** [CONFIRM AND FILL: instructor name; classmates whose setup materials I used; the sections I prepared myself].

## Workflow

1. **Photogrammetry in WebODM** (Docker on WSL2): feature matching, structure-from-motion, multi-view stereo, georeferencing with GCPs. Result: 173,928 sparse tie points, 21.5 million dense points, 4.4 cm ground sampling distance.
2. **Products:** orthomosaic, DSM, DTM, point cloud, textured 3D model and contour lines.
3. **Parallel workflow in ArcGIS Pro (Ortho Mapping):** block adjustment, DSM and orthomosaic, then a canopy height model (CHM = DSM - DTM) and a composite raster for cloud processing.
4. **OBIA in Google Earth Engine:** SNIC segmentation of the RGB + DSM composite, per-object mean RGB and elevation, then a 100-tree Random Forest for five classes (Forest, Built-up, Road, Bareland, Grassland). 816 reference points were digitised on the orthomosaic and split 70/30 for training and validation.

## Results

| Item | Result |
|---|---|
| Onboard GPS error | 13.57 m RMSE, mostly a constant vertical offset (about 13.1 m) |
| After adding 9 GCPs | 0.71 m RMSE (fit residual, see limitations) |
| Reprojection error | 1.21 px (0.19 normalized) |
| OBIA overall accuracy | [CONFIRM: 87.1% (kappa 0.84) or 80.5%] on the 30% validation set |
| Pixel-based comparison | 62% overall accuracy, with strong salt-and-pepper noise |

[ADD FIGURES: orthomosaic, DSM, DTM, 3D model, OBIA vs pixel-based land-cover maps]

## Limitations I identified

- **Terrain under dense canopy is interpolated.** Photogrammetry sees the ground only through canopy gaps, so the DTM beneath thick forest is estimated. The CHM is therefore indicative, and LiDAR would be the right reference for sub-canopy terrain.
- **The 0.71 m figure is not independent accuracy.** The GCPs were used in the adjustment, and I did not hold out check points.
- **OBIA validation is optimistic.** Randomly splitting nearby points from one scene can overestimate accuracy. A spatially separated validation set is the next step.
- **One site, one date.** This shows a workflow, not a time series or a transferable model.

## Why this matters for my research

UAV-derived DSMs, CHMs and orthomosaics give centimeter-scale structure between field plots and satellite pixels. I would like to use data like this as a reference when evaluating GEDI and NISAR forest height and structure estimates in Ethiopian forests.

## Materials

- [UAV photogrammetry manual (PDF)](/files/UAV_based_RS_Final.pdf)
- [OBIA manual (PDF)](/files/UAV_based_OBIA2.pdf)
