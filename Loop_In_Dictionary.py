#Looping with Dictionary

User= {
        "Name":"Sanju",
        "Age": 25
        }
 
#print all key in dictionary
for Each_Key in User:
    # print(Each_Key)


#print all values in dictionary
    for Each_Key in User.values():
        # print(Each_Key)


# item method : 
        for Each_Key in User.items():
            print(Each_Key)

User_Info = User.items()
print(User_Info)

#print key and values together using loop
for each_key, each_value in User.items():
    print(f"key is {each_key} and value is {each_value}")

