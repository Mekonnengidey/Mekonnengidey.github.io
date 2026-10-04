---

#layout: default
title: "Sentinel-1 InSAR Surface Deformation Analysis — Afar, Ethiopia, teaser,icon"
thumbnail: "insar-teaser-title-results.png"
#permalink: /portfolio/portfolio-2/
excerpt: " A complete single-pair Differential SAR Interferometry (DInSAR) workflow using Sentinel-1 SLC imagery to investigate surface deformation around the Afar volcanic region. The analysis moves from complex SAR phase to an interpretable line-of-sight (LOS) displacement map, while explicitly examining coherence, filtering, phase unwrapping, geocoding, and the limitations of a single interferometric pair."
collection: portfolio

---

<!-- Paste the contents of portfolio-2.md below this front matter if your site uses this layout. -->

<!-- # Sentinel-1 InSAR Surface Deformation Analysis — Afar, Ethiopia -->

**Case study By Mekonnen Gidey| Advanced Remote Sensing, MSc Geoinformation Science |Bahir Dar University | May 2026**


![InSAR title-page teaser: interferometric fringes and derived displacement](/images/insar-teaser-title-results.png)

## 1. Case-study question

Can a repeat-pass Sentinel-1 SLC pair be processed into a spatially interpretable surface-deformation product over the Afar volcanic region, and what do the interferometric phase, coherence, unwrapped phase, and LOS displacement reveal about the observed deformation pattern?

This case study is based on an Advanced Remote Sensing practical assignment. The original manual describes the objective as developing an interferogram from a Sentinel-1 SLC pair, identifying the volcanic craters involved, and measuring surface deformation/displacement between the acquisition dates. fileciteturn0file0L15-L23

> **Scope:** This is presented as a research-style case study, not as a fully validated scientific paper. The source explicitly notes that a single image pair requires external reference data for validation and recommends multi-date analysis to reduce atmospheric and unwrapping effects. fileciteturn0file0L552-L561

---

## 2. Study context

The study area is the **Afar region around Guba Haili / Hayli Gubbi and Erta Ale, Ethiopia**, a volcanic environment where surface movement is of direct interest. The manual frames the analysis around eruption activity reported on **23 November 2025**. fileciteturn0file0L18-L23

![Afar / Guba Haili study area](/images/study-area-afar-guba-haili.png)

*Study-area context reproduced from the practical manual.*

### Why InSAR is useful here

InSAR exploits the phase difference between two complex SAR observations acquired from slightly different sensor positions. After coregistration, the interferometric phase contains contributions from terrain, orbital/flat-earth effects, atmospheric conditions, noise, and possible surface deformation. Differential processing removes the modeled flat-earth and topographic contributions so that the remaining phase can be interpreted primarily in terms of deformation, atmosphere, and residual noise. fileciteturn0file0L24-L40

The central phase model used in the workflow is:

$$\phi = \phi_{DEM} + \phi_{flat} + \phi_{disp} + \phi_{atm} + \phi_{noise}$$

and, after removing the modeled terrain and flat-earth components:

$$\phi_{disp}+\phi_{atm}+\phi_{noise}=\phi-\phi_{DEM}-\phi_{flat}$$

fileciteturn0file0L191-L214

---

## 3. Data and processing environment

| Component | Case-study specification |
|---|---|
| Sensor | Sentinel-1 SAR |
| Product | Level-1 SLC, IW mode, dual polarization product; VV selected for this workflow |
| Acquisition 1 | 19 November 2025, 15:26:35 UTC |
| Acquisition 2 | 25 November 2025, 15:27:34 UTC |
| Study area | Afar / Guba Haili area, Ethiopia |
| Selected sub-swath | IW2 |
| Selected bursts | 1–5 |
| DEM | SRTM 1Sec HGT, auto-downloaded in SNAP |
| Software | ESA SNAP 13 |
| Phase unwrapping | SNAPHU via SNAP plugin |
| Final displacement | Line-of-sight displacement in metres |

The two source products are explicitly listed in the manual as Sentinel-1C and Sentinel-1A IW SLC products acquired on 19 and 25 November 2025. fileciteturn0file0L54-L62 The workflow selects IW2 and bursts 1–5 to isolate the area of interest. fileciteturn0file0L132-L149

### Sentinel-1 acquisition geometry

![Sentinel-1 IW sub-swaths](/images/sentinel1-iw-sub-swaths.png)

*IW acquisition is organized into three TOPSAR sub-swaths; the study area is handled within IW2.*

![Study-area location in the Sentinel-1 product](/images/product-world-map-study-area.png)

*World-view/product inspection used to locate the study area and check acquisition geometry.*

---

# 4. Methodology

The workflow is deliberately shown as a processing chain rather than a long procedural narrative. Each stage changes the representation of the SAR information and prepares the next scientific interpretation.

| Stage | Operation | Main input | Purpose | Main output / decision |
|---|---|---|---|---|
| 1 | TOPS Split | Two IW SLC products | Keep only relevant sub-swath/bursts | IW2, bursts 1–5 |
| 2 | Apply Orbit File | Split SLCs | Improve satellite-position information | Orbit-corrected products |
| 3 | Back Geocoding | Two orbit-corrected SLCs + DEM | Precisely coregister master/secondary | Coregistered stack |
| 4 | Enhanced Spectral Diversity | Multi-burst stack | Refine range/azimuth alignment | ESD-corrected stack |
| 5 | Interferogram + coherence | Coregistered stack | Estimate phase difference and phase quality | Wrapped interferogram + coherence |
| 6 | TOPS Deburst | Interferogram | Remove burst seamlines | Continuous burst mosaic |
| 7 | Goldstein filtering | Debursted phase | Improve fringe signal-to-noise ratio | Filtered phase |
| 8 | Subset | Filtered interferogram | Focus processing on the analysis area | Working subset |
| 9 | SNAPHU export / unwrap / import | Wrapped phase + coherence | Resolve the 2π phase ambiguity | Unwrapped phase |
| 10 | Phase to Displacement | Unwrapped phase | Convert phase to metric LOS change | LOS displacement |
| 11 | Terrain Correction | Displacement + DEM | Geocode and correct SAR geometry | Map-projected displacement |
| 12 | Interpretation | Final maps + histogram | Relate phase patterns to deformation | Spatial deformation interpretation |

The processing logic follows the manual's sequence from TOPS splitting through orbit correction, coregistration/ESD, interferogram formation, debursting, filtering, subsetting, unwrapping, phase-to-displacement conversion, and terrain correction. fileciteturn0file0L132-L190 fileciteturn0file0L272-L320 fileciteturn0file0L325-L348 fileciteturn0file0L455-L491

---

## 5. Pre-processing: making the pair interferometrically usable

### TOPS split — reduce the problem to the relevant bursts

The study area falls within IW2 and bursts 1–5. Selecting only these bursts reduces the processing volume while retaining the area needed for analysis. fileciteturn0file0L132-L149

![TOPS Split showing IW2 and bursts 1–5](/images/tops-split-bursts-1-5.png)

### Orbit correction and back geocoding

Orbit information is applied before coregistration. SNAP then uses orbit information and a DEM to coregister the two SLCs through Sentinel-1 TOPS Back Geocoding. fileciteturn0file0L150-L179

![Apply Orbit File](/images/apply-orbit-file.png)

![Back Geocoding](/images/back-geocoding.png)

For this case, the manual notes that ESD is required because multiple bursts were selected; it refines range and azimuth shifts between the secondary and reference images. fileciteturn0file0L184-L190

---

# 6. Interferogram formation and coherence

The interferogram is produced by cross-multiplying the reference image with the complex conjugate of the secondary image. The resulting phase is not automatically deformation: it is a mixture of terrain, flat-earth, atmosphere, noise, and displacement contributions. fileciteturn0file0L191-L204

![Interferogram formation settings](/images/interferogram-formation-settings.png)

### The first critical diagnostic: coherence

Coherence is an essential quality indicator because phase measurements become unreliable where the two acquisitions are not sufficiently similar. The manual identifies temporal, geometric, and volumetric decorrelation as major causes and notes particularly poor repeat-pass coherence over dense vegetation with C-band Sentinel-1. fileciteturn0file0L215-L228

<table>
<tr><td><img src="/images/interferogram-phase.png" alt="Wrapped interferogram phase"></td><td><img src="/images/coherence-map.png" alt="Coherence map"></td></tr>
<tr><tr><td><strong>Wrapped interferometric phase</strong><br>Phase is represented from −π to +π as repeating fringe cycles.</td><td><strong>Coherence</strong><br>Bright areas provide stronger phase information; dark areas are less reliable.</td></tr>
</table>

The manual reports high coherence in urban/agricultural areas and low coherence in forest, with values below about 0.3 described as problematic for reliable later unwrapping. fileciteturn0file0L259-L271

---

# 7. Cleaning and stabilizing the phase

### Deburst → filter → subset

The three operations progressively prepare the interferogram for phase unwrapping:

1. **TOPS Deburst** removes the seamlines between bursts.
2. **Goldstein phase filtering** improves the signal-to-noise ratio of the existing fringe pattern; it cannot recover phase information already lost to decorrelation.
3. **Subset** focuses the computational product on the analysis area and removes unwanted edge regions. fileciteturn0file0L272-L320

![Goldstein filtering: before and after](/images/goldstein-filter-before-after.png)

*The filter is used to improve the quality of existing phase fringes before unwrapping; coherence itself is not changed by this operation.* fileciteturn0file0L283-L293

---

# 8. Phase unwrapping

Wrapped interferometric phase is ambiguous within a 2π cycle. Unwrapping estimates the continuous phase by resolving the integer number of cycles between neighboring pixels. The result is therefore a relative phase-derived quantity, and reliable unwrapping depends strongly on coherence. The manual suggests a minimum coherence around 0.3 as a practical guide. fileciteturn0file0L325-L344

![Wrapped versus unwrapped phase principle](/images/phase-unwrapping-principle.png)

### SNAPHU implementation

The workflow exports the wrapped phase and configuration from SNAP, runs SNAPHU, then imports the resulting unwrapped phase back into SNAP. The DEFO statistical-cost mode is used in the documented workflow. fileciteturn0file0L358-L372

![SNAPHU export settings](/images/snaphu-export-settings.png)

![SNAPHU unwrapping progress](/images/snaphu-unwrapping-progress.png)

![SNAPHU import](/images/snaphu-import.png)

The manual recommends checking the imported result visually: a successful result should be relatively smooth except around areas of expected deformation, while low-coherence regions and complex urban structures can produce unwrapping errors. fileciteturn0file0L421-L450

![Unwrapped phase result](/images/unwrapped-phase-result.png)

---

# 9. From phase to physical displacement

The unwrapped phase is continuous but is not yet a metric displacement. The **Phase to Displacement** operator converts it into surface change along the radar line of sight (LOS), in metres. The manual interprets positive values as uplift and negative values as subsidence. fileciteturn0file0L455-L470

<table>
<tr><td><img src="/images/phase-to-displacement-result.png" alt="Phase to displacement result"></td><td><img src="/images/los-displacement-histogram.png" alt="LOS displacement histogram"></td></tr>
<tr><td><strong>Unwrapped phase → displacement</strong><br>The phase is converted into a metric LOS displacement field.</td><td><strong>Displacement distribution</strong><br>The histogram provides a useful diagnostic of the spatial value distribution and the effect of the display stretch.</td></tr>
</table>

---

# 10. Terrain correction and final geocoded product

Terrain correction converts the SAR product from slant/ground-range geometry into a map-projected product and uses a DEM to correct geometric distortions such as foreshortening, layover, and shadow. The documented workflow uses SRTM 1Sec HGT and allows either WGS84 geographic coordinates or UTM for GIS use. fileciteturn0file0L474-L491

![Terrain correction settings](/images/terrain-correction-result.png)

![Final interferogram](/images/final-interferogram.png)

![Final LOS displacement map](/images/final-los-displacement-map.png)

---

# 11. Results: what the maps show

### Spatial deformation pattern

The final interpretation in the manual focuses on deformation near **Erta Ale and Hayli Gubbi**. Dense, closely spaced fringes around Erta Ale are interpreted as a strong spatial gradient of ground displacement. fileciteturn0file0L513-L528

| Final-product evidence | Interpretation reported in the case study |
|---|---|
| Dense concentric interferometric fringes | Strong spatial gradient of displacement around the volcanic area |
| Blue/green negative-displacement zone | Subsidence/sinking pattern, with the displayed scale reaching about **−0.146 m** |
| Bright/white positive-displacement zone | Uplift/inflation pattern, with the displayed scale reaching about **+0.034 m** |
| Yellow / near-zero zone | Relatively stable area |
| Full metadata range | True minimum about **−0.471 m** and maximum about **+0.150 m** |

These values come from the manual's interpretation of the final products. Importantly, the manual distinguishes the **true metadata extrema** from the **display/color-bar range**: the display is stretched/clipped around the main distribution so that a few extreme/noisy pixels do not dominate the visualization. fileciteturn0file0L529-L550

### Why the display range matters

The apparent map range is therefore not necessarily the same as the absolute raster range. This is a useful example of why remote-sensing interpretation should inspect both the raster statistics and the visualization stretch before reporting a numerical deformation magnitude.

![Unwrapped phase and LOS displacement histograms](/images/unwrapped-phase-histogram.png)

![LOS displacement histogram](/images/los-displacement-histogram.png)

---

# 12. Critical analysis

## What is convincing in the result?

**The processing chain is internally coherent.** The workflow progresses through the major transformations required for a repeat-pass InSAR displacement product: precise image alignment, phase formation, coherence assessment, phase cleaning, ambiguity resolution, metric conversion, and geocoding.

**The coherence map provides an explicit quality-control layer.** Instead of interpreting every fringe equally, the workflow recognizes that phase quality varies spatially and that low-coherence areas can contaminate unwrapping. fileciteturn0file0L215-L228

**The final deformation map is physically interpretable.** The result can be discussed in metres along the radar LOS rather than only as abstract phase cycles. fileciteturn0file0L455-L470

## What cannot be claimed from this experiment?

This is the most important research limitation. The manual itself states that the reliability of a single-pair displacement result remains uncertain without external reference data. Atmospheric phase contributions and unwrapping errors can also affect the result. fileciteturn0file0L552-L557

Therefore, this portfolio **does not claim independent validation of the reported deformation magnitudes**. It demonstrates a complete and technically reasoned InSAR workflow and documents the resulting spatial pattern.

A stronger scientific study would:

- process a longer Sentinel-1 time series rather than one pair;
- compare consecutive acquisition pairs;
- average or otherwise model multi-date results to reduce atmospheric and unwrapping effects;
- introduce independent reference observations for validation; and
- report uncertainty alongside deformation magnitude.

The first three extensions are directly recommended in the source manual. fileciteturn0file0L552-L561

---

# 13. Research-style interpretation

The practical demonstrates a useful **Earth-observation measurement pipeline**:

**Complex SAR observations**
→ **precise coregistration**
→ **interferometric phase**
→ **coherence-based quality assessment**
→ **phase filtering**
→ **phase unwrapping**
→ **LOS displacement**
→ **terrain-corrected spatial interpretation**

The important methodological lesson is that the final map is not simply an image product. It is the endpoint of a sequence of assumptions and quality controls. In particular, coherence, atmospheric effects, phase ambiguity, DEM/topographic removal, and visualization range all affect how the deformation map should be interpreted.

---

# 14. Technical contribution / skills demonstrated

| Area | Demonstrated capability |
|---|---|
| SAR | Working with Sentinel-1 IW SLC data and complex phase information |
| InSAR | Interferogram formation, coherence estimation, phase interpretation |
| DInSAR | Removal of flat-earth and DEM-related phase contributions for deformation analysis |
| SNAP | End-to-end Sentinel-1 InSAR processing in SNAP 13 |
| SNAPHU | External phase unwrapping integrated through the SNAP plugin |
| DEM integration | SRTM-based coregistration and terrain correction |
| Geospatial interpretation | LOS displacement mapping, histogram inspection, spatial pattern interpretation |
| Critical analysis | Recognition of decorrelation, atmospheric contamination, unwrapping errors, outliers and validation limitations |

---

# 15. Reproducibility

**Software:** ESA SNAP 13 + SNAPHU plugin  
**Input:** Sentinel-1 SLC pair dated 19 and 25 November 2025  
**Study-area selection:** IW2, bursts 1–5, VV  
**DEM:** SRTM 1Sec HGT  
**Output:** terrain-corrected LOS displacement raster and associated interferometric products

The source manual provides the processing parameters, intermediate product naming, and operator sequence needed to reproduce the workflow. For example, the documented subset is saved as `20251119_20251125_split_Orb_Stack_esd_ifg_deb_flt_subset.dim`. fileciteturn0file0L294-L321

---

# 16. From course practical to research direction

This case study is a useful foundation for moving from **single-pair demonstration** toward **multi-temporal SAR research**. The immediate research opportunity is to replace the single interferometric pair with a time series, quantify temporal consistency, separate persistent deformation from atmospheric artefacts, and validate the resulting deformation signal against independent observations.

That progression is particularly relevant to broader work in SAR, InSAR, time-series Earth observation, environmental monitoring, and geospatial AI.

---

## References

1. Roca et al. (1997). *InSAR Principles: Guidelines for SAR Interferometry Processing and Interpretation* (ESA TM-19).
2. European Space Agency. *S1TBX Stripmap Interferometry with Sentinel-1 Tutorial, Version 2.*
3. European Space Agency. *InSAR Displacement Mapping with ERS Data.*
4. European Space Agency. *S1TBX DEM Generation with Sentinel-1 IW Tutorial.*

The references above are those listed in the original practical manual. fileciteturn0file0L565-L577

---

### Project record

**Course:** Advanced Remote Sensing  
**Programme:** MSc Geoinformation Science  
**Institution:** Bahir Dar University, Department of Geography and Environmental Studies  
**Submitted to:** Dr. Daniel Ayalew  
**Date:** 20 May 2026

---

> **Portfolio note:** This page intentionally uses figures, diagnostic maps, and compact tables as the primary narrative. The goal is to let a reader understand the measurement chain and evaluate the evidence without having to read the original 28-page practical manual line by line.
