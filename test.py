# Asks user if they want to open the file to access hours 

startofprogram = input("Are you trying to access your student's hours file? if Yes enter Y if no enter N: ").capitalize
if startofprogram != 'Y' or 'N':
    print("please enter a 'Y' or 'N'.")
elif startofprogram == "N":
    print("Have a good day!")
        
#if this true then program continues
elif startofprogram == 'Y':
    # this is where we will call the funtion
    print("This is a place holder")
        
