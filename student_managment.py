# Import the built-in csv module to read and write spreadsheet-like CSV files
import csv
# Import the os module to check if files exist on your computer
import os

# Define the name of the file where student data will be saved
FILENAME = "students.csv"

# Define a function to load student records from the CSV file into our program
def load_students():
    # Start with an empty dictionary to store student data while the program runs
    students = {}
    # Check if the CSV file already exists on your computer
    if os.path.exists(FILENAME):
        # Open the CSV file in read mode ('r') safely using a context managerr
        with open(FILENAME, mode='r', newline='') as file:
            # Create a reader object that interprets rows as dictionaries using the header row
            reader = csv.DictReader(file)
            # Loop through each row found inside the CSV file
            for row in reader:
                # Use the student ID as a key to store their Name, Age, and Grade details
                students[row['ID']] = {
                    'Name': row['Name'],
                    'Age': row['Age'],
                    'Grade': row['Grade']
                }
    # Return the dictionary filled with student data back to the main program
    return students

# Define a function to save our current student data back into the CSV file
def save_students(students):
    # Open the CSV file in write mode ('w') which overwrites or creates the file
    with open(FILENAME, mode='w', newline='') as file:
        # Define the exact column headers we want at the top of our CSV file
        fieldnames = ['ID', 'Name', 'Age', 'Grade']
        # Create a writer object configured to write data matching our headers
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        # Write the column headers as the very first row in the CSV file
        writer.writeheader()
        # Loop through every student ID and their associated info dictionary
        for student_id, info in students.items():
            # Write a new row into the CSV file for the current student
            writer.writerow({
                'ID': student_id,
                'Name': info['Name'],
                'Age': info['Age'],
                'Grade': info['Grade']
            })
    # Print a success message letting the user know the data is safely stored
    print("Data successfully saved to CSV file!")

# Define the main function where the interactive menu logic lives
def main():
    # Load any existing student data from the CSV file into a working variable
    students = load_students()
    
    # Start an infinite loop to keep the menu running until the user decides to exit
    while True:
        # Print a blank line for clean spacing in the terminal
        print("\n=== STUDENT MANAGEMENT SYSTEM ===")
        # Print the option to add a new student
        print("1. Add Student Details")
        # Print the option to update an existing student
        print("2. Update Student Records")
        # Print the option to delete a student record
        print("3. Delete Student Records")
        # Print the option to search for a specific student using their ID
        print("4. Search Student by ID")
        # Print the option to show a list of all students currently saved
        print("5. Display All Students")
        # Print the option to save all work and close the program
        print("6. Exit & Save")
        
        # Ask the user to type a number choice and remove any accidental spaces
        choice = input("Enter your choice (1-6): ").strip()
        
        # Check if the user selected option 1 (Add Student)
        if choice == '1':
            # Ask the user to input a unique ID number for the student
            student_id = input("Enter Student ID: ").strip()
            # Check if this specific ID already belongs to another student
            if student_id in students:
                # Print an error message because IDs must be unique
                print("Error: Student ID already exists.")
            # If the ID is completely new and available
            else:
                # Ask the user to enter the student's full name
                name = input("Enter Name: ").strip()
                # Ask the user to enter the student's age
                age = input("Enter Age: ").strip()
                # Ask the user to enter the student's class grade
                grade = input("Enter Grade: ").strip()
                # Add the new student's info into our memory dictionary under their unique ID
                students[student_id] = {'Name': name, 'Age': age, 'Grade': grade}
                # Print a success confirmation message to the user
                print("Student added successfully!")
                
        # Check if the user selected option 2 (Update Student)
        elif choice == '2':
            # Ask the user for the ID of the student they want to change
            student_id = input("Enter Student ID to update: ").strip()
            # Check if that student ID exists in our records
            if student_id in students:
                # Tell the user they can press Enter to skip any details they don't want to change
                print("Leave blank to keep the current value.")
                # Prompt for a new name while displaying the current saved name
                name = input(f"Enter new Name ({students[student_id]['Name']}): ").strip()
                # Prompt for a new age while displaying the current saved age
                age = input(f"Enter new Age ({students[student_id]['Age']}): ").strip()
                # Prompt for a new grade while displaying the current saved grade
                grade = input(f"Enter new Grade ({students[student_id]['Grade']}): ").strip()
                
                # If the user typed a new name, update it in our records
                if name: students[student_id]['Name'] = name
                # If the user typed a new age, update it in our records
                if age: students[student_id]['Age'] = age
                # If the user typed a new grade, update it in our records
                if grade: students[student_id]['Grade'] = grade
                # Print a confirmation that the details were updated successfully
                print("Student details updated!")
            # If the ID typed by the user does not exist
            else:
                # Print an error message letting them know it wasn't found
                print("Student ID not found.")
                
        # Check if the user selected option 3 (Delete Student)
        elif choice == '3':
            # Ask the user for the ID of the student they want to remove
            student_id = input("Enter Student ID to delete: ").strip()
            # Check if that student ID exists in our records
            if student_id in students:
                # Remove the student's data entirely from our working dictionary
                del students[student_id]
                # Print a confirmation that the record was wiped out
                print("Student records deleted successfully.")
            # If the ID typed by the user does not exist
            else:
                # Print an error message letting them know it wasn't found
                print("Student ID not found.")
                
        # Check if the user selected option 4 (Search Student by ID)
        elif choice == '4':
            # Ask the user for the ID of the student they are looking for
            student_id = input("Enter Student ID to search: ").strip()
            # Check if that student ID exists in our records
            if student_id in students:
                # Pull out the target student's info dictionary for quick reading
                info = students[student_id]
                # Print the student's ID, Name, Age, and Grade clearly on the screen
                print(f"\n[ID: {student_id}] Name: {info['Name']}, Age: {info['Age']}, Grade: {info['Grade']}")
            # If the ID typed by the user does not exist
            else:
                # Print an error message letting them know it wasn't found
                print("Student ID not found.")
                
        # Check if the user selected option 5 (Display All Students)
        elif choice == '5':
            # Check if our student dictionary is completely empty
            if not students:
                # Inform the user that there is nothing to show yet
                print("No records found.")
            # If there is at least one student record available
            else:
                # Print a clean section header for the list
                print("\n--- All Student Records ---")
                # Loop through every single student in our memory dictionary one by one
                for student_id, info in students.items():
                    # Print out all details for the current student in a clean row format
                    print(f"ID: {student_id} | Name: {info['Name']} | Age: {info['Age']} | Grade: {info['Grade']}")
                    
        # Check if the user selected option 6 (Exit & Save)
        elif choice == '6':
            # Call our save function to write everything permanently into the CSV file
            save_students(students)
            # Print a closing message to the user
            print("Exiting application. Goodbye!")
            # Break out of the infinite while loop to close the program
            break
        # If the user typed anything other than a number from 1 to 6
        else:
            # Print an error message telling them to select a valid menu choice
            print("Invalid option. Please choose between 1 and 6.")

# Check if this script is being run directly by Python rather than being imported elsewhere
if __name__ == '__main__':
    # Call the main function to start p the entire system application
    main()
