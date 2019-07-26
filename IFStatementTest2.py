# Ask user to enter name and age
# if Name starts with A or a and age is greater then 10 then 
#print msg "User accepted" else print msg "User Not accepted"

Name,Age = input("Enter You Name And Age : ").split(",")

print(Name[0].title())
print(int(Age))

if Name[0].title() == "A" and int(Age) >= 10:
    print("User Accepted")
else:
    print("User Not Accepted")