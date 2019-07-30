#min() and max() functions

# Number = [1,2,3,4,5]
# print(min(Number))
# print(max(Number))

#write python function which will give you difference between greatest and lowest number
def Gap_Calculator(Number_Parameter):
    return (max(Number_Parameter)-min(Number_Parameter))

print(Gap_Calculator([15,20,60,120,200,350]))

