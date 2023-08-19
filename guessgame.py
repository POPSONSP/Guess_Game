"""
Project:
Create a guessing game, user have access to 3 attempts  to enter any number between 0 and 9 after which the game will end,
if the user entered the right number, the user win the game.
"""

guess_count=0
right_number="5"
while guess_count <3:
    user=input("enter your guesss number: ")
    if user==right_number:
        print("you have won")
        break
    else:
        print("you have entered the wrong input")
    guess_count+=1    
    
else:
    print("you have exceeded the number of trial")


    
    