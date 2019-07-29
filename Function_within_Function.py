def Greater(a,b):
    if a>b:
        return a
    else:
        return b

#print(Greater(100,20))

def New_Greater(a,b,c):
    bigger = Greater(a,b)
    return Greater(bigger,c)

print(New_Greater(101,204,30))

