"""
Utilities for Student Management System
"""
def addStudent (student) :
    sid = input ("\n\tEnter Student ID : ")
    sname = input ("\tEnter Student Name : ")
    sadd = input ("\tEnter Student Address : ")
    smob = input ("\tEnter Student Mobile : ")
    student. update ({sid: [sname, sadd, smob] } )
    return student

def viewAllStudent (student) :
    for sid, details in student.items () :
        print("\n\tStudent ID : " , sid)
        print("\tStudent Name : ", details [0])
        print("\tStudent Address : ", details [1])
        print("\tStudent Mobile : ", details [2])
        print ("\t **************** ")
    return None

def deleteStudent (student) :
    sid = input ("n\tEnter Student ID To Delete : ")
    detail = student.get (sid)
    if detail != None:
        print ("n\tStudent Name :", detail [0])
    del student [sid]
        print ("tDeleted Successfully!")
    else:
        print("n\tStudent Not Found On This ID")
        return student

I
