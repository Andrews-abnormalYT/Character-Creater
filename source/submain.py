print("Create your charater")
name = input("What is your charater called?")
age = input("What is your charater's age?")
strengths = input("What is your charater's Strength")
weaknesses = input("What is your charaters's Weaknesses")
print("Your charater's name is", name)
print("Your charater is", age, "years old")
print("Strengths:", strengths)
print("Weaknesses:", weaknesses)
print(name, "says, 'Thanks for creating me!'")

print("How was the charater?")
mood = input()
if mood == "Good":
    print("Great, your charater is good")
    right = input("Is that right?")
    if right == "Yes":
        print("Lets go again!")
        import submain
    else:
        restart = input("Would you like to restart?")
        if restart == "Yes":
            import submain
        else:
            exit()
elif mood == "Bad":
    print("So it isn't good!")
    right = input("Is that right?")
    if right == "Yes":
        restart = input("Would you like to restart?")
        if restart == "Yes":
            import submain
        else:
            exit()
    else:
        restart = input("Would you like to restart?")
        if restart == "Yes":
            import submain
        else:
            exit()
else:
    print("Ok")
    exit = input("Press any key to continue, then press enter")
    
