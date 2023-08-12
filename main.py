import colorama
from colorama import Fore, Back, Style

colorama.init()

import re #regular expression module

from tabulate import tabulate #tabulate module


#accessing the student module from the student package

from student import Student

#students database
student_database = []

 #creating a welcome screen
def welcome_screen():
    
    option = int(input(Fore.LIGHTGREEN_EX + """***** Welcome to Student Management System *****
    1. Add Student
    2. View all Students
    3. Update Student info
    4. Delete Student info
    5. Search Student
    6. Exit app
    Please select option: """))
    
    


#creating a function to determine user option
    user_option(option)


def user_option(option):
    if option == 1:
        add_student()
    elif option == 2:
        view_all_students()
    elif option == 3:
        update_student()
    elif option == 4:
        delete_student()
    elif option == 5:
        search_student()
    else:
        print(Fore.RED + Style.BRIGHT + "Invalid option")



    welcome_screen()
    



#Define a regular expression pattern for a valid name with only alphabetic characters
def valid_name(name):
    pattern = r'^[a-zA-Z\s\-]+$'
    return re.match(pattern, name)


#function to handle adding a new student
def add_student():
        print(Fore.RED + Style.BRIGHT + "***** Adding a new student *****")
        student_id = input(Fore.BLUE + Style.BRIGHT + "Enter student ID: ")
         
        while True:
           first_name = input(Fore.BLUE + Style.BRIGHT + "Enter first name: ")
           if valid_name(first_name):
            break
           print(Fore.RED + Style.BRIGHT + "Invalid first name")

        while True:   
            last_name = input(Fore.BLUE + Style.BRIGHT + "Enter last name: ")
            if valid_name(last_name):
                break
            print(Fore.RED + Style.BRIGHT + "Invalid last name")

        age = int(input(Fore.BLUE + Style.BRIGHT + "Enter age: "))
        gender = input(Fore.BLUE + Style.BRIGHT + "Enter gender: ")


        #create instance of the class, which will make us get an object
        student = Student(student_id, first_name, last_name, age, gender)
        
        #save student into database
        student_database.append(student)
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Student added successfully")

#function to view all the students
def view_all_students():
   
    headers = ["Student_ID", "First Name", "Last Name", "Age", "Gender"]
    rows = [[student.student_id, student.first_name, student.last_name, student.age, student.gender]
            for student in student_database]
    table = tabulate(rows, headers, tablefmt="fancy_grid")
    print(table)

#function to check if student is in database
def is_student_in_database(student_id):
    for student in student_database:
        if student.student_id == student_id:
            return True
    return False
    
#function to update student info
def update_student():
    print(Fore.RED + Style.BRIGHT + "***** Updating student info *****")
    student_id = input(Fore.BLUE + Style.BRIGHT + "Enter student ID: ")
    
    # Print the entered student ID and student IDs in the database
    print("Entered student ID:", student_id)
    print("Student IDs in the database:", [student.student_id for student in student_database])
    
    if is_student_in_database(student_id):
                ask_update = int(input(Fore.BLUE + Style.BRIGHT + """What would you like to update?
            1. First name
            2. Last name
            3. Age
            4. Gender
            5. Exit
            Please select option: """))
                                    
                if ask_update == 1:
                    first_name = input(Fore.BLUE + Style.BRIGHT + "Enter first name: ")
                    for student in student_database:
                        if student.student_id == student_id:
                            student.first_name = first_name
                            print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "First name updated successfully")
                            break
                elif ask_update == 2:
                    last_name = input(Fore.BLUE + Style.BRIGHT + "Enter last name: ")
                    for student in student_database:
                        if student.student_id == student_id:
                            student.last_name = last_name
                            print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Last name updated successfully")
                            break
                elif ask_update == 3:
                    age = int(input(Fore.BLUE + Style.BRIGHT + "Enter age: "))
                    for student in student_database:
                        if student.student_id == student_id:
                            student.age = age
                            print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Age updated successfully")
                            break
                elif ask_update == 4:
                    gender = input(Fore.BLUE + Style.BRIGHT + "Enter gender: ")
                    for student in student_database:
                        if student.student_id == student_id:
                            student.gender = gender
                            print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Gender updated successfully")
                            break
                
                elif ask_update == 5:
                            print(Fore.RED + Style.BRIGHT + "Exiting update mode")
                            exit() #exit update loop
                else:
                    print(Fore.RED + Style.BRIGHT + "Invalid option")
                    
    else:
                print(Fore.RED + Style.BRIGHT + "Student not found in database")



#function to delete student info
def delete_student():
     print(Fore.RED + Style.BRIGHT + "***** Deleting student info *****")
     student_id = input(Fore.BLUE + Style.BRIGHT + "Enter student ID: ")
     
     # Print the entered student ID and student IDs in the database
     print("Entered student ID:", student_id)
     print("Student IDs in the database:", [student.student_id for student in student_database])

     if is_student_in_database(student_id):
          for student in student_database:
              if student.student_id == student_id:
                  student_database.remove(student)
                  confirm = input(Fore.RED + Style.BRIGHT + "Are you sure you want to delete student? (y/n): ")
                  if confirm == "y":
                       print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Student deleted successfully")
                       break
              else:
                  print(Fore.RED + Style.BRIGHT + "Student not found in database")
                  exit()

# Function to search for a student by ID and print the result in a table
def search_student():
    print(Fore.RED + Style.BRIGHT + "***** Search Student *****")
    student_id = input(Fore.BLUE + Style.BRIGHT + "Enter student ID: ")

    found_student = None
    for student in student_database:
        if student.student_id == student_id:
            found_student = student
            break

    if found_student:
        headers = ["Student_ID", "First Name", "Last Name", "Age", "Gender"]
        student_data = [[found_student.student_id, found_student.first_name, found_student.last_name,
                         found_student.age, found_student.gender]]

        table = tabulate(student_data, headers, tablefmt="fancy_grid")
        print(table)
    else:
        print(Fore.RED + Style.BRIGHT + f"Student with ID {student_id} not found")


     
      
     
     

     
     
welcome_screen()


        