#list inside tuple: As concepts say tuple is immutable and we cannot make modification to it
#But, if we define list within tuple the it is possible to make all modification like: insert, delete, remove, etc..

#Example:

Days = ("Mod","Tues",["Wed,Thurs"])
print(Days)

#now i append new element in list in tuple days
Days[2].append("Fri")
print(Days)

#pop()
print(Days[2].pop())
print(Days)