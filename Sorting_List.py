#Sorting List: it sort the list and changes the original list as well.

fruits = ["Apple","Orange","Mango","Banana","Apple","Orange","Pineapple"]

fruits.sort()
print(fruits)

Numbers = [3,5,2,4,1,6,8,7,]
Numbers.sort()
print(Numbers)

#sorted() method : it sorts the list but wont change the original list 
Numbers1 = [3,5,2,4,1,6,8,7,]
print(sorted(Numbers1))
print(Numbers1)

#Clear methos () : It clears the entire list
Numbers1.clear()
print(Numbers1)

#Copy() method: you can copy any list and create new list
Number2 = Numbers.copy()
print(Number2)

