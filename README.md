# HVAC System Automation in Python

This repository demonstrates how Python (Pandas) can be used to automate validation and analysis of HVAC system parameters based on real engineering workflows.

Instead of performing repetitive manual checks, these scripts help quickly verify system performance and identify potential issues.

---

##  Engineering context

In HVAC design, tasks such as airflow balancing, pressure verification, and velocity calculations are often repetitive and time-consuming.

These scripts show how such checks can be automated, allowing engineers to focus on system analysis and decision-making rather than manual validation.

---

##  About Me

HVAC design engineer with hands-on experience in ventilation systems and BIM modeling (Revit).

Currently focused on combining engineering workflows with data analysis and automation using Python.

---

##  Available scripts

### 1. sauna_check.py

Checks airflow balance in a ventilation system.

- reads airflow data from CSV  
- calculates supply and exhaust balance  
- verifies required pressure conditions  

**Use case:**  
Quick validation of airflow balance for a single system (e.g. sauna or small ventilation unit)

---

### 2. hvac_file_reader.py

Analyzes pressure conditions between clean and dirty rooms.

- reads pressure data from CSV  
- checks pressure differences (e.g. > 20 Pa)  
- generates a simple validation report  

**Use case:**  
Verification of pressure zoning requirements in buildings (e.g. medical or industrial spaces)

---

### 3. hvac_vent_velocity_data.py

Calculates air velocities in duct sections and exports results.

- builds structured DataFrame from input data  
- calculates velocity using standard engineering formula  
- exports results to CSV  

**Use case:**  
Automated aerodynamic checks and reporting for multiple ventilation branches
