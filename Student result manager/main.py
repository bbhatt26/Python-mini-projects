import json

FILE_NAME = "students.json" #file name

# load data when program start 
def load_students():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

student = load_students()

while True:
    print("\n-----------STUDENT MANAGER APP------------") 
    print("1. Add Student")
    print("2. View Students")
    print("3. Check Result")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Clear All")
    print("7. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        name = input ("Enter student name: ").strip().title()
        marks = int(input("Enter marks: "))
        student[name]= marks
        print(f"{name} Sucessfully Added!")
        
        # save after every add
        with open(FILE_NAME, "w") as f:
            json.dump(student, f)
        
    elif choice =="2":
        if not student:
            print("No student found!")
        else:
            for name, marks in student.items():
                print(name, ":", marks)
                
    elif choice == "3":
        name= input("Enter student name: ")
        
        if name in student:
            marks = student[name]
            
            if marks>=40:
                print("PASS")
            else:
                print("FAIL")
                
        else:
            print("Student Not Found !")
            
            
    elif choice == "4":
        name = input("Enter name to update: ").strip().title()
        if name in student:
            new_marks = int(input("Enter new marks: "))
            student[name] = new_marks
            print("Updated!")
            
    elif choice == "5":
        name = input("Enter student name to delete: ").strip().title()

        if name in student:
            del student[name] #delete from the dictionary
            #update the file aftwr deletion
            with open(FILE_NAME, "w") as f:
                json.dump(student, f)
            print(f"✅ {name} deleted successfully!")
        else:
            print("Student Not Found!")
    
    elif choice == "6":
        confirm = input("⚠️ All students will be deleted. Are you sure? y/n: ").lower()
        if confirm == "y":
            student.clear() # clear the dictionary
            with open(FILE_NAME, "w") as f:
                json.dump(student, f) # empty dictionary saved
            print("✅ All data cleared!")
        else:
            print("Cancelled")
        
    elif choice == "7":
        print("Exiting............")
        break
    
    else:
        print("Invalid choice!")
