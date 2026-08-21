---
title: "Bi-Temporal SAR GRD Processing for Flood Mapping: SNAP vs. GEE"
excerpt: "A comparative analysis of Sentinel-1 SAR flood mapping workflows using ESA SNAP and Google Earth Engine to assess the August 2025 Awash River inundation."
header:
  teaser: "/assets/images/portfolio/flood-map-teaser.png"
categories:
  - Portfolio
  - Remote Sensing
tags:
  - SAR
  - Google Earth Engine
  - ESA SNAP
  - Flood Mapping
---

### Project Overview

Heavy rainfall during the Ethiopian Kiremt season in August 2025 caused severe flooding and widespread displacement along the Awash River plain and parts of Addis Ababa. This project leverages Synthetic Aperture Radar (SAR) technology to map the disaster footprint, overcoming the severe cloud-cover limitations that optical sensors face during storm events. 

![Map showing the Awash River study area and baseline conditions](/assets/images/portfolio/study-area-map.png)

By processing Sentinel-1 Ground Range Detected (GRD) imagery across two distinct platforms—the ESA Sentinel Application Platform (SNAP) and Google Earth Engine (GEE)—this work demonstrates end-to-end multi-temporal change detection. The objective was to isolate transient emergency floodwaters from permanent water bodies, quantify the total inundated area, and critically evaluate the operational trade-offs between localized desktop processing and automated cloud-parallel computing.

---

### Methodology and Technical Workflow

The analysis utilized a dual-image detection strategy, comparing a pre-flood baseline image (July 26, 2025) with a crisis image captured during peak flooding (August 7, 2025). 

#### 1. Automated Pre-Processing (ESA SNAP)
To ensure rigorous spatial and radiometric alignment, a batch processing graph was developed in SNAP to apply identical mathematical parameters to both temporal scenes:

*   **Orbit and Radiometric Correction:** Updated metadata with precise satellite orbital positions and converted raw intensity to scientifically meaningful Sigma0 backscatter coefficients.
*   **Speckle Filtering:** Applied an adaptive 7x7 Lee Sigma speckle filter to smooth homogeneous water regions while preserving sharp terrestrial edges and infrastructure boundaries.
*   **Geometric Adjustments:** Executed Range-Doppler Terrain Correction using an SRTM Digital Elevation Model to project radar geometry onto a flat WGS84 Cartesian grid at a 10-meter spatial resolution.

![Screenshot of the ESA SNAP Graph Builder showing the pre-processing node chain](/assets/images/portfolio/snap-graph-workflow.png)

#### 2. Cloud-Based Automation (Google Earth Engine)
A parallel workflow was scripted in JavaScript using GEE to test scalability and cloud automation:

*   **Programmatic Filtering:** Filtered the `COPERNICUS/S1_GRD` collection by temporal bounds, study area geometry, and strict relative orbit tracking to guarantee identical viewing angles.
*   **Custom Algorithm Development:** Engineered a custom Refined Lee adaptive scalar speckle filter within the script to mimic SNAP's edge-preserving capabilities on pre-processed cloud assets.

![Screenshot of the Google Earth Engine code editor and initial script output](/assets/images/portfolio/gee-code-editor.png)

---

### Analysis and Thresholding

Calm open water causes specular radar reflection, resulting in a distinct drop in the co-polarized (VV) backscatter signal. 

*   **Bimodal Histogram Analysis:** Logarithmic (dB) transformation of the calibrated data revealed a bimodal distribution, allowing for the calculation of a strict -12 dB backscatter threshold separating specular water from rough land.
*   **Raster Algebra:** Executed cross-temporal raster subtraction (post-water minus pre-water) using relational Boolean logic to isolate newly flooded zones and generate binary inundation masks.

![Bimodal histogram graph demonstrating the -12 dB backscatter threshold cut-off](/assets/images/portfolio/bimodal-histogram.png)

---

### Key Findings and Cross-Platform Validation

Both architectures successfully identified the primary flood boundaries, confirming that the physical behavior of radar backscatter is highly consistent across software suites.

*   **Quantitative Results:** The SNAP desktop environment calculated a flood area of 85.86 km², while the GEE cloud script calculated 87.09 km². 
*   **Discrepancy Drivers:** The minor 1.23 km² variance is driven by fundamental platform differences. SNAP applies filtering to raw geometry prior to terrain correction, yielding superior edge preservation and tight boundary delineation. Conversely, GEE applies filtering to already resampled pixels and calculates area geodetically across the WGS84 ellipsoid, introducing slight overestimations. 

![Side-by-side comparison maps of the final flood extraction masks: SNAP vs. GEE](/assets/images/portfolio/snap-vs-gee-comparison.png)

### Conclusion

This comparative analysis establishes SNAP as the optimal engine for highly accurate, phase-preserved micro-scale diagnostics, while demonstrating GEE's unmatched efficiency for rapid, regional-scale environmental monitoring and time-series scaling.
