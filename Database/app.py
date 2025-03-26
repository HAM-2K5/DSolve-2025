from flask import Flask, render_template, request, jsonify
from medical_database import MedicalDatabase
import json

app = Flask(__name__)
db = MedicalDatabase()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/medical-officer')
def medical_officer():
    return render_template('medical_officer.html')

@app.route('/paramedic')
def paramedic():
    return render_template('paramedic.html')

# API endpoints
@app.route('/api/patient', methods=['POST'])
def add_patient():
    data = request.json
    print(data)
    db = MedicalDatabase()
    try:
        patient_id = db.add_patient(
            name=data['name'],
            phone_number=data['phone_number'],
            date_of_birth=data.get('date_of_birth'),
            blood_type=data.get('blood_type'),
            allergies=data.get('allergies'),
            medical_conditions=data.get('medical_conditions'),
            emergency_contact=data.get('emergency_contact')
        )
        return jsonify({'success': True, 'patient_id': patient_id})
    except Exception as e:
        print(e)
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/api/patient/<int:patient_id>', methods=['PUT'])
def update_patient(patient_id):
    db = MedicalDatabase()
    data = request.json
    try:
        db.update_patient(patient_id, **data)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/api/patient/phone/<phone_number>', methods=['GET'])
def get_patient_by_phone(phone_number):
    db = MedicalDatabase()
    data = request.json
    print(data)
    try:
        patient = db.get_patient_by_phone(phone_number)
        print(patient)
        if patient:
            return jsonify({
                'success': True,
                'patient': {
                    'id': patient[0],
                    'name': patient[1],
                    'phone_number': patient[2],
                    'date_of_birth': patient[3],
                    'blood_type': patient[4],
                    'allergies': patient[5],
                    'medical_conditions': patient[6],
                    'emergency_contact': patient[7],
                    'last_updated': patient[8]
                }
            })
        return jsonify({'success': False, 'error': 'Patient not found'}), 404
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True) 