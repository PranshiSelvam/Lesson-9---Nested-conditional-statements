medical_cause = input("Do you have any medical cause (Yes or No): ")
attendance = int(input("What is your attendance in percentage: "))
if medical_cause == "Yes":
    print("You are allowed for the examination")
else:
    if attendance>=75:
        print("You are allowed for the examination")
    else:
        print("You are not allowed for the examination")

