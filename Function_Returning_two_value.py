#Functions Returning Two output:
#if function return more then one value then it returns in form of tuple
#but values can be seprated by using tuple unpacking concept where values are assigned to new individial variables

#Example:
def Get_values(num1,num2):
     add  = num1+num2
     multiply = num1*num2
     return add, multiply
    
print(Get_values(2,4))      #this will return tuple output

#so, to make it separate assign the value to individual new variables like below
add_output, multipule_output =  Get_values(2,4)
print(add_output)
print(multipule_output)
