#Example to add value to key

#create a blank dictionary
Emp_Details = {}
# print(Emp_Details)
# print(type(Emp_Details))

#now create a list of key
Emp_Parameter = ["Name","Age","ID"]
Emp_Value = ["Sanju",25,1]
i = 0

#Add this list to dictionary Emp_detail
for Each_Emp_Parameter in Emp_Parameter:
    # print(Each_Emp_Parameter)
    Emp_Details[Each_Emp_Parameter] = Emp_Value[i]
    i += 1
    
# print(Emp_Details)

# Suppose you have list of emp names and their respective age and id.
# Add multipule entry for all 3 keys in Emp_Details Dictionary
Emp_Name = ["Singh","Arti","Poonam"]
Emp_Age = [30,25,24]
Emp_ID = [2,3,4]

for Each_Emp_Parameter in Emp_Parameter:
    #for Name key
    if "Name" in Each_Emp_Parameter:                
        Emp_Details[Each_Emp_Parameter] = Emp_Name
    elif "Age" in Each_Emp_Parameter:
        Emp_Details[Each_Emp_Parameter] = Emp_Age
    else:
        Emp_Details[Each_Emp_Parameter] = Emp_ID

print(Emp_Details)

