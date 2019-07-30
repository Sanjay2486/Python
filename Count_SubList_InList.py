#write a python code to count number of sub list in a single given list

# print(type([1,2,3]))

def Count_SubList(List_Parameter):
    Count_output = 0
    for Each_Element in List_Parameter:
        if type(Each_Element) is list:
            Count_output +=1
    
    return Count_output

print(Count_SubList([1,2,3,[4,5,6],[7,8],9,[10,11,12],[21,25]]))
