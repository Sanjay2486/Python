#Tuple Unpacking: assigning of tuples  elements to variables. 
#note: count of variables must to equals to count of element else it will through an error like : "Too many tuples to unpack"
# Example
days = ("Mon","Tues","Wed")

print(days)
#now lets unpack it
day1,day2,day3 = (days) #here tuples elements are assigned to individual elements
print(day1)
print(day2)
print(day3)

#error code : "too many values to unpack (expected 2)"
# day1,day2, = (days) #this is error code.. do not try this..  just for undestanding

