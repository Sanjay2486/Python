# Ask user to unput number , more then 1 digit: Ex: 1234
# write a python code to add each digit : 1+2+3+4
# Hint: Do not conver input value into int initiality. read it as string value and get each character and then convert it into int()

User_Number = input("Enter Number Of More Then 1 Digit : ")

Sum_Output = 0
Get_Number = 0

if len(User_Number) == 1:
    pass
else:
    while Get_Number <= len(User_Number)-1:
        New_Number = int(User_Number[Get_Number])
        Sum_Output += New_Number
        Get_Number += 1
        
print(Sum_Output)
