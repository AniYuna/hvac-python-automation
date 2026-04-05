# HVAC System Automation in Python
These projects demonstrate how Python (Pandas) can be used to automate basic checks of various parameters in HVAC systems.
## About Me
I have experience in HVAC system design and am currently exploring how to combine engineering solutions with data analysis and automation.
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
