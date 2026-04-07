"""
Student Management Syatem
"""
from utils import addStudent , viewAllStudent , deleteStudent

student = dict()
while True:
    print("\n\t ***** STUDENT MANAGEMENT SYSTEM ***** n")
    print("\n\t\t1. Add Student")
    print("\t\t2. View All Students")
    print("\t\t3. Delete A Student")
    print("\t\t0. Exit")
    ch = int (input ("nt tEnter Your Choice : ") )
    if ch == 0:
        print ("n\tBYE-BYE ADMIN! ")
        break
    elif ch == 1:
        student = addStudent (student)
        print ("n\tStudent Added Successfully!")
        input ("\tPress Enter To Continue ... ")
    elif ch == 2:
        viewAllStudent (student)
        input ("tPress Enter To Continue ... ")
    elif ch == 3:
        student = deleteStudent (student)

    
