#Keys in Dictionary

#we can check if key is present in dictionary or not
#Example:

User= {
        "Name":"Sanju",
        "Age": 25
        }
print(User)

#IF Condition to check if key is there or not
if "Name" in User:
    print("Key present")
else:
    print("No Key Found")


#We can also check if the value is presnet in dictionary or not
if "Sanju" in User.values():
    print("Value Present")
else:
    print("No value Found")