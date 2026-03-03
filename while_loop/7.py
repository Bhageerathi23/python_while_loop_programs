#
marks = 0

while marks != -1:
    marks = int(input("Enter marks (-1 to stop): "))

    if marks == -1:
        print("Program Ended")
    elif marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 50:
        print("Grade: C")
    else:
        print("Grade: Fail")


#
while True:
    marks = int(input("Enter marks (-1 to stop): "))

    if marks == -1:
        print("Program Ended")
        break
    elif marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 50:
        print("Grade: C")
    else:
        print("Grade: Fail")