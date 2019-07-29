# Example for default parameters:
# Rule: to create a dafult parameters, its mandetory that your last paramerter must be also be default one

def Default_Paramerters(FirstName,LastName,Age=25):
    print(FirstName)
    print(LastName)
    print(Age)

Default_Paramerters("Sanjay","Singh")

#Now what if you your defult parameter is passed as none

def Default_Paramerters(FirstName,LastName,Age=None):
    print(FirstName)
    print(LastName)
    print(Age)

Default_Paramerters("Sanjay","Singh",25)
