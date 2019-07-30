#Define a function which will take list containing number as input
#and return square of each number element in list

#Example : user inputs number list like
#Number = [1,2,3,4]
#output = [1,4,9,16]

#Define function which will give square root of each number element 
def Number_Square(Number):
    Square_List = []    
    for Each_Number in Number:
        Square_List.append(int(Each_Number)**2)            
    return Square_List

#Take user input as list 
print(Number_Square(list(input("Enter Number : ").split(","))))