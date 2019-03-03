# Surrounds user input by *
user_input = input("Your text is surrounded! Come out with your hands up!! ")
print(("*" * (len(user_input)+2)) + "\n*" + user_input + "*\n" +("*" * (len(user_input)+2)))