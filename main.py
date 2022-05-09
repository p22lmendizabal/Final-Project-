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
        anotherstudent = input("Will you be adding another student? Enter 'Y' if yes or 'N' if no: ").capitalize()
        if anotherstudent == 'Y':
            student_info()
        elif anotherstudent == 'N':
            print("Thank you. Have a good day.")
            break
        elif anotherstudent != 'Y' or 'X':
            print("Enter a 'Y' or 'N'")
            continue
        return
with open('students service hours.txt', 'r+') as infile:
    infile.write(name)
    infile.write('\n')
    infile.write(address)
student_info()
repeat_student_info()

