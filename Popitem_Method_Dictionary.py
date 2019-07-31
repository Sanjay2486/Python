#popitem() method: unlike pop() method, this can delete any key:value pair randomly

User= {
        "Name":"Sanju",
        "Age": 25,
        "ID":1
        }
    
popped_item = User.popitem()
print(popped_item)
print(User)