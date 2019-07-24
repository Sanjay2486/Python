#*****************Replace Method******************

#simple replace example
Name = "sanjay singh"
print(f"orignal value  : {Name}")
Name = Name.replace(" ","_")
print(f"replaced value : {Name} ")

#replace only first is word in entire sentence
sentense = "SUV is my car and it is best"     #i want you to replace only 1st is
print(sentense.replace ("is","was",1))

#****************Find Method**********************

test1 = "He has nice python code and has nice explainations"

#find the position of 2nd has dynamicily
print(test1.find("has",test1.find("has",1,len(test1))+1,len(test1)))

