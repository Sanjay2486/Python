#pop() method: It is use to delete any key:value pair from dictionary

User= {
        "Name":"Sanju",
        "Age": 25,
        "ID":1
        }

print(User)

#pop ID key and values . Note: you can store the popped item in new variable 

popped_item = User.pop("ID")
print(popped_item)
print(User)

