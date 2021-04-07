import studeninfo

print("1.Teacher")
print("2.Student")
user=input("Enter your Choice:=")
if('Teacher'==user):
    studeninfo.teacher_info()
elif('Student'==user):
    studeninfo.student_info()
else:
    print("You Choice is Invalid ????....Please check it..")