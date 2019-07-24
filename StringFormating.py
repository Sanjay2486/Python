# String Formating : using place holder {} we can pass the variable value without converting it into str value while printing the output
Name = "Sanju"
Age = 25
print(f"My name is {Name} and Age is {Age}")

# if you want to increase age by 2 so we can do that calculation as well
print(f"My name is {Name} and Age is {Age + 2}")

# *********************************************Test********************************************************************** 
# Ask user to input 3 numbers and you have to print average of all three number. Use String Format concept to get average.
# Note: input should be separated by coma
nu1,num2,num3 = input("Please enter numbers: ").split()
print(f"Average is {(int(nu1)+int(num2)+int(num3))/3}")


