import csv
import os

FILENAME = "students.csv"

def load_students():
    students = {}
    if os.path.exists(FILENAME):
        with open(FILENAME, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students[row['ID']] = {
                    'Name': row['Name'],
                    'Age': row['Age'],
                    'Grade': row['Grade']
                }
    return students

def save_students(students):
    with open(FILENAME, mode='w', newline='') as file:
        fieldnames = ['ID', 'Name', 'Age', 'Grade']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student_id, info in students.items():
            writer.writerow({
                'ID': student_id,
                'Name': info['Name'],
                'Age': info['Age'],
                'Grade': info['Grade']
            })
    print("Data successfully saved to CSV file!")

def main():
    students = load_students()
    
    # --- NEW LOGIN STEP FOR TEACHERS AND PARENTS ---
    print("=== WELCOME TO THE STUDENT MANAGEMENT SYSTEM ===")
    print("Identify your role to continue:")
    print("1. Teacher")
    print("2. Parent")
    
    role = input("Enter your role choice (1 or 2): ").strip()
    
    # If the user chooses 1, they log in as a Teacher with full access
    if role == '1':
        print("\nLogged in successfully as: TEACHER (Full Management Access)")
        while True:
            print("\n--- TEACHER MENU ---")
            print("1. Add Student Details")
            print("2. Update Student Records")
            print("3. Delete Student Records")
            print("4. Search Student by ID")
            print("5. Display All Students")
            print("6. Exit & Save")
            
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == '1':
                student_id = input("Enter Student ID: ").strip()
                if student_id in students:
                    print("Error: Student ID already exists.")
                else:
                    name = input("Enter Name: ").strip()
                    age = input("Enter Age: ").strip()
                    grade = input("Enter Grade: ").strip()
                    students[student_id] = {'Name': name, 'Age': age, 'Grade': grade}
                    print("Student added successfully!")
                    
            elif choice == '2':
                student_id = input("Enter Student ID to update: ").strip()
                if student_id in students:
                    print("Leave blank to keep the current value.")
                    name = input(f"Enter new Name ({students[student_id]['Name']}): ").strip()
                    age = input(f"Enter new Age ({students[student_id]['Age']}): ").strip()
                    grade = input(f"Enter new Grade ({students[student_id]['Grade']}): ").strip()
                    
                    if name: students[student_id]['Name'] = name
                    if age: students[student_id]['Age'] = age
                    if grade: students[student_id]['Grade'] = grade
                    print("Student details updated!")
                else:
                    print("Student ID not found.")
                    
            elif choice == '3':
                student_id = input("Enter Student ID to delete: ").strip()
                if student_id in students:
                    del students[student_id]
                    print("Student records deleted successfully.")
                else:
                    print("Student ID not found.")
                    
            elif choice == '4':
                student_id = input("Enter Student ID to search: ").strip()
                if student_id in students:
                    info = students[student_id]
                    print(f"\n[ID: {student_id}] Name: {info['Name']}, Age: {info['Age']}, Grade: {info['Grade']}")
                else:
                    print("Student ID not found.")
                    
            elif choice == '5':
                if not students:
                    print("No records found.")
                else:
                    print("\n--- All Student Records ---")
                    for student_id, info in students.items():
                        print(f"ID: {student_id} | Name: {info['Name']} | Age: {info['Age']} | Grade: {info['Grade']}")
                        
            elif choice == '6':
                save_students(students)
                print("Exiting application. Goodbye!")
                break
            else:
                print("Invalid option. Please choose between 1 and 6.")
                
    # If the user chooses 2, they log in as a Parent with read-only search access
    elif role == '2':
        print("\nLogged in successfully as: PARENT (View-Only Portal)")
        while True:
            print("\n--- PARENT MENU ---")
            print("1. Search Child Record by ID")
            print("2. Exit Portal")
            
            choice = input("Enter your choice (1-2): ").strip()
            
            if choice == '1':
                student_id = input("Enter your Child's Student ID to search: ").strip()
                if student_id in students:
                    info = students[student_id]
                    print(f"\n--- Child Progress Record ---")
                    print(f"ID: {student_id}\nName: {info['Name']}\nAge: {info['Age']}\nCurrent Grade: {info['Grade']}")
                else:
                    print("Student ID not found in system records. Please verify with administration.")
            elif choice == '2':
                print("Exiting Parent portal. Goodbye!")
                break
            else:
                print("Invalid option. Please choose 1 or 2.")
                
    else:
        print("Invalid role selection. Exiting program.")

if __name__ == '__main__':
    main()
