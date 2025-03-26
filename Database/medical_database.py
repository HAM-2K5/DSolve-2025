import sqlite3
from datetime import datetime
import json

class MedicalDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('medical_records.db')
        self.create_tables()
    
    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            date_of_birth TEXT,
            blood_type TEXT,
            allergies TEXT,
            medical_conditions TEXT,
            emergency_contact TEXT,
            last_updated TIMESTAMP
        )
        ''')
        self.conn.commit()
    
    def add_patient(self, name, phone_number, date_of_birth=None, blood_type=None, 
                   allergies=None, medical_conditions=None, emergency_contact=None):
        cursor = self.conn.cursor()
        cursor.execute('''
        INSERT INTO patients (name, phone_number, date_of_birth, blood_type, 
                            allergies, medical_conditions, emergency_contact, last_updated)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, phone_number, date_of_birth, blood_type, 
              json.dumps(allergies) if allergies else None,
              json.dumps(medical_conditions) if medical_conditions else None,
              emergency_contact, datetime.now()))
        self.conn.commit()
        return cursor.lastrowid
    
    def update_patient(self, patient_id, **kwargs):
        cursor = self.conn.cursor()
        update_fields = []
        values = []
        
        for key, value in kwargs.items():
            if key in ['allergies', 'medical_conditions']:
                value = json.dumps(value) if value else None
            update_fields.append(f"{key} = ?")
            values.append(value)
        
        values.append(datetime.now())
        values.append(patient_id)
        
        query = f'''
        UPDATE patients 
        SET {', '.join(update_fields)}, last_updated = ?
        WHERE id = ?
        '''
        cursor.execute(query, values)
        self.conn.commit()
    
    def get_patient_by_phone(self, phone_number):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM patients WHERE phone_number = ?', (phone_number,))
        patient = cursor.fetchone()
        
        if patient:
            # Convert JSON strings back to lists
            patient = list(patient)
            patient[5] = json.loads(patient[5]) if patient[5] else None  # allergies
            patient[6] = json.loads(patient[6]) if patient[6] else None  # medical_conditions
            return patient
        return None
    
    def get_patient_by_id(self, patient_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM patients WHERE id = ?', (patient_id,))
        patient = cursor.fetchone()
        
        if patient:
            # Convert JSON strings back to lists
            patient = list(patient)
            patient[5] = json.loads(patient[5]) if patient[5] else None  # allergies
            patient[6] = json.loads(patient[6]) if patient[6] else None  # medical_conditions
            return patient
        return None

# Example usage
if __name__ == "__main__":
    db = MedicalDatabase()
    
    # Example: Adding a new patient
    patient_id = db.add_patient(
        name="John Doe",
        phone_number="1234567890",
        date_of_birth="1990-01-01",
        blood_type="O+",
        allergies=["Penicillin", "Aspirin"],
        medical_conditions=["Asthma", "Hypertension"],
        emergency_contact="9876543210"
    )
    
    # Example: Updating patient information
    db.update_patient(
        patient_id,
        allergies=["Penicillin", "Aspirin", "Ibuprofen"],
        medical_conditions=["Asthma", "Hypertension", "Diabetes"]
    )
    
    # Example: Retrieving patient information
    patient = db.get_patient_by_phone("1234567890")
    if patient:
        print(f"Patient found: {patient}")
    else:
        print("Patient not found") 