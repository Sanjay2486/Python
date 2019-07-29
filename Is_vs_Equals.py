# 'is' vs '==' comparision:
#               OUTPUT                      DIFFERENT_MEMORY_LOCATION
#   '=='    TRUE(if same list)              even though memory location are different
#   'is'    TRUE(if same list)              even though memory location are same
#   'is'    FALSE(if same list)             if memory location are different

List1 = [1,2,3]
List2 = [1,2,3]
    

if List1 == List2:
     print("Yes")
else:
    print("No")


if List1 is List2:
    print("Yes")
else:
    print("No")
