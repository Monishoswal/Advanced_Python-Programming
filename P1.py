def student(roll_no , name) :
    print(roll_no , name)
student(10,"Xyz")

def subject(*sub) :
    print(sub)
subject("Maths","Python")

def stud(roll_no , name, clas="xyz"):
    print(roll_no , name , clas )
stud(10,"xyz")
stud(10,"xyz","Sy3")

def stu(roll_no , name):
    print(roll_no , name )
stu(name = "abc" , roll_no = "10")
