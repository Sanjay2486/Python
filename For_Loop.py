#For Loop with range functions
for i in range(10):
    print("Hello World")

# #suppose my range value starts with 5 and ends with 10 , then
for i in range(5,10):
    print("Hello World")

#Break
for i in range(1,11):
    if i==5:
        break
    print(i)

#Conitue
for i in range(1,11):
    if i==5:
        continue    # this will skip number 5
    print(i)