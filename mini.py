students=[]

def add_student():
    name=input("Enter student name :")
    age=int(input("Enter age :"))
    marks=float(input("Enter marks"))

    student={
        "name":name,
        "age":age,
        "marks":marks
    }

    students.append(student)
    print("Student added successfully!")

def display_students():
    if len(students)==0:
        print("No student found")
    else:
        for student in students:
            print("Name",student["name"])
            print("Age",student["age"])
            print("Marks",student["marks"])
            print("---------------")     

def search_student():
    name=input("Enter student name to search :")

    for student in students:
        if student["name"].lower()==name.lower():
            print("Student found!")
            return
    print("Student not found")        

def delete_student():
    name=input("Enter student name to delete :")

    for student in students:
        if student["name"].lower()==name.lower():
            students.remove(student)
            print("Student deleted successfully!")
            return
    print("Student not found")

def main():
    while True:
        print("\n======STUDENT MANAGEMENT SYSTEM======")  
        print("1.Add student")
        print("2.Display student")
        print("3.Search student")
        print("4.Delete student")
        print("5.Exit")

        choice=int(input("Enter your choice :"))

        if choice==1:
            add_student()

        elif choice==2:
            display_students()

        elif choice==3:
            search_student() 

        elif choice==4:
            delete_student()

        elif choice==5:
            print("Thank you!")
            break

        else:
            print("Invalid choice")

main()                                         