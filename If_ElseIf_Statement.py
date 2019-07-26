# Check If age is btween 25 to 30, if yes then print "you are eligible"
#note: use if elseif statement

Age = int(input("Enter Your Age: "))

if Age==0 and Age < 0:
    print("Wrong Input")
elif 0<Age<=10:
    print("Too Young")
elif 10<Age<=25:
    print("still Young")
elif 25<Age<35:
    print("Eligible")
else:
    print("Too Old")
