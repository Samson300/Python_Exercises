# Counts down from user input, 1 second delay
import time

user_input = int(input("Where do you want to start the count 1-20? "))

if user_input > 20:
    user_input = int(input("Ooops did you pick a number between 1-20? "))

while user_input >=1:
    print(user_input)
    time.sleep(1)
    user_input -= 1
    if user_input == 0:
        print("Blastoff!")