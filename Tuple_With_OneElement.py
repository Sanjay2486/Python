#Tuple with one element:
# Tuple can be of 1 element if comma (",") is applied after the element. else it will considered as simple data with its data type

#Example:
Num1 = (1)
print(type(Num1))       #this is int

#where as

Num2 = (1,)
print(type(Num2))       #this is tuple

Name = ("Sanju")        #this is not tuple
print(type(Name))

Name1 = ("Singh",)      #this is tuple
print(type(Name1))

Name3 = "Sanjay","Singh","Kumar"        #this is also a tuple: tuple can be without prenthesis
print(type(Name3))