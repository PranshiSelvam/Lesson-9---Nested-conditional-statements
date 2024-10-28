print("Which ride would like to choose: \n")
print("1. Car \n")
print("2. Bike \n")
choice = int(input("Please enter the number of the vehicle you have chosen: "))
if choice == 1:
    print("You have chosen a car. Which car would you choose? \n")
    print("1. Sedan \n 2. XUV \n 3. Sports car \n")
    choice2 = int(input("Please enter the number of the car: "))
    if choice2 == 1:
        print("You have chosen Sedan.")
    elif choice21 == 2:
        print("You have chosen XUV. ")
    elif choice2 == 3:
        print("You have choen Sports car")
    else:
        print("Please enter a valid input")
elif choice == 2:
    print("You have chosen a bike. Which bike would you like to choose? \n")
    print("1. Scooty \n 2. Scooter \n 3. Sports bike")
    choice3 = int(input("Enter the number of choice you have chosen: "))
    if choice3 == 1:
        print("You have chosen Scooty")
    elif choice3 == 2:
        print("You have chosen Scooter")
    elif choice3 == 3:
        print("You have chosen Sports Bike")
    else:
        print("Invalid input")
else:
    print("Invalid input")
