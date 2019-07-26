#While Loop : it run the statment untill it condition becomes false

Number = 1

while Number<=10:
    print(f"Number is Samller then 10 /n running loop {Number}")
    #increment Number value by 1
    Number = Number +1


# Sum all increment value under variable Number

Number = 0
GetTotal = 0
while Number<=10:
    print(f"Running Loop {Number} And SumValue is : {Number + 1}")
    GetTotal += Number
    print(GetTotal)
    Number += 1


