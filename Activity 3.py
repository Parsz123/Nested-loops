choice1 = int(input("Choose your ride - 1 for bike and 2 for car: "))

if choice1 == 1:
    choice2 = int(input("Do you want a scooter or a scooty - 1 for scooter, 2 for scooty: "))
    if choice2 == 1:
        print("You will have a scooter")
    elif choice2 == 2:
        print("You will have a scooty")
    else:
        print("Invalid choice for bike type")
elif choice1 == 2:
    choice3 = int(input("What car do you want to have - 1 for BMW, 2 for XUV: "))
    if choice3 == 1:
        print("You will have a BMW")
    elif choice3 == 2:
        print("You will have an XUV")
    else:
        print("Invalid choice for car type")
else:
    print("Invalid choice for ride")
