#Ask user to input any string.
#write a python code to check if the reverse of user input is same as original string value
#Ex: reverse of madam is madam

# print(User_Input[::-1])
def Is_Palindrome(Input_Value):
    if User_Input[::-1]==User_Input:            
        return "Is palindrome"
    else:        
        return "Its Not Palindrome"

User_Input = input("Enter Any Palindrome String : ")

print(Is_Palindrome(User_Input))