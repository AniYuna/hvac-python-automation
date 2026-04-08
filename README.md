# HVAC System Automation in Python
These projects demonstrate how Python (Pandas) can be used to automate validation and analysis of HVAC system parameters based on real engineering scenarios.
## About Me
HVAC design engineer with hands-on experience in ventilation systems and building modeling (Revit).
Currently focusing on combining engineering workflows with data analysis and automation using Python.
## Available scripts

### 1. sauna_check.py

Checks airflow balance in a ventilation system.

- reads airflow data from CSV
- calculates supply and exhaust balance
- verifies if required pressure conditions are met

Use case: basic airflow balance check for a single system (e.g. sauna)

---

### 2. hvac_file_reader.py

Analyzes pressure conditions in clean and dirty rooms.

- reads pressure data from CSV
- checks if pressure difference meets required limits (e.g. > 20 Pa)
- generates a simple report

Use case: validation of pressure conditions between different types of rooms

---

### 3. hvac_vent_velocity_data.py

Calculates air velocities in duct cross-sections and exports results.

- creates a multi-column DataFrame from individual data series
- calculates velocity (V = L / (3600 * S)) using the `math` library
- uses the double-bracket technique `[[]]` for advanced DataFrame indexing
- exports the final engineering report to a `.csv` file

Use case: quick aerodynamic check and automated reporting for multiple ventilation branches
