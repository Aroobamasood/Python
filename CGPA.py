# python program to calculate cgpa of a student with 5 subject marks.

Name = input("Enter student name: \n")
Reg_no = input("Enter student Registration number: \n")

for i in range(5):
    choice = input("Do you want to enter subject marks for student (Y/N)?  \n")
    choice = choice[0]

    if choice.upper() == 'Y':
        print("1.Enter subject marks (Theory only)")
        print("2.Enter subject marks(Theory and lab)")
        option = input("Enter your choice: \n")

        if option == '1':
            Subject_name = input("Enter Subject Name: \n")
            Subject_marks = int(input("Enter Subject Marks: \n"))
            credit_hours = int(input("Enter credit hours:  \n"))

        elif option == '2':
            Subject_name = input("Enter Subject Name: \n")
            Subject_th_marks = int(input("Enter Subject Theory marks: \n"))
            Subject_lab_marks = int(input("Enter Subject Lab marks: \n"))
            credit_hours = int(input("Enter credit hours:  \n"))

    elif choice.upper() == 'N':
        print("program terminated")
        break
Total_Grade_Points = ((Subject_th_marks+Subject_lab_marks)*credit_hours)\
                     + ((Subject_th_marks+Subject_lab_marks)*credit_hours) + \
                     (Subject_marks*credit_hours)+(Subject_marks*credit_hours)+(Subject_marks*credit_hours)


print("Name of student: ", Name)
print("Registration number: ", Reg_no)
print("Total Grade points are: ", Total_Grade_Points)

CGPA = Total_Grade_Points / 17

if CGPA >= 90:
    print("CGPA is 4.0")
    print("You have Passed.")
elif 80 <= CGPA <= 89:
    print("CGPA is 3.0")
    print("You have Passed.")
elif 70 <= CGPA <= 79:
    print("CGPA is 2.5")
    print("You have Passed.")
elif 60 <= CGPA <= 69:
    print("CGPA is 2.0")
    print("You have Passed.")
elif 50 <= CGPA <= 59:
    print("CGPA is 1.5")
    print("You have Passed.")
else:
    print("Your CGPA is below 50.")
    print("You have failed!")