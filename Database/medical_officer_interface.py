from medical_database import MedicalDatabase
import json

def print_menu():
    print("\n=== Medical Records Management System ===")
    print("1. Add new patient")
    print("2. Update patient information")
    print("3. View patient information")
    print("4. Exit")
    print("=====================================")

def get_patient_info():
    name = input("Enter patient name: ")
    phone = input("Enter phone number: ")
    dob = input("Enter date of birth (YYYY-MM-DD): ")
    blood_type = input("Enter blood type: ")
    
    print("\nEnter allergies (comma-separated, press Enter if none):")
    allergies_input = input().strip()
    allergies = [a.strip() for a in allergies_input.split(",")] if allergies_input else None
    
    print("\nEnter medical conditions (comma-separated, press Enter if none):")
    conditions_input = input().strip()
    conditions = [c.strip() for c in conditions_input.split(",")] if conditions_input else None
    
    emergency_contact = input("\nEnter emergency contact number: ")
    
    return {
        "name": name,
        "phone_number": phone,
        "date_of_birth": dob,
        "blood_type": blood_type,
        "allergies": allergies,
        "medical_conditions": conditions,
        "emergency_contact": emergency_contact
    }

def main():
    db = MedicalDatabase()
    
    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            print("\n=== Adding New Patient ===")
            patient_info = get_patient_info()
            patient_id = db.add_patient(**patient_info)
            print(f"\nPatient added successfully! Patient ID: {patient_id}")
            
        elif choice == "2":
            print("\n=== Updating Patient Information ===")
            phone = input("Enter patient's phone number: ")
            patient = db.get_patient_by_phone(phone)
            
            if patient:
                print("\nCurrent patient information:")
                print(f"Name: {patient[1]}")
                print(f"Phone: {patient[2]}")
                print(f"Blood Type: {patient[4]}")
                print(f"Allergies: {patient[5]}")
                print(f"Medical Conditions: {patient[6]}")
                
                print("\nEnter new information (press Enter to skip):")
                new_info = {}
                
                new_name = input("New name: ").strip()
                if new_name: new_info["name"] = new_name
                
                new_phone = input("New phone: ").strip()
                if new_phone: new_info["phone_number"] = new_phone
                
                new_blood = input("New blood type: ").strip()
                if new_blood: new_info["blood_type"] = new_blood
                
                new_allergies = input("New allergies (comma-separated): ").strip()
                if new_allergies: new_info["allergies"] = [a.strip() for a in new_allergies.split(",")]
                
                new_conditions = input("New medical conditions (comma-separated): ").strip()
                if new_conditions: new_info["medical_conditions"] = [c.strip() for c in new_conditions.split(",")]
                
                new_emergency = input("New emergency contact: ").strip()
                if new_emergency: new_info["emergency_contact"] = new_emergency
                
                if new_info:
                    db.update_patient(patient[0], **new_info)
                    print("\nPatient information updated successfully!")
                else:
                    print("\nNo changes made.")
            else:
                print("\nPatient not found!")
                
        elif choice == "3":
            print("\n=== View Patient Information ===")
            phone = input("Enter patient's phone number: ")
            patient = db.get_patient_by_phone(phone)
            
            if patient:
                print("\nPatient Information:")
                print(f"ID: {patient[0]}")
                print(f"Name: {patient[1]}")
                print(f"Phone: {patient[2]}")
                print(f"Date of Birth: {patient[3]}")
                print(f"Blood Type: {patient[4]}")
                print(f"Allergies: {patient[5]}")
                print(f"Medical Conditions: {patient[6]}")
                print(f"Emergency Contact: {patient[7]}")
                print(f"Last Updated: {patient[8]}")
            else:
                print("\nPatient not found!")
                
        elif choice == "4":
            print("\nThank you for using the Medical Records Management System!")
            break
            
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main() 