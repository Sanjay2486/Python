#Random Gussing Game
import random

winning_number = random.randint(1,100)
Guss = 1
User_Number = int(input("Guess a number between 1 to 100"))
game_over = False

while not game_over:
    if User_Number==winning_number:
        print(f"you win and you guessed in {Guss} time")
        game_over = True
    else:
        print("Wrong Guess")
        Guss += 1
        User_Number = int(input("Guess a number between 1 to 100"))

