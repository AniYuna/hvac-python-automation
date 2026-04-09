# HVAC System Automation in Python

Python (Pandas) scripts for automating validation of HVAC system parameters based on real engineering workflows.

---

## What this solves

In HVAC design, checks like airflow balance, pressure differences, and duct velocities are repetitive and time-consuming when done manually.

These scripts automate such validations to improve speed and consistency.

---

## Scripts

### 1. sauna_check.py
Airflow balance validation.

- reads data from CSV  
- calculates supply/exhaust balance  
- checks pressure conditions  

---

### 2. hvac_file_reader.py
Pressure difference validation.

- reads pressure data  
- checks required limits (e.g. > 20 Pa)  
- outputs simple report  

---

### 3. hvac_vent_velocity_data.py
Duct velocity calculation.

- processes input data with Pandas  
- calculates air velocity  
- exports results to CSV  

---

## Example

Airflow balance check automated instead of manual table verification.

**Result:** faster validation and reduced risk of oversight.

---

## Tech

Python, Pandas
