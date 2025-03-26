# Emergency Medical Information System

This system provides a local database solution for storing and accessing patient medical information. It consists of two main interfaces:
1. Medical Officer Interface - for hospital staff to manage patient records
2. Paramedic Interface - for emergency responders to quickly access critical patient information

## Features

- Store patient information including:
  - Name and contact details
  - Blood type
  - Allergies
  - Medical conditions
  - Emergency contact information
- Update patient records during hospital visits
- Quick access to critical information for emergency responders
- Local database storage (no internet connection required)

## Requirements

- Python 3.6 or higher
- SQLite3 (usually comes with Python)

## Installation

1. Clone or download this repository
2. No additional installation required as the system uses built-in Python libraries

## Usage

### For Medical Officers

Run the medical officer interface:
```bash
python medical_officer_interface.py
```

This interface allows you to:
1. Add new patients
2. Update existing patient information
3. View patient records
4. Exit the system

### For Paramedics

Run the paramedic interface:
```bash
python paramedic_interface.py
```

This interface allows you to:
1. Quickly look up patient information using their phone number
2. View critical medical information including allergies and conditions
3. Access emergency contact information

## Security Notes

- The database is stored locally in `medical_records.db`
- No internet connection is required
- Access is controlled through separate interfaces for medical officers and paramedics

## Important Notes

- Always keep the database file secure and backed up
- Update patient information regularly during hospital visits
- Paramedics should verify patient identity before administering any treatment
- The system is designed for quick access to critical information in emergency situations 