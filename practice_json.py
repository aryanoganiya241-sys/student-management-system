import json

def load_data():
    try:
        with open("student.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
    
def save_students(students):
    with open("student.json","w") as file:
        json.dump(students,file)

def show():
    if not students:
        print("no student found")
        return
    for student in students:
        print(f"name:{student["name"]}")
        print(f"roll:{student["roll"]}")
        print(f"marks:{student["marks"]}")
        print("-"*20)
students=load_data()
save_students(students)
#show(students)

def add_students():
    students=load_data()
    name=input("enter name of student to add:")
    roll=int(input("enter roll number to add student:"))
    marks=int(input("enter marks of student:"))
    new_student={
        "name":name,
        "roll":roll,
        "marks":marks
    }
    students.append(new_student)
#students=load_data()
    save_students(students)
    print("added successfully")
#add_students(students)

def search_students():
    students=load_data()
    search=int(input("enter roll number to search:"))
    found=False
    for student in students:
        if search==student["roll"]:
            found=True
            print(f"name:{student["name"]} roll:{student["roll"]}")
    if found is False:
        print("invalid roll number")
#search_students(students)

def delet_students():
    students=load_data()
    found=False
    delet=int(input("enter roll number to delet:"))
    for student in students:
        if delet==student["roll"]:
            found=True
            students.remove(student)
            print("deleted succussefully")
        save_students(students)
    if found is False:
        print("invalid roll number")
#delet_students(students)

def update_students():
    students=load_data()
    found=False
    up=int(input("enter roll number of student  to update:"))
    for student in students:
        if up==student["roll"]:
            found=True
            new_name=input("enter new name name:")
            new_marks=int(input("enter new marks of students:"))
            student["name"]=new_name
            student["marks"]=new_marks
        save_students(students)
        print("updated successfully")
        break
        
    if found is False:
        print("invalid roll number")
#update_students(students)

def total_student():
    students=load_data()
    total=len(students)
    print("total students =",total)
#total_student(students)

def average_student():
    students=load_data()
    total=len(students)
    sum=0
    for student in students:
        sum=sum+student["marks"]
        avg=sum/total
    print("average marks of students is:",avg)
#average_student(students)

def topper_student():
    students=load_data()
    topper=students[0]
    for student in students:
        if student["marks"]>topper["marks"]:
            topper=student
    print("topper details")
    print("="*50)
    print("\n"f"Name  :{topper["name"]}")
    print(f"roll  :{topper["roll"]}")
    print(f"marks :{topper["marks"]}")
#topper_student(students)

def sorting_by_name():
    students=load_data()
    for i in range(len(students)):
        for j in range(i+1,len(students)):
            if students[j]["name"]>students[i]["name"]:
                students[i],students[j]=students[j],students[i]
    for student in students:
        print(f"{student["name"]}\t\t{student["marks"]}\t\t{student["roll"]}")
#sorting_by_name(students)

def sorting_by_marks():
    students=load_data()
    for i in range(len(students)):
        for j in range(i+1,len(students)):
            if students[j]["marks"]>students[i]["marks"]:
                students[i],students[j]=students[j],students[i]
    for student in students:
        print(f"{student["name"]}\t\t{student["marks"]}\t\t{student["roll"]}")
#sorting_by_marks(students)

def grade_system():
    students=load_data()
    print("\nName\t\tMarks\tGrade")
    print("-"*30)
    for student in students:
        if student["marks"]>=90:
            grade="A+"
        elif student["marks"]>=80:
            grade="A"
        elif student["marks"]>=70:
            grade="B"
        elif student["marks"]>=60:
            grade="C"
        elif student["marks"]>=50:
            grade="D"
        elif student["marks"]>=40:
            grade="E"
        else:
            print("fail")
        print(student["name"],"\t",student["marks"],"\t",grade)



def display_menu():
    print("="*50)
    print("          student managment sysytem")
    print("="*50)
    print("\n")
    print("1.show students")
    print("2.add students")
    print("3.search students")
    print("4.delet students")
    print("5.update students")
    print("6.total students")
    print("7.average marks of students")
    print("8.topper student")
    print("9.soring")
    print("10.garde of student")
    print("11.exit")
    choice=int(input("\nenter your choice"))
    print("choice",choice)
    print("\n")
    return choice
while True:
    choice=display_menu()
    if choice==1:
        show()
    elif choice==2:
        add_students()
    elif choice==3:
        search_students()
    elif choice==4:
        delet_students()
    elif choice==5:
        update_students()
    elif choice==6:
        total_student()
    elif choice==7:
        average_student()
    elif choice==8:
        topper_student()
    elif choice==9:
        print("1.sort by name")
        print("2.sort by marks")
        op=int(input("enter type of sorting"))
        if op==1:
            sorting_by_name()
        elif op==2:
            sorting_by_marks()
    elif choice==10:
        grade_system()
    elif choice==11:
        print("exit")
        break
    else:
        print("invalid choice")