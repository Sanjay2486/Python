#List within list:

matrix = [[1,2,3],[4,5,6],[7,8,9]]  #this list has 3 element.
print(matrix)

# print(matrix[0])    #here entire first list will be considered as a single element

#for loop to read each item and sub item in it
for each_matrix_list in matrix:    
    print(each_matrix_list)
    for each_list in each_matrix_list:
        print(each_list)

# now how to access sub list item
#Example: access 5
print(matrix[1][1])

#Example to access 6
print(matrix[2][1])

