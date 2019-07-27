#Ask user to enter any name
#Write a python code which will give you output like below:
#Suppose user enters:  Sanjay singh
#Output :
#       S:1
#       a:2
#       n:2
#       j:1
#       y:1
#        :1
#       s:1
#       i:1
#       g:1
#       h:1

User_Input_Name = input("Enter Name : ")

intcrement_loop = 0
temp = ""

while intcrement_loop <= len(User_Input_Name)-1:
    if User_Input_Name[intcrement_loop] not in temp:
        temp += User_Input_Name[intcrement_loop]
        print(temp)
        print(f"{User_Input_Name[intcrement_loop]}:{User_Input_Name.count(User_Input_Name[intcrement_loop])}")    
    intcrement_loop += 1
    
