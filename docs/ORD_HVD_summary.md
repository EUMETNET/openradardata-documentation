# 1. High-Value Datasets (HVD) and Open Radar Data (ORD): Compliance with the HVD scope and requirements


Under [**Commission Implementing Regulation (EU) 2023/138**](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32023R0138&qid=1769496997370), weather radar data are explicitly designated as **High-Value Datasets (HVDs)** within the **meteorological** thematic category. This means that public-sector weather radar data and products must be made openly available under harmonised technical and legal conditions to maximise reuse, innovation, and cross-border applications .

For radar data providers (e.g. National Meteorological Services (NMSs)), this is not just about openness — it sets **concrete requirements on formats, timeliness, access mechanisms, metadata, and licensing**.
Data must be free of charge, provided via APIs (with bulk download options), and licensed under open, machine-readable terms (e.g., Creative Commons BY 4.0).

---

## What radar data and products must be provided as HVDs?

### **Scope**

Radar datasets must include:

* Data **per radar station** within a Member State
* **National radar composites**, where available

### **Required radar variables**

The regulation explicitly lists the following radar products and parameters ([modified terminology](Clarifying the terminology in HVDs)):

* Radar reflectivity factor
* Dual - polarisation variables
* Precipitation rate and accumulated precipitation 
* Radial velocity 
* Echo tops

This implies that **both single-site and composite radar products**, including polarimetric information, fall under the HVD obligation.

---

## Technical requirements for radar data publication

### **1. Update Frequency & Timeliness**

Radar data must be made available:

* With updates every **5 minutes**, or at the **shortest available interval** 

### **2. Access mechanisms**

Radar data must be provided through:

* **APIs** (Application Programming Interfaces), **and**
* **Bulk download**

This ensures both:

* automated, real-time access, and
* efficient retrieval of large historical datasets 

### **3. Data formats**

Radar data must be published in **open, machine-readable formats**, specifically including:

* **HDF5**
* **BUFR** (old data format for the archived data)

### **4. Metadata & documentation**

Radar datasets must be accompanied by:

* **Complete metadata**, published online in an open, widely used machine-readable format
* **Public documentation** describing:

  * data structure
  * semantics
  * variables and conventions used
---

## Legal conditions for reuse

### **Licensing**

Radar HVDs must be made available under:

* **Creative Commons BY 4.0**, or
* an **equivalent or less restrictive open licence**

This allows **free and unrestricted reuse**, including commercial use, provided attribution is given .

### **Cost**

High-Value Datasets must be provided **free of charge**, unless a temporary exemption applies under the Open Data Directive (not typical for meteorological services).

---

## Compliance of ORD API data and product supply with the HVD scope and requirements?

The [datasets in ORD](https://github.com/EUMETNET/openradardata-documentation/blob/main/docs/2-ORD-API-discovering-and-accessing-data.md) are:

1. EUMETNET OPERA single-site radar data

* 24-hour rolling cache, with a long-term archive (2012–, TBD)
* Formats: BUFR (older) and ODIM HDF5 (recent)
* License: CC BY 4.0 (with exceptions noted in metadata)
* Currently mainly includes:
DBZH (Doppler-filtered horizontal reflectivity factor, with national QC applied)
TH (unfiltered horizontal reflectivity factor)
VRADH (horizontal radial velocity)
Basic dual-pol variables (e.g. correlation coefficient, differential reflectivity, differential phase shift, specific differential phase) are planned to be added from 2027 onwards (TBD)
2. European OPERA composite products

Products: maximum reflectivity, instantaneous rain rate, 1-hour accumulation
TBDcoming later)
Formats: ODIM HDF5 and cloud-optimized GeoTIFF (TBD)
License: CC BY 4.0
3. National radar products

Examples of national composites, rain rate composites, accumulations, echo tops
Access: via links to national interfaces (24h access of links)
Formats: ODIM HDF5 or cloud-optimized GeoTIFF


---




---

## Clarifying the terminology in HVDs
The annex in HVD annex table is inaccurate and here are briefly explained the terminology used in radar meteorology. The used terminology in the current key attributes list (https://glossary.ametsoc.org/).

* Reflectivity factor
* Backscatter
* Polarisation variables
* Precipitation
* Wind
* Echotops (echo tops) 



### Reflectivity 
The basic radar variable is actually called radar reflectivity factor, which is stated in units of mm6 m-3 or provided also as dBZ. The radar reflectivity factor is proportional to the reflectivity which again has dimensions of area per unit volume (e.g., cm2m-3, or, more commonly, cm-1 or m-1), however reflectivity is not given as observable of the weather radar.  


### Backscatter
By definition is the scattering of radiant energy into the hemisphere of space bounded by a plane normal to the direction of the incident radiation and lying on the same side as the incident ray. Presumably here it is meant to describe the backscatter coefficient, i.e., the physical quantity used to describe the backscattering process, are m−1 sr−1 (per meter and steradian). This is a measure of the reflective strength of a radar target, however also here, backscatter coefficient is not given directly as a radar observable, but radar reflectivity factor is the used quantity. Therefore, it is assumed that the two first terms of the key attributes list are describing the same radar observable. 


### Polarization
Polarization is general term describing the correlation between two orthogonal components of its electric (or, equivalently, magnetic) field for a transverse electromagnetic wave. With respect to weather radar, here it is probably meant, the radar variables that can be measured with dual-polarization radars. Dual-polarization weather radars measure typically with two linear polarizations, orthogonally horizontal and vertical directions. The basic and operationally measured dual-pol radar variables are differential reflectivity Zdr, propagation differential phase shift (ϕ_dp), and co-polar correlation coefficient (ρ_hv), but there are also other dual-pol variables. However, it is assumed here that in the list of key attributes should not go to this much of detail, but the term the basic dual-polarization variables could be used to describe these observables.      

### Precipitation
Weather radar doesn’t measure precipitation directly, however the instantaneous precipitation rate (mm/h) or rain rate (mm/h) can be derived using retrieval algorithm from the measured radar reflectivity factor. Therefore, it is suggested to be described this quantity either as the basic radar product in general terms or as instantaneous precipitation rate (mm/h) or rain rate (mm/h).   

### Wind
Weather radar doesn’t measure wind directly, however Doppler radars can observe radial velocity component from the hydrometeors or other scatterers in the atmosphere, also known as Doppler velocity. Interpretation of the Doppler velocity depends on the viewing geometry and the kind of target. Clear-air echoes are assumed to move with the wind, so that the Doppler velocity measured at a given location in the atmosphere is equal to the radial component of the wind at that location. Precipitation falls relative to the air, so that the Doppler velocity of a precipitation target is assumed to be the sum of the radial velocity component of the precipitation terminal fall velocity and the radial component of the air motion. To simplify the interpretation, in the list of key attributes the term radial velocity should be used instead of wind.  There is also a radar product called wind profile, but this is not necessarily computed in all Meteorological Services in Europe and computational algorithms differ nationally. 

### Echo tops
Echo top is a product based on radar observations and used often in detection of convective storms. Basically, an echo top is a top of an area of precipitation indicated by the radar. This product is created either from a single or multiple radar volume observations. The definition is depended on the used thresholds to define the cloud top as well as from the wavelength and sensitivity of the radar system. There exist several algorithms how this product can be computed. This is not a direct radar observable, nor it is created in all Meteorological Services in Europe and due to the before-mentioned reasons, this quantity is not comparable between the different member states. Hence, it is suggested to remove this from the list of key attributes.    

