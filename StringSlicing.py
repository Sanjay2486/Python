#String Slicing : is use to print sub string within string value
# syntax : [Start Argument : Stop Argument]
Language = "Python"

#print "th" from python
#                012345                 
print(Language[2:4])

#print sub strting from y character till end 
print(Language[1:])

# Print Sub string only with end argument 3 length
print(Language[:4])

#Step argument
print(Language[0:5:1])  #step argument is 1
print(Language[0:5:2])  #code will move by 2 steps

# reverse string
print(Language)
print(Language[3:0:-1])
print(Language[3:1:-1])
print(Language[3:2:-1])
print(Language[3::-1])


