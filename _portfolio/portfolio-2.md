---

layout: single
title: "Sentinel-1 InSAR Surface Deformation Analysis of the 2025 Hayli Gubbi Volcano, Afar, Ethiopia"
header:
  teaser: "insar-teaser-title-results.png"
excerpt: "A Differential SAR Interferometry (DInSAR) workflow using SNAP & Sentinel-1 SLC data to map line-of-sight surface deformation caused by the 2025 Afar volcanic eruption."
collection: portfolio

---

**Author:** Mekonnen Gidey | MSc Geoinformation Science, Bahir Dar University  
**Date:** May 2026  
**Project Resources:** [Download Full Project Document](/files/Adv_RS_Lab_2_InSAR.pdf) 

---

### Project Overview
This project presents a single-pair Differential SAR Interferometry (DInSAR) workflow using Sentinel-1 SLC imagery to investigate ground surface deformation resulting from the November 2025 volcanic activity in the Afar region, Ethiopia. The analysis processes complex SAR phase observations into a geocoded Line-of-Sight (LOS) displacement map while evaluating phase coherence, adaptive filtering, SNAPHU phase unwrapping, and geometric corrections.

## Key Technical Skills Demonstrated

* **SAR / DInSAR Processing:** Sentinel-1 SLC coregistration, Back-Geocoding, and ESD alignment.
* **Phase Analysis:** Coherence evaluation, Goldstein filtering, phase unwrapping with SNAPHU.
* **Geospatial & Geodetic Analytics:** Metric displacement modeling, SRTM DEM geocoding, and histogram interpretation.
* **Software Tools:** ESA SNAP 13, Graph process modeling, Batch processing, SNAPHU, GIS.


> *Note: This portfolio post is a concise, web-optimized summary of my full 28-page project report. For the detailed technical breakdown, mathematical formulations, and step-by-step SNAP parameter settings, please refer to the full PDF report linked above.*

---

## 1. Background & Objectives

### Background
On **23 November 2025**, significant volcanic activity occurred in the Afar depression, centered near the **Hayli Gubbi (Guba Haili)** and **Erta Ale** volcanic complex. Volcanic eruptions and subsurface magma movement induce measurable surface deformation—such as co-eruptive inflation, deflation, or faulting—that can be captured from space using Synthetic Aperture Radar (SAR).

![Afar / Guba Haili study area context](/images/study-area-afar-guba-haili.png)
*Figure 1: Geographic context of the Afar study area focusing on Hayli Gubbi and Erta Ale.*

### Objectives
* **Process Repeat-Pass SAR Data:** Execute a complete DInSAR processing chain in ESA SNAP 13 using Sentinel-1 SLC acquisitions acquired immediately before and after the eruption.
* **Map Ground Displacement:** Quantify relative Line-of-Sight (LOS) deformation across the volcanic complex.
* **Evaluate Phase Quality & Uncertainty:** Assess spatial coherence, signal decorrelation over varying land covers, and potential atmospheric noise constraints.

---

## 2. InSAR Methodology & Phase Model

InSAR measures surface movement by evaluating the phase difference between two complex SAR acquisitions taken from slightly different orbital positions. The interferometric phase ($\phi$) is modeled as:

$$\phi = \phi_{\text{DEM}} + \phi_{\text{flat}} + \phi_{\text{disp}} + \phi_{\text{atm}} + \phi_{\text{noise}}$$

Differential processing removes the topographic ($\phi_{\text{DEM}}$) and flat-earth orbital ($\phi_{\text{flat}}$) components using a reference DEM, leaving the residual phase representing deformation, atmospheric delay, and noise:

$$\phi_{\text{disp}} + \phi_{\text{atm}} + \phi_{\text{noise}} = \phi - \phi_{\text{DEM}} - \phi_{\text{flat}}$$

![Sentinel-1 IW sub-swaths](/images/sentinel1-iw-sub-swaths.png)
*Figure 2: Sentinel-1 TOPSAR acquisition geometry across IW sub-swaths (sub-swath IW2 selected).*

![Study-area location in the Sentinel-1 product](/images/product-world-map-study-area.png)
*Figure 3: Coverage and orbital footprint of the Sentinel-1 acquisitions over Ethiopia.*

---

## 3. Data & Processing Environment

| Parameter | Specification |
|---|---|
| **Sensor & Mode** | Sentinel-1 SAR (Level-1 SLC, IW Mode, VV Polarization) |
| **Pre-Eruption Master** | 19 November 2025, 15:26:35 UTC |
| **Post-Eruption Slave** | 25 November 2025, 15:27:34 UTC |
| **Sub-swath & Bursts** | Sub-swath IW2, Bursts 1–5 |
| **Digital Elevation Model** | SRTM 1-ArcSec HGT |
| **Processing Software** | ESA SNAP 13 & SNAPHU (Phase Unwrapping) |
| **Output Quantity** | Geocoded Line-of-Sight (LOS) Displacement (meters) |

---

## 4. Processing Chain

The workflow follows a structured sequence designed to maintain sub-pixel co-registration accuracy and clean phase information prior to displacement conversion:

| Stage | Operation | Purpose / Key Result |
|---|---|---|
| 1 | **TOPS Split** | Isolated sub-swath IW2 and bursts 1–5 over the study site. |
| 2 | **Apply Orbit File** | Updated precise orbital state vectors (POEORB). |
| 3 | **Back-Geocoding & ESD** | Coregistered master and slave images to sub-pixel accuracy using SRTM DEM and Enhanced Spectral Diversity. |
| 4 | **Interferogram & Coherence** | Generated raw wrapped phase and spatial coherence map. |
| 5 | **TOPS Deburst** | Merged individual burst boundaries into a continuous raster. |
| 6 | **Goldstein Filtering** | Applied adaptive filtering to improve phase fringe clarity. |
| 7 | **Subsetting** | Cropped processing area to the immediate volcanic AOI. |
| 8 | **SNAPHU Unwrapping** | Resolved 2π phase ambiguities using Minimum Cost Flow (MCF). |
| 9 | **Phase to Displacement** | Converted unwrapped phase values into metric LOS displacement. |
| 10 | **Terrain Correction** | Geocoded output to UTM projection using SRTM DEM. |

---

## 5. Pre-Processing & Coregistration

### TOPS Split & Orbit Correction
The processing was reduced to sub-swath IW2 and bursts 1–5 to minimize computational load while covering the entire volcanic structure. Precise orbit files were applied to correct orbital geometry.

![TOPS Split showing IW2 and bursts 1–5](/images/tops-split-bursts-1-5.png)
*Figure 4: TOPS Split selection isolating IW2, bursts 1–5 over the volcanic target.*

![Apply Orbit File](/images/apply-orbit-file.png)
*Figure 5: Orbital correction setup applying precise orbit state vectors.*

![Back Geocoding](/images/back-geocoding.png)
*Figure 6: DEM-assisted Back-Geocoding for high-precision master-slave alignment.*

---

## 6. Interferogram Generation & Coherence Diagnostics

Cross-multiplying the master image with the complex conjugate of the slave image yielded the wrapped interferometric phase. 

![Interferogram formation settings](/images/interferogram-formation-settings.png)
*Figure 7: SNAP Interferogram formation operator configuration.*

### Coherence Analysis
Spatial coherence was computed as a diagnostic layer to evaluate phase reliability. Higher coherence (> 0.6) in the arid lava fields enabled stable phase unwrapping, whereas localized decorrelation was observed in sparsely vegetated pockets.

<table>
  <tr>
    <td style="width: 50%;"><img src="/images/interferogram-phase.png" alt="Wrapped interferogram phase"></td>
    <td style="width: 50%;"><img src="/images/coherence-map.png" alt="Coherence map"></td>
  </tr>
  <tr>
    <td><em>Figure 8a: Wrapped interferometric phase showing cyclic 2π fringes.</em></td>
    <td><em>Figure 8b: Spatial coherence map (bright areas represent high phase stability).</em></td>
  </tr>
</table>

---

## 7. Filtering & Spatial Subsetting

To improve the signal-to-noise ratio, **Goldstein Phase Filtering** was applied before phase unwrapping. This enhanced fringe visibility across areas of low SNR without distorting the underlying phase structure.

![Goldstein filtering: before and after](/images/goldstein-filter-before-after.png)
*Figure 9: Comparison of interferometric phase fringes before (left) and after (right) Goldstein filtering.*

---

## 8. Phase Unwrapping (SNAPHU)

Phase unwrapping was executed using SNAPHU via the SNAP export interface. The unwrapping process resolves the 2π ambiguity, producing a continuous relative phase map across the target area.

![Wrapped versus unwrapped phase principle](/images/phase-unwrapping-principle.png)
*Figure 10: Conceptual transformation from ambiguous wrapped phase to continuous unwrapped phase.*

![SNAPHU export settings](/images/snaphu-export-settings.png)
*Figure 11: SNAPHU export settings using statistical-cost mode (DEFO).*

![SNAPHU unwrapping progress](/images/snaphu-unwrapping-progress.png)
*Figure 12: Execution log of SNAPHU Phase Unwrapping process.*

![SNAPHU import](/images/snaphu-import.png)
*Figure 13: Re-importing unwrapped phase raster back into SNAP.*

![Unwrapped phase result](/images/unwrapped-phase-result.png)
*Figure 14: Final unwrapped interferometric phase raster.*

---

## 9. Conversion to LOS Displacement & Geocoding

The continuous unwrapped phase was converted to metric Line-of-Sight displacement (metres) using the radar wavelength ($\lambda \approx 5.556\text{ cm}$ for Sentinel-1 C-band).

<table>
  <tr>
    <td style="width: 50%;"><img src="/images/phase-to-displacement-result.png" alt="Phase to displacement result"></td>
    <td style="width: 50%;"><img src="/images/los-displacement-histogram.png" alt="LOS displacement histogram"></td>
  </tr>
  <tr>
    <td><em>Figure 15a: Computed Line-of-Sight (LOS) displacement map.</em></td>
    <td><em>Figure 15b: Histogram distribution of LOS displacement values.</em></td>
  </tr>
</table>

### Range Geocoding
Doppler Range-Terrain Correction (SRTM 1-ArcSec) was applied to correct geometric distortions (foreshortening and layover) and project the raster into geographical space.

![Terrain correction settings](/images/terrain-correction-result.png)
*Figure 16: Range-Doppler Terrain Correction parameters in SNAP.*

![Final interferogram](/images/final-interferogram.png)
*Figure 17: Geocoded wrapped interferogram over the Afar volcanic zone.*

![Final LOS displacement map](/images/final-los-displacement-map.png)
*Figure 18: Final geocoded Line-of-Sight (LOS) displacement map.*

---

## 10. Results & Discussion

### Deformation Pattern Observed
* **Localized Volcanic Subsidence:** Concentric fringe patterns around Erta Ale and Hayli Gubbi indicate significant ground subsidence associated with co-eruptive magma movement.
* **Displacement Magnitude:** The display scale highlights concentrated deformation ranging from approximately **−0.146 m** (subsidence) to **+0.034 m** (localized uplift).
* **Statistical Range:** Inspecting the full raster metadata reveals minimum LOS change reaching **−0.471 m** and maximum uplift around **+0.150 m**.

![Unwrapped phase histogram](/images/unwrapped-phase-histogram.png)
*Figure 19: Unwrapped phase histogram distribution.*

![LOS displacement histogram](/images/los-displacement-histogram.png)
*Figure 20: LOS displacement statistical distribution highlighting main signal stretch and extreme values.*

---

## Results & Volcanological Interpretation

| Deformation Parameter | Metric Value (LOS) | Geological Mechanism |
| :--- | :--- | :--- |
| **Maximum Subsidence** | -0.471 m (-47.1 cm) | Caldera collapse / Magma chamber evacuation |
| **Maximum Uplift** | +0.150 m (+15.0 cm) | Peripheral magmatic dike intrusion |
| **Coherence Threshold** | > 0.6 | Strong phase stability across the arid Afar terrain |

---

### Analysis Highlights
* **Fringe Density Analysis:** Concentric closed fringe loops around the Erta Ale and Hayli Gubbi craters indicate steep spatial deformation gradients occurring across the 6-day acquisition window (November 19 to November 25, 2025).
* **Deformation Dynamic:** The spatial pattern reflects co-eruptive magma movement, characterized by central caldera deflation flanked by asymmetric dike-induced uplift along the active rift axis.
* **Histogram Scaling vs. True Metadata:** While automated histogram color-stretching clips display values between -0.146 m and +0.034 m to mitigate localized noise artifacts, absolute raster metadata confirms peak ground displacement bounds of -0.471 m to +0.150 m.

---

## References

1. European Space Agency (ESA). *S1TBX Stripmap & TOPSAR Interferometry with Sentinel-1 Tutorial*. ESA STEP Documentation.
2. Ferretti, A., Monti-Guarnieri, A., Prati, C., Rocca, F., & Vassena, B. (2007). *InSAR Principles: Guidelines for SAR Interferometry Processing and Interpretation* (ESA TM-19). European Space Agency.
3. Goldstein, R. M., & Werner, C. L. (1998). Radar interferogram filtering for geophysical applications. *Geophysical Research Letters*, 25(21), 4035-4038.
4. Hanssen, R. F. (2001). *Radar Interferometry: Data Interpretation and Error Analysis*. Kluwer Academic Publishers, Dordrecht.
