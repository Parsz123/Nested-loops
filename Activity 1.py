reason = input("Do you have a medical reason - Y for yes, N for no ")
attendance = int(input("What is your attendance rate?"))
if reason == "Y" or reason == "y":
    print("You are allowed")
else:
    if attendance >= 75:
        print("You are allowed")
    else:
        print("You are not allowed")