# Take two comma input from user 
# 1 intput for username
# 2 input would be for single character to find its count in username
# it should be case insensitive and remove all unwanted space as well using strip() method

Name,char = input("Enter Name and Search Key : ").split(",")
print(f"Name is {Name.strip()} and count of {char.strip()} in name is : {Name.strip().lower().count(char.strip().lower())}")

