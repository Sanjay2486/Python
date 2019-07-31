# Dictionaries:
# It is used to collect unorderd data.
# unline list, dictioraries keeps the data in order by using "key:value" pairing
#Example: create a dictionary to store user profile

User_Profile = {
                "Name":"Sanju",
                "Age"  : 25,
                "Address": "Bangalore",
                "Spouse" : "Arti"}

print(User_Profile)

#Accessing data from dictionary
#Get name
print(User_Profile["Name"])

#Update values on empty dictionary
dict1 = {}
dict1["Name"] = "Sanju"
print(dict1)
dict1["Age"] = 25
print(dict1)

