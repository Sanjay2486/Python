#Pop() Method: this method remove the last element from list. However, it also returns the indexed position of the popped elements 
#               so that we can retrive that popped element again

Number = list(range(1,11))
print(Number)

Number.pop()
print(Number)

print(Number.pop())