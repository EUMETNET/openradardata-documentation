# 1. Overview

The **Open Radar Data (ORD) API** is designed to fulfill the EU Implementing Regulation (EU) 2023/138 of the EU Open Data Directive (EU) 2019/1024 for the  (High Value Datasets (HVDs))[https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32023R0138&qid=1769496997370] defining the weather radar observations.  

Data must be free of charge, provided via APIs (with bulk download options), and licensed under open, machine-readable terms (e.g., Creative Commons BY 4.0).

Great topic — this regulation is *very* relevant for radar data portals 👍
Below is a **website-ready summary** focused on **what “High-Value Datasets (HVD)” mean for weather radar data**, with a **clear emphasis on Section 3 (Meteorological) of the Annex**, especially **radar data**. I’ll keep it explanatory rather than legalistic, so it works for informing users.

---

## High-Value Datasets (HVD) and Weather Radar Data — What Does It Mean?

Under **Commission Implementing Regulation (EU) 2023/138**, weather radar data are explicitly designated as **High-Value Datasets (HVDs)** within the **Meteorological** thematic category. This means that public-sector weather radar data must be made openly available under harmonised technical and legal conditions to maximise reuse, innovation, and cross-border applications .

For radar data providers (e.g. national meteorological services), this is not just about openness — it sets **concrete requirements on formats, timeliness, access mechanisms, metadata, and licensing**.

---

## What Counts as High-Value Meteorological Data?

The regulation defines five types of meteorological datasets:

* Weather station observations
* Climate (validated) observations
* Weather alerts
* **Radar data**
* Numerical Weather Prediction (NWP) model data

Weather radar data are therefore **explicitly in scope**, alongside observations and models .

---

## What Radar Data Must Be Provided?

### **Scope**

Radar datasets must include:

* Data **per radar station** within a Member State
* **National radar composites**, where available

### **Required radar variables**

The regulation explicitly lists the following radar products and parameters:

* Reflectivity
* Backscatter
* Polarisation variables
* Precipitation
* Wind
* Echotops (echo tops) 

This implies that **both single-site and composite radar products**, including polarimetric information, fall under the HVD obligation.

---

## Technical Requirements for Radar Data Publication

### **1. Update Frequency & Timeliness**

Radar data must be made available:

* **Near real time**
* With updates every **5 minutes**, or at the **shortest available interval** 

This is a key requirement for nowcasting, aviation, hydrology, and emergency response use cases.

---

### **2. Access Mechanisms**

Radar data must be provided through:

* **APIs** (Application Programming Interfaces), **and**
* **Bulk download**

This ensures both:

* automated, real-time access, and
* efficient retrieval of large historical datasets .

---

### **3. Data Formats**

Radar data must be published in **open, machine-readable formats**, specifically including:

* **HDF5**
* **BUFR**
* **GRIB** (or NetCDF as an alternative)

Other internationally recognised open formats are also acceptable, provided they are well documented .

---

### **4. Metadata & Documentation**

Radar datasets must be accompanied by:

* **Complete metadata**, published online in an open, widely used machine-readable format
* **Public documentation** describing:

  * data structure
  * semantics
  * variables and conventions used

The regulation explicitly refers to INSPIRE-aligned documentation as an example of good practice .

---

## Legal Conditions for Reuse

### **Licensing**

Radar HVDs must be made available under:

* **Creative Commons BY 4.0**, or
* an **equivalent or less restrictive open licence**

This allows **free and unrestricted reuse**, including commercial use, provided attribution is given .

---

### **Cost**

High-Value Datasets must be provided **free of charge**, unless a temporary exemption applies under the Open Data Directive (not typical for meteorological services).

---

## API Quality & Operational Requirements (Applies to All HVDs)

Radar data APIs must also comply with general HVD rules:

* Publicly documented **terms of use**
* Published **quality-of-service criteria** (availability, capacity, performance)
* A designated **point of contact** for API users
* Datasets clearly marked as **“High-Value Dataset”** in their metadata .

---

## What This Means in Practice for Radar Data Users

For users, this regulation ensures that weather radar data across Europe are:

* **Openly licensed and free to use**
* **Accessible programmatically via APIs**
* **Available in near real time**
* **Provided in standard scientific formats**
* **Comparable and interoperable across countries**

This significantly lowers barriers for:

* research
* cross-border applications
* AI and machine learning
* nowcasting, hydrology, aviation, and climate services.

---

If you want, next I can:

* turn this into **short website sections / FAQs**,
* write a **“What does this mean for radar users?”** box, or
* help you map these requirements to **your existing radar data services** (e.g. FMI / NORDRAD context).

---

## What are the High Value Dataset requirements for weather radar data 


---

## Clarifying the terminology in HVDs
The annex in HVD annex table is inaccurate and here are briefly explained the terminology used in radar meteorology. The used terminology in the current key attributes list (https://glossary.ametsoc.org/).

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

