#List : collection of elements is square bracket. A list can have various data type element
#List are mutable: Means once created can be edited again

#Simple List Example:

Emp_Name_list = ["Sanju","Arti","Poonam","Rahul","Gopal"]

print(Emp_Name_list)

#Example -2 List with different data type elements
List2 = ["Sanjay",32,"Arti",30,"Poonam","30"]
print(List2)

#slicing in list
#example: print 
# first two name from emp_name_list
print(Emp_Name_list[0:2])
#Last Name
print(Emp_Name_list[-1:0])

#Change the age of arti from 30 to 25
List2[3] = 25
print(List2)

#How to add new element in list : Note : Append method always add new item in last
#Suppose you have list of fruits , and we want you to add new fruit in it
fruit_list = ["Apple","Mango"]
print(f"Old Fruit List {fruit_list}")
#Append Banana now
fruit_list.append("Banana")
print(f"New Fruit List {fruit_list}")

#But what if unlike append method, you want to insert new item in required position
#To do that we use: "Insert Method"

print(f"Old fruit list : {fruit_list}")

#insert pineapple in 1st postion of fruit list
fruit_list.insert(1,"Pineapple")
print(f"New fruit list : {fruit_list}")

#Join or Concatenate two list[]
Alpha_List1 = ["A","B","C"]
Alpha_List2 = ["D","E","F"]
    #now i want to join item of both list and make it one
Alphabats_List = Alpha_List1+Alpha_List2
print(Alphabats_List)

#Extend Method: We can also add new item into list by using extend method().
Alpha_List3 = ["G","H","I"]
    #Now extend Alphabats_List with Alpha_list3
Alphabats_List.extend(Alpha_List3)

#print(f"Extended List : {Alphabats_List}")
Alphabats_List.append(Alpha_List3)
print(Alphabats_List)

#Delete Methods In List:
#1. Pop() : By default it deletes last element from list. But, if position of element is passed as argument then it will
            # the item from that position only

print(f"Original Alphabate list : {Alphabats_List}")
Alphabats_List.pop()
print(f"Alphabate list using pop() method : {Alphabats_List}")
Alphabats_List.pop()
print(f"Alphabate list using pop() method : {Alphabats_List}")
Alphabats_List.pop(2)
print(f"Alphabate list by passing argument to pop() method : {Alphabats_List}")

# Delete Operator : del LIst_name[Index]
#it also delete the element of list based on index position passed as argument
del Alphabats_List[1]
print(Alphabats_List)

#Remove Method():  this method removes the element from list by passing element name directly.
#this is usefull when we are not aware of index position of element
Alphabats_List.remove("H")
print(Alphabats_List)

#IN Operator to check if any elemenr is there in list or not
print(fruit_list)

if "Apple" in fruit_list:
    print("Yes")
else:
    print("No")



