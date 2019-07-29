# Ask user to input 2 numbers and write a function to return which one is greater

User_Input1 = int(input("Enter Number1 : "))
User_Input2 = int(input("Enter Number2 : "))

def HighestNumber(Num1,Num2):
    if Num1>Num2:
        return(f"Number1: {Num1} is greater then Number2 {Num2} ")
    else:
        return(f"Number2: {Num2} is greater then Number1 {Num1} ")

print(HighestNumber(User_Input1,User_Input2))
    
