#Functions: it helps in avoiding writting same taks code again and again by defining function and call it whenever it requires

#Example: suppose you have a senario where you always want to sum two numbers

def Sum_Number(Num1,Num2):
    return(Num1+Num2)

Get_Total = Sum_Number(2,2)
print(Get_Total)

#Example2: Function to concatenate 2 string values

FirstName="Sanju"
LastName = "Singh"

def FullName(Name1,Name2):
    return(Name1+Name2)

print(FullName(FirstName,LastName))

#Example3: Function to retuen last character from the return value
def Last_Char(Name):
    return(Name[-1])

print(Last_Char("Sanjay"))

#Example4: Odd or even number

def Odd_Even(Num):
    if Num%2==0:
        return("Even")               
    else:
        return("Odd")

print(Odd_Even(int(input("Enter Any Number : "))))

#Function without passing any argument or Function without parameters

def comments():
    return ("Log out")

print(comments())
