#Ask user to input numbers and convert it into list
#define function in python which will reverse the list using append and return method only

#User input:
User_List = list(input("Enter Numbers : ").split(","))

print(f"Using Reverse function : \n{list(reversed(User_List))})")
print(f"Using [::-1] : \n{list(reversed(User_List))})")
#creating empty Reversed list varibale
Reversed_List = []

#Defining function which will read user input list and append it in Reversed_List[] in revers order
def Reverse_Function(List_Parameter):
    i = 1
    #loops to read each elemene to list in reverse order
    while i <= len(List_Parameter):
        Reversed_List.append(List_Parameter[-i])
        i += 1
    # for Each_Parameter in List_Parameter:
        
    return Reversed_List

#call function
print("Using Append Method:")
print(Reverse_Function(User_List))

