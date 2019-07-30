#create a range of list from 1 to 10 
#write a python function which will create sub list of odd and even number from range list

#Example : 
# List[1,2,3,4,5,6,7,8,9] ------> [[1,3,5,7,9][2,4,6,8]]

Number_List = list(range(1,11))
# print(Number_List)

Odd_List = []
Even_List= []
Final_List = []

def Odd_Even_Function(List_Parameter):
    for Each_Element in List_Parameter:
        if Each_Element%2==0:
            Even_List.append(Each_Element)
        else:
            Odd_List.append(Each_Element)

    Final_List.append(Even_List)
    Final_List.append(Odd_List)
    return Final_List

print(Odd_Even_Function(Number_List))
                