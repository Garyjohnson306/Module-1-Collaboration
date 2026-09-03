#Gary Johnson
#GPAapp
#Python app that qualifies students for honor roll/Dean's list

while True:
    last_name = input("Enter student's last name: ")

    if last_name == "ZZZ":
        break

    first_name = input("Enter student's first name: ")
    gpa = float(input("Please enter student's GPA: "))

    if gpa >= 3.5:
        print(first_name, "you made the Dean's List!")
    elif gpa >= 3.25:
        print(first_name, "you made the Honor Roll!")
    else:
        print("Your GPA is a", gpa)