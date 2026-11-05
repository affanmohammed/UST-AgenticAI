# UST Global & UST Global: Gas Compression & Turbomachinery Operational Manual
**Document ID:** UST-OPS-TM-2026-V5  
**Classification:** Restricted / Enterprise Operational Standard & Technical Specification  
**Custodian:** Directorate of Engineering & Operations Infrastructure  
**Partner:** UST Enterprise AI & Industrial Automation Practice  
**Asset Hubs Governed:** Fahud, Marmul, Nimr, Lekhwair, Yibal, Harweel, and Qarn Alam Central Processing Facilities  
**Effective Date:** January 15, 2026 | **Review Cycle:** Annual  

---

## 1. Scope, Executive Governance, and System Architecture

### 1.1 Scope and Operational Intent
This Technical Operations Manual establishes mandatory baseline parameters, engineering safety tolerances, dynamic surge mitigation protocols, condition-monitoring thresholds, and emergency procedures governing all high-pressure centrifugal gas compression trains operated by UST Global (UST) in partnership with UST Global engineering systems. The standards documented herein apply to all mechanical, instrumentation, control, and maintenance personnel deployed across South and North Oman asset operational hubs.

Non-compliance with the boundaries established in this manual constitutes an immediate operational hazard, triggering mandatory management of change (MOC) reviews and potentially invoking safety instrumented system (SIS) interlocks.

### 1.2 System Architecture Overview
Each primary compression train (designated Trains Alpha, Bravo, Charlie, and Delta across regional hubs) comprises a tandem turbomachinery train configured as follows:
1. **Prime Mover Driver**: Industrial two-shaft gas turbine (Solar Taurus 60 or General Electric Frame 6B dual-fuel industrial turbine) delivering shaft power between 5.5 MW and 38.5 MW at ISO conditions.
2. **Speed Increasing Gearbox (SIG)**: Epicyclic or parallel-shaft double-helical speed-increasing transmission with forced lubrication, transforming power turbine shaft speeds (5,500 - 8,200 RPM) to compressor pinion speeds (11,500 - 16,500 RPM).
3. **Centrifugal Compressor Body**: Multi-stage horizontal or barrel-split centrifugal compressor (Dresser-Rand / Baker Hughes / Solar C40/C50 series) equipped with dry gas face seals, active magnetic or hydrodynamic tilt-pad bearings, and dynamic anti-surge recycle valves.
4. **Inter-Stage and After-Cooling System**: High-efficiency air-cooled fin-fan heat exchangers with automated variable-pitch fan blade control to maintain gas suction temperatures between 38°C and 48°C.
5. **Suction Knock-Out Scrubbers**: Multi-cyclone and wire-mesh demister vessels equipped with nuclear and differential-pressure level instrumentation to ensure complete removal of liquid droplets larger than 3 microns prior to impeller entry.

---

## 2. Gas Turbine Driver Operating Envelopes and Combustion Parameters

### 2.1 Turbine Aerodynamic and Thermodynamic Limits
The turbine driver must operate strictly within verified combustion stability envelopes. Any operation outside these limits risks combustion blowout, excessive thermal fatigue on turbine first-stage nozzles, or destructive rotor resonant oscillation.

| Subsystem / Metric | Engineering Unit | Minimum Allowable | Normal Design Range | Level 1 Warning | Level 2 ESD Trip | Response Latency |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Gas Generator Speed (N1) | % of Rated | 78.0 % | 92.0 - 99.5 % | 102.5 % | 105.0 % | 10 ms |
| Power Turbine Speed (N2) | RPM | 8,500 RPM | 14,200 - 14,950 RPM | 15,200 RPM | 15,650 RPM | 10 ms |
| Turbine Exhaust Gas Temp (T7) | °C | 380 °C | 510 - 545 °C | 575 °C | 610 °C | 50 ms |
| T7 Thermocouple Spread ($\Delta T$) | °C | 0 °C | 12 - 28 °C | 42 °C | 65 °C | 100 ms |
| Combustion Chamber Dynamic P | mbar pk-pk | 0.0 mbar | 8.0 - 22.0 mbar | 35.0 mbar | 55.0 mbar | Continuous |
| Fuel Gas Header Supply Pressure | kPa(g) | 2,100 kPa(g) | 2,450 - 2,750 kPa(g) | 2,250 kPa(g) | 1,950 kPa(g) | 200 ms |
| Fuel Gas Superheat above Dewpoint | °C | 20 °C | 35 - 55 °C | 25 °C | 15 °C | 1 sec |

### 2.2 Dual-Fuel Transition Protocols
Transitions between fuel gas and back-up low-sulfur operational distillate diesel must only occur when the turbine load is stabilized between 45% and 70% of continuous maximum rating (MCR). Automated fuel transition sequences are inhibited if:
- Fuel gas hydrocarbon dew point margin falls below 20°C.
- Fuel distillate viscosity exceeds 4.5 cSt at burner inlet manifolds.
- Ambient temperature exceeds 48°C at Fahud or Nimr field stations.

---

## 3. Centrifugal Compressor Technical Specifications and Process Thresholds

### 3.1 Multi-Stage Compression Operating Envelopes
Compression train performance across Fahud and Marmul central processing stations requires strict adherence to thermodynamic compression ratios ($\Pi = P_{discharge} / P_{suction}$) to prevent aerodynamic stall and excessive polytropic discharge temperatures.

| Stage / Component | Parameter Description | Nominal Value | Alarm Level 1 (Warn) | Alarm Level 2 (Trip) | Monitoring System |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1st Stage Suction | Suction Pressure ($P_{s1}$) | 1,250 - 1,400 kPa(g) | 1,150 kPa(g) | 980 kPa(g) | Yokogawa Rosemount DP |
| 1st Stage Suction | Suction Temperature ($T_{s1}$) | 38.0 - 45.0 °C | 52.0 °C | 60.0 °C | Dual Duplex RTD (Pt100) |
| 1st Stage Discharge | Discharge Pressure ($P_{d1}$) | 3,100 - 3,350 kPa(g) | 3,500 kPa(g) | 3,750 kPa(g) | Smart Pressure Transmitter |
| 2nd Stage Suction | Interstage Pressure ($P_{s2}$) | 3,020 - 3,250 kPa(g) | 2,850 kPa(g) | 2,600 kPa(g) | Smart Pressure Transmitter |
| Final Discharge | Final Discharge Pressure ($P_{d2}$) | 6,800 - 7,200 kPa(g) | 7,450 kPa(g) | 7,850 kPa(g) | 2oo3 Voting Triple SIS |
| Final Discharge | Final Discharge Temp ($T_{d2}$) | 115.0 - 132.0 °C | 145.0 °C | 158.0 °C | 2oo3 Thermocouple |
| Balance Piston | Balance Line Differential P | 12.0 - 25.0 kPa | 45.0 kPa | 65.0 kPa | Differential P Transmitter |
| Casing Shell | Shell Metal Skin Temperature | 65.0 - 95.0 °C | 115.0 °C | 130.0 °C | Surface Skin RTDs |

---

## 4. Aerodynamic Surge Protection and Dynamic Anti-Surge Control Valves (ASCV)

### 4.1 Aerodynamic Surge Physics and Consequences
Centrifugal compressor surge is an unstable aerodynamic operational state occurring when gas volumetric throughput through the impellers drops below the critical Surge Limit Line (SLL). At this boundary, aerodynamic boundary layers detach from impeller blades, reversing flow from discharge to suction at frequencies between 0.5 Hz and 4.0 Hz. 

Unmitigated surge causes:
- Instantaneous axial thrust reversal exceeding 120 kN, destroying magnetic thrust collars and tilt-pad bearings.
- Rapid gas overheating within 1.5 seconds, damaging dry gas seal elastomers and labyrinth seals.
- Mechanical contact between rotating impellers and stationary diaphragms, causing catastrophic rotor seizure.

### 4.2 ASCV Modulation Algorithms and Dynamic Safety Margins
To prevent surge excursion, each train is equipped with two redundant fast-acting pneumatically actuated Anti-Surge Control Valves (ASCV-301A and ASCV-301B):
1. **Surge Deviation Calculation**: The anti-surge controller continuously computes operating margin ($\Delta S$) relative to the Surge Control Line (SCL):
   $$\Delta S = rac{Q_{actual} - Q_{surge}}{Q_{surge}}$$
   Where $Q_{actual}$ represents volumetric suction flow and $Q_{surge}$ represents predicted flow at the current pressure ratio.
2. **Standard Proportional-Integral Response**: When $\Delta S > 0.12$, normal PI modulation maintains stable operating distance.
3. **Open-Loop Step-Response Ingress**: If operating point rapidly traverses toward the surge line with $d(\Delta S)/dt < -0.05 	ext{ sec}^{-1}$ or $\Delta S < 0.08$, the controller commands the ASCV actuator to open within **350 milliseconds**, bypassing discharge gas through the recycling loop back to the suction scrubber inlet cooler.
4. **Emergency Blowdown Depressurization**: If $\Delta S < 0.02$ or if reverse flow detection sensors trigger, the emergency shutdown system locks the ASCV 100% full-open and triggers emergency blowdown valve BDV-401 to vent compressor inventory to high-pressure flare within **2.8 seconds**.

---

## 5. Tandem Dry Gas Seal (DGS) Subsystems and Condition Monitoring

### 5.1 Dry Gas Seal Configuration
All gas compressors utilize tandem dry gas mechanical seal cartridges (John Crane Type 28AT or EagleBurgmann DGS series) configured with an intermediate labyrinth and nitrogen safety containment:
- **Primary Seal Stage**: Absorbs full process differential pressure (up to 75 bar).
- **Secondary Safety Containment Stage**: Operates at low pressure (2.0 - 4.5 bar), acting as absolute containment if the primary seal face fails.
- **Buffer Supply**: Conditioned dry fuel gas filtered to 1.0 micron absolute, superheated to 25°C above dew point, injected at $\Delta P \ge 3.5 	ext{ bar}$ above process suction pressure.

### 5.2 Dry Gas Seal Safety Operating Boundaries

| Seal Parameter | Unit | Normal Operating | Level 1 Warning | Level 2 ESD Trip | Corrective Action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Primary Vent Leakage Flow | Nm³/hr | 8.0 - 24.0 Nm³/hr | 45.0 Nm³/hr | 90.0 Nm³/hr | Immediate train blowdown to flare |
| Secondary Vent Leakage Flow | Nm³/hr | 0.5 - 2.5 Nm³/hr | 8.0 Nm³/hr | 18.0 Nm³/hr | Switch to secondary nitrogen purge |
| Buffer Gas $\Delta P$ (Seal vs Suction) | bar | 4.2 - 6.5 bar | 3.5 bar | 2.2 bar | Verify booster pump & filter DP |
| Primary Vent Line Pressure | kPa(g) | 12.0 - 28.0 kPa(g) | 55.0 kPa(g) | 95.0 kPa(g) | Check flare backpressure orifice |
| Separation Nitrogen Supply P | bar(g) | 6.5 - 8.5 bar(g) | 5.5 bar(g) | 4.0 bar(g) | Verify central nitrogen generation bank |
| Seal Face Metal Temperature | °C | 42.0 - 68.0 °C | 88.0 °C | 105.0 °C | Check buffer cooling and flow rates |

---

## 6. Forced Lubricating Oil Circulating Systems and Hydraulic Controls

### 6.1 Lube Oil Specification and Quality Standards
All turbomachinery trains share a closed-loop forced lubrication system charged with synthetic polyol-ester or highly refined mineral turbine oil meeting ISO VG 32 viscosity grade standards (UST Material Code: UST-LUB-SYN-32).
- Cleanliness standard: ISO 4406 cleanliness code must be maintained at **15/13/10** or better.
- Moisture limit: Dissolved water content must remain strictly below **80 ppm** (parts per million).

### 6.2 Lube Oil Operating Tolerances and Filtration Limits
1. **Supply Temperature**: Controlled via thermostatically modulated three-way mixing valves to maintain header temperature at **45°C - 55°C**. If header temperature exceeds **62°C**, Level 1 warning triggers; at **70°C**, emergency turbine shutdown is initiated.
2. **Header Supply Pressure**: Maintained at **2.4 - 3.2 bar(g)**. If pressure drops below **1.8 bar(g)**, the auxiliary AC electric motor-driven lube oil pump starts automatically within 0.8 seconds. If pressure falls below **1.2 bar(g)**, the DC emergency rundown pump starts and triggers Level 2 ESD.
3. **Duplex Filter Differential Pressure**: Clean filter $\Delta P \le 0.4 	ext{ bar}$. When $\Delta P \ge 1.5 	ext{ bar}$, automated warning instructs operations to switch filter banks and replace dirty synthetic micro-glass cartridges.

---

## 7. Functional Safety Instrumented Systems (SIS) & SIL-3 Emergency Shutdown Matrix

### 7.1 Safety Integrity Level (SIL) Standards
All safety-critical instrumented loops on Fahud, Marmul, and Nimr turbomachinery trains conform strictly to IEC 61508 / IEC 61511 Safety Integrity Level 3 (SIL-3) architecture with triple modular redundancy (2oo3 voting logic).

### 7.2 Emergency Shutdown Hierarchy
The safety system implements four distinct, non-bypassable shutdown levels:
- **ESD-0 (Facility Total Blackout & Depressurization)**: Initiated by facility-wide fire and gas detection or catastrophic hydrocarbon cloud release. Trips all turbines, activates deluge systems, and vents all process vessels to flare.
- **ESD-1 (Asset Compression Train Isolation & Fast Blowdown)**: Initiated by severe process breaches (e.g. Primary Seal vent flow > 90 Nm³/hr, compressor discharge overpressure > 7,850 kPa). Isolates train suction/discharge valves and completes 100% depressurization via BDV-401 within 180 seconds.
- **ESD-2 (Controlled Mechanical Train Trip)**: Initiated by critical mechanical anomalies (vibration > 52 µm pk-pk, turbine exhaust overtemperature > 610°C, lube oil loss). Cuts fuel gas instantly, engages starter barring gear, but maintains process pressure intact to prevent flare venting.
- **ESD-3 (Operational Controlled Cooldown & Idle)**: Operator-initiated ramp-down for planned maintenance or non-urgent warning conditions. Unloads compressor, idles turbine for 15 minutes cooldown, then shuts down.

---

## 8. Predictive Maintenance Cycles, Overhauls, and Hydrostatic Testing Protocols

### 8.1 Maintenance Intervals and Preventive Routines
All maintenance operations must be planned in SAP PM and logged in the UST Enterprise Asset Management (EAM) repository with certified technician sign-offs.

| Frequency / Operating Hours | Maintenance Action Item | Inspection Standard | Custodian Team |
| :--- | :--- | :--- | :--- |
| Every 500 Running Hours | Lube oil laboratory spectrometry analysis (viscosity, TAN, wear metals) | ASTM D5185 / ISO 4406 | Field Chemical Laboratory |
| Every 4,000 Running Hours | Duplex lube oil filter cartridges and seal gas coalescing filter replacement | Manufacturer Spec | Mechanical Maintenance |
| Every 8,000 Running Hours | Turbine boroscope inspection of combustor liner, transition pieces, and stage 1 nozzles | OEM Visual Borescope Standard | Turbomachinery Specialist |
| Every 16,000 Running Hours | Anti-surge valve full-stroke dynamic calibration, seat leakage testing, pneumatic proof test | IEC 60534-4 Class V | Instrumentation & Control |
| Every 24,000 Running Hours | Gas Turbine Hot Gas Path (HGP) complete overhaul and rotor blade renewal | OEM Factory Overhaul Standard | Specialized OEM Contractor |
| Every 36 Months | Centrifugal compressor outer barrel casing hydrostatic integrity pressure testing | 1.5x MAWP sustained 4 hours | Certified Third-Party Inspection (TPI) |
| Every 48,000 Running Hours | Complete train major overhaul including rotor extraction, diaphragm de-scaling, bearing renewal | API 617 8th Edition | Lead Turnaround Team |

### 8.2 Hydrostatic Pressure Integrity Verification Standard
Every **36 months**, the compressor outer barrel casing must undergo certified hydrostatic integrity verification:
1. All process nozzles must be blanked with ASME Class 900 certified blind flanges.
2. Casing filled with treated demineralized water containing corrosion inhibitor (UST-CHEM-CI-04).
3. Test pressure raised incrementally to **1.5x Maximum Allowable Working Pressure (MAWP)**.
4. Test pressure sustained continuously for **4.0 hours** minimum with calibrated digital pressure logging. Zero pressure drop allowed after temperature equalization.
5. All tests must be witnessed and certified by an independent Third-Party Inspection (TPI) agency.

---

## 9. Rotor Dynamics, Vibration Monitoring, and Spectral Diagnostics

### 9.1 Vibration Sensor Placement and Thresholds
Each bearing housing is equipped with dual orthogonal eddy-current non-contact proximity probes (Bently Nevada 3500 rack system) positioned at 45° Left and 45° Right relative to vertical top dead center.
- **Nominal Baseline**: 12.0 - 24.0 µm peak-to-peak.
- **Level 1 Alert (Warning)**: **38.0 µm peak-to-peak**. Triggers automated vibration spectrum capture and dispatching of vibration diagnostic specialist.
- **Level 2 Action (ESD Trip)**: **52.0 µm peak-to-peak** sustained for 1.2 seconds. Initiates immediate ESD-2 mechanical trip.

### 9.2 Fast Fourier Transform (FFT) Spectral Fault Diagnosis
Vibration data analysts must apply the following fault signature diagnostic matrix:
- **1X Running Frequency Dominance (>80% of overall amplitude)**: Indicates mechanical rotor unbalance. Rotor dynamic re-balancing must meet ISO 1940-1 Grade G1.0 tolerance limits.
- **2X Running Frequency Dominance with 180° Phase Shift**: Indicates mechanical shaft misalignment across the speed-increasing gearbox coupling. Re-alignment requires laser optical alignment tools to within 0.05 mm offset.
- **Sub-synchronous Peak at 0.42X - 0.48X Running Speed**: Indicates dangerous hydrodynamic oil whirl or oil whip in tilt-pad journal bearings. Requires immediate lube oil temperature adjustment and bearing clearance verification.

---

## 10. Corporate Governance, Omanization Mandates, and UST AI Implementation

### 10.1 Omanization Workforce Quota Requirements
As governed by Ministerial Decision 22/2026 and UST Global Corporate Governance Directive Section 2.1:
- All engineering, operational, and maintenance teams deployed on Fahud, Marmul, Nimr, and Lekhwair assets must maintain a minimum verified **Omanization ratio of 68%** certified technical personnel.
- All lead control room operator (CRO) and turbomachinery superintendent roles must be staffed by certified Omani national engineers.
- Contractor organizations failing to maintain verified monthly staffing records are subject to contractual withholding of 15% on monthly invoice disbursements.

### 10.2 UST Enterprise AI & RAG System Integration
In partnership with UST Global, all technical operations data, sensor telemetry, incident history, and standard operating procedures documented in this manual are digitized and indexed within the **Enterprise Context Engineering & RAG Platform**:
- Real-time SCADA feeds from Yokogawa CENTUM VP DCS and Bently Nevada systems are continuously streamed into the vector and knowledge-graph repository.
- Operational queries submitted by field engineers (e.g., via mobile field terminals or control room consoles) are parsed, chunked, verified through strict guardrails, and answered with strict citations back to this manual.
- Grounding and faithfulness metrics must be audited continuously to eliminate hallucination risks on critical safety-instrumented systems.

---
*End of Operational Manual — UST-OPS-TM-2026-V5*
