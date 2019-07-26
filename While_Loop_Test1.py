# Ask user to enter any natural number and print sum of 1 to n

User_input = int(input("Enter Number : "))

Increment_Number = 1
Sum_Of_Number = 0

while Increment_Number<=User_input:
    Sum_Of_Number += Increment_Number
    Increment_Number = Increment_Number +1
print(Sum_Of_Number)
