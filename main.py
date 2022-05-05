# author: LM (AMDG) 5/3/22
# file manager for student hours
# we ask user to input student's information


def student_info():
    name = input("Please enter the student's name: ")
    address = input("Please enter the student's address:")
    phone = input("Please enter Parent's phone number:")
    return name, address, phone


def repeat_student_info():
    while True:
        anotherstudent = input("Will you be adding another student? Enter 'Y' if yes or 'N' if no: ").capitalize
        if anotherstudent == 'Y':
            student_info()
        elif anotherstudent == 'N':
            break
        elif anotherstudent != 'Y' or 'X':
            repeat_student_info()
while True:
    student_info()
    repeat_student_info()

#Asks user if they want to open the file to access hours 
while True:
    startofprogram = input("Are you trying to access your student's hours file? if Yes enter Y if no enter N: ").capitalize()
    if startofprogram != 'Y' or 'N':
        print("please enter a 'Y' or 'N'. ")
    elif startofprogram == "N":
        print("Have a good day!")
        break
    #if this true then program continues
    elif startofprogram == 'Y':
        # this is where we will call the funtion
        print("This is a place holder")
