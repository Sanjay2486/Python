#********************* Nested IF Statement Test**********************************
# Number guessing Game
# Make a variable, like winning_number and assign any number to it.
# Ask user to guess a number
# if user guessed correctly then print "You Win!!!"
# if user did not guessed correctly the :
#         if user guessed lower thean actual number then print "too low"
#         if user guessed higher then actual number then print "too high"

# Bonus:
# Google "how to generate random number in python " to generate random winning number

winning_number = 25

user_input = int(input("Enter Your Number : "))

if user_input == winning_number:
    print("You Win!!!")
else:
    if user_input > winning_number:
        print("Too High")
    else:
        print("Too Low")

