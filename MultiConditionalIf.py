# Check multi condition using IF statement

# AND OPERATOR
Name="Sanju"
Age=25

User_Input_Name = input("Enter Name : ")
User_Input_age = int(input("Enter Age : "))

if User_Input_Name == Name and User_Input_age == Age:
    print("Condition Met")
else:    
    print("Condition Not Met")

# OR OPERATOR
User_Input_Name = input("Enter Name : ")
User_Input_age = int(input("Enter Age : "))

if User_Input_Name == Name or User_Input_age == Age:
    if User_Input_Name == Name:       
        print("Name Condition Met")
    else:
        print("Age Condition Met")
else:    
    print("Condition Not Met")
