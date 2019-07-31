#Update() method: this method is use to update new key:values in existing dictionary

User= {
        "Name":"Sanju",
        "Age": 25,
        "ID":1
        }

New_Dictionary = {"State":"Karnataka","City":"Bangalore","Pin":560068,"Hobbies":["DJ","Travelling","TV"]}

#now add New_Dictionary into User Dictionary
User.update(New_Dictionary)
print(User)

#Now suppose user tries to update new key which is already present but values differ
New_Dictionary = {"Name":"Sanjay","State":"Karnataka","City":"Bangalore","Pin":560068,"Hobbies":["DJ","Travelling","TV"]}
User.update(New_Dictionary)
print(User) # python will replace the old key:value with new key:value





