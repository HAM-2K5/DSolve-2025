from medical_database import MedicalDatabase

def print_emergency_info(patient):
    if not patient:
        print("\n⚠️  NO PATIENT RECORD FOUND!")
        print("Please proceed with standard emergency protocols.")
        return
    
    print("\n=== EMERGENCY PATIENT INFORMATION ===")
    print(f"Name: {patient[1]}")
    print(f"Blood Type: {patient[4]}")
    print("\n⚠️  CRITICAL INFORMATION:")
    print(f"Allergies: {patient[5] if patient[5] else 'None'}")
    print(f"Medical Conditions: {patient[6] if patient[6] else 'None'}")
    print(f"Emergency Contact: {patient[7]}")
    print("\nLast Updated:", patient[8])
    print("===================================")

def main():
    db = MedicalDatabase()
    
    while True:
        print("\n=== Emergency Medical Information System ===")
        print("1. Look up patient by phone number")
        print("2. Exit")
        print("=========================================")
        
        choice = input("Enter your choice (1-2): ")
        
        if choice == "1":
            phone = input("\nEnter patient's phone number: ")
            patient = db.get_patient_by_phone(phone)
            print_emergency_info(patient)
            
        elif choice == "2":
            print("\nThank you for using the Emergency Medical Information System!")
            break
            
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main() 