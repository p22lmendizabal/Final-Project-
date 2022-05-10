# author: LM (AMDG) 5/3/22
# file manager for student hours
# we ask user to input student's information




def student_info():
    name = input("Please enter the student's name: ")
    address = input("Please enter the student's address:")
    phone = input("Please enter Parent's phone number:")
    with open('students_service_hours.txt', 'w') as infile:
        infile.write('Name: {0}'.format(name))
        infile.write('\n')
        infile.write('Address: {0}'.format(address))
        infile.write('\n')
        infile.write("Parent's Phone Number: {0}".format(phone))
        infile.write("\n")
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

student_info()
repeat_student_info()

