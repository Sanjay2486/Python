#How to convert tuple to list:

#create simple tuple of range from 1 to 10
number = tuple(range(1,11))
print(number)

#now convert number tuple to list
number1 = list(number)
print(number1)

#How to convert tuple to string
number2 = tuple(range(1,11))
print(number2)

#now convert number tuple to list
number3 = str(number2)
print(number3)
print(type(number3))

Dummy_tuple = (3,2,1,4,6,8,5,10)
print(type(Dummy_tuple))
print(sorted(Dummy_tuple))