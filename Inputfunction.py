# Name = input("Enter Your Name : ")
# print(Name)

# # Sum two number by user
# num1 = int(input("Enter Number 1: "))
# num2 = int(input("Enter Number 2: "))
# print(num1+num2)

#float() used to have output in decimal places
# print(float(num1+num2))

# multipule input in single input function
name,age,mobile = input("Enter Your Name, Age and Mobile: ").split()
print(name)
print(age)
print(mobile)

#split(,) : using comma in split function
name,age,mobile = input("Enter Your Name, Age and Mobile: ").split(",")
print(name)
print(age)
print(mobile)
