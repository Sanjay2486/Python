#get() method: this is use to access key values from dictionary
#note: if ket is not present then it will return none value, instead error

User= {
        "Name":"Sanju",
        "Age": 25,
        "ID":1
        }

#get() method
print(User.get("Name"))

#Example for unknown key
print(User.get("Namessss"))     #this will return none as this key is not present in dictionary

User.clear()
print(User)