---
title: "Teaching experience 2"
collection: teaching
type: "Workshop"
permalink: /teaching/2015-spring-teaching-1
venue: "University 1, Department"
date: 2015-01-01
location: "City, Country"
---

This is a description of a teaching experience. You can use markdown like any other post.

Heading 1
======
Technical Manuals & Teaching Resources
======

As part of my academic and laboratory responsibilities at **Bahir Dar University Geospatial Data Technology Center (GDTC)**, I have developed a series of technical and laboratory manuals based on applied research and geospatial projects. These resources are maintained in the **BDU GDTC library** and used to support practical instruction, postgraduate training, and independent research in GIS, Remote Sensing, Geospatial Data Science, and Spatial Programming.

### 1. SAR Data Processing & Applications — Postgraduate Laboratory Manual

- Comprehensive practical manual covering **Synthetic Aperture Radar (SAR)** data acquisition, preprocessing, calibration, filtering, visualization, interpretation, and analysis.
- Provides step-by-step workflows using **Sentinel-1 SAR and ESA SNAP**, with emphasis on reproducible radar-data processing.
- Covers core concepts including **SAR geometry, polarization, speckle filtering, radiometric calibration, terrain correction, backscatter analysis, and multi-temporal interpretation**.
- Developed as a reusable postgraduate teaching resource for **Remote Sensing, SAR, and Geospatial Data Science** courses.

### 2. Sentinel-1 SAR Flood & Inundation Mapping — Laboratory Manual

- Practical manual for **SAR-based flood and inundation mapping** using multi-temporal Sentinel-1 observations.
- Demonstrates **VV/VH polarization analysis, SAR preprocessing, backscatter-based water detection, thresholding, change detection, and GIS-based flood delineation**.
- Includes workflows for comparing pre- and post-event SAR observations and generating inundation maps and flood-risk information.
- Introduces automated and scripted approaches for **repeatable multi-temporal flood-monitoring workflows**.

### 3. Interferometric SAR (InSAR) for Surface Deformation Monitoring — Laboratory Manual

- Practical guide to **InSAR-based surface deformation analysis** using sequential SAR acquisitions.
- Covers interferometric processing concepts including **SAR coregistration, interferogram generation, phase analysis, filtering, phase unwrapping, geocoding, and deformation interpretation**.
- Demonstrates the application of InSAR to **tectonic, volcanic, seismic, and other surface-deformation processes**.
- Integrates deformation products with **GIS, DEMs, geological information, and environmental datasets** for geohazard assessment.

### 4. Object-Based Image Analysis & Bayesian Classification — Laboratory Manual

- Developed an advanced practical workflow for **Object-Based Image Classification (OBIC)** using **ERDAS IMAGINE Objective**.
- Documents an **11-stage object-based classification workflow** for high-resolution agricultural plot delineation.
- Demonstrates image segmentation, object generation, feature extraction, rule/model development, classification, and accuracy assessment.
- Uses **0.15 m aerial imagery** and a calibrated **Multi-Bayesian Network** for agricultural field delineation.
- Documents an experimental classification workflow achieving **Mean PixProb > 0.98**, providing a practical example of probabilistic object-based image classification.

### 5. Watershed Delineation, Morphometric Analysis & Conservation Prioritization — GIS Laboratory Manual

- Practical guide for **DEM-based watershed and drainage-network analysis** using ArcGIS Pro.
- Demonstrates delineation of the **Gilgel Abay watershed** and hierarchical subdivision into micro-watersheds.
- Covers hydrological terrain processing including **fill, flow direction, flow accumulation, stream extraction, stream ordering, and watershed delineation**.
- Provides workflows for **linear, areal, and relief-based morphometric analysis** of drainage basins.
- Applies multi-criteria spatial analysis to **rank and prioritize micro-watersheds for conservation and preservation**.
- Includes procedures for automated parameter extraction, spatial ranking, thematic mapping, and reproducible watershed analysis.

### 6. Advanced Geostatistics & Investment Site Suitability Analysis — Laboratory Manual

- Practical manual demonstrating the application of **advanced spatial statistics, geostatistics, GIS, and Multi-Criteria Decision Analysis (MCDA)** to investment-site selection in Bahir Dar.
- Covers integration and preprocessing of heterogeneous **environmental, infrastructural, accessibility, socioeconomic, and land-related datasets**.
- Demonstrates spatial analysis techniques including **proximity analysis, spatial interpolation, suitability modeling, weighted overlay, constraint mapping, and spatial ranking**.
- Provides workflows for generating suitability surfaces and identifying **high-, moderate-, and low-suitability investment zones**.
- Emphasizes reproducible spatial decision-support workflows for **urban planning, investment analysis, and evidence-based land-use decision-making**.

### 7. Geostatistical Modeling & Malaria Risk Analysis — Laboratory Manual

- Practical guide for applying **spatial statistics and geostatistical modeling** to environmental and public-health risk analysis in **West Gojam**.
- Integrates malaria occurrence information with environmental and geographic variables such as **elevation, land cover, climatic conditions, proximity measures, and other spatial risk factors**.
- Demonstrates **exploratory spatial data analysis, spatial interpolation, hotspot analysis, spatial relationships, risk modeling, and thematic risk mapping**.
- Provides workflows for identifying spatial concentrations and environmental patterns associated with **malaria risk**.
- Demonstrates the application of geospatial analysis to **public-health planning, environmental risk assessment, and spatially targeted intervention**.

### 8. Advanced Geospatial Database & Web Map Services — Laboratory Manual

- Practical guide to designing a **geospatial data management and dissemination infrastructure** using **PostgreSQL/PostGIS and GeoServer**.
- Covers spatial database design, geometry types, coordinate reference systems, spatial queries, spatial indexing, data organization, and management of institutional geospatial datasets.
- Demonstrates configuration of **GeoServer workspaces, PostGIS data stores, raster coverage stores, and published geospatial layers**.
- Covers publication and consumption of geospatial data through **OGC Web Map Service (WMS) and Web Feature Service (WFS)**.
- Demonstrates management and visualization of both **vector and raster datasets**, including GeoTIFF-based raster layers.
- Introduces **SLD-based styling, map rendering, reprojection, layer configuration, and web-based geospatial data dissemination**.
- Documents an end-to-end Spatial Data Infrastructure workflow:

  **PostgreSQL/PostGIS → GeoServer → OGC Services → GIS/Web Clients**

- Designed as a practical resource for teaching **Spatial Databases, Web GIS, GeoServer, OGC standards, and geospatial data infrastructure**.

### 9. Python Web GIS, Health Facility Accessibility & Network Routing — Laboratory Manual

- Practical guide to developing a **Python-based Web GIS application** for health-facility accessibility and route optimization.
- Demonstrates integration of **PostgreSQL/PostGIS, GeoServer, Python Web APIs, OpenStreetMap, routing services, and interactive web mapping**.
- Implements spatial queries for identifying **nearby health facilities** based on user-defined geographic locations.
- Demonstrates network-based accessibility analysis using **road-network distance and travel time**, rather than simple Euclidean distance.
- Integrates the **OSRM routing API** for nearest-road matching and fastest-route computation.
- Covers API request/response handling, **JSON processing, GeoJSON, coordinate handling, route geometry, distance/duration extraction, and web-map visualization**.
- Demonstrates integration of institutional geospatial data served through GeoServer with external **OpenStreetMap-based routing services**.
- Documents the complete application architecture:

  **PostgreSQL/PostGIS → GeoServer/OGC Services → Python Web API → OpenStreetMap/OSRM → Interactive Web Map**

- Provides a practical example of integrating **spatial databases, server-side GIS, REST APIs, network analysis, Python programming, and web cartography** into a geospatial decision-support application.

---

### Teaching & Research Resource Portfolio

Collectively, these manuals cover a broad range of **geospatial methods, computational tools, and environmental applications**, including:

**Remote Sensing → SAR/InSAR → Object-Based Classification → GIS → Hydrological Modeling → Geostatistics → Spatial Decision Analysis → Spatial Databases → GeoServer/OGC → Python APIs → Web GIS → Network Analysis**

The manuals are designed not only as software tutorials but as **research-oriented workflows**, linking geospatial theory, computational methods, real-world datasets, quantitative analysis, validation, and environmental decision-making.
Heading 2
======

Heading 3
======
