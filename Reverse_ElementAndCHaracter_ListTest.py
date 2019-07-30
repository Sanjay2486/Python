#Ask user to input words and convert it into list
#Write a python function which will reverse the list along wiht character of each element in it
#Example:
#['abc','def','ghi']---->['ihg','fed','cba']

#user input
User_List  = list(input("Enter Words : ").split(","))

#create empty list
Output_List = []

#function to reverse element in list along with character of each elements
def Get_User_List(Parameter_List):
    for Each_Words in range(len(Parameter_List)):
        popped_Item = Parameter_List.pop()
        print(popped_Item)       
        New_Word = popped_Item[::-1]
        Output_List.append(New_Word)
    
    return Output_List

#Call Function and print output
print(Get_User_List(User_List))


