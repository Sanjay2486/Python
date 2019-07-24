# String indexing: to get the character from a string value using index position
# Note: default index starts with 0 position and to apply index we always use []
language = "Python"

#explainatin
# Char   Index(Start to End)   Index(End To Start)
# P   =  0                              -6
# Y   =  1                              -5
# T   =  2                              -4
# H   =  3                              -3
# O   =  4                              -2
# N   =  5                              -1

print(language[3])
print(language[-5])
#Note: Index out of range means , index number that you have passed is not in the range lenght of the string
