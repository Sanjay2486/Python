#Common Eelemt Finder
# Create two list and wrtite a python function which will give you common element in both list
#Example:
#input---->[1,2,3,4] [1,2,5,6,7]
#output--->[1,2]

output = []

def Common_element_Finder(List_Parameter1,List_Parameter2):
    #get each sub list
    for Each_SubList in List_Parameter1:
        if Each_SubList in List_Parameter2:
            output.append(Each_SubList)
    return output
    
print(Common_element_Finder([1,2,3,4],[5,6,7,1,2,9]))


