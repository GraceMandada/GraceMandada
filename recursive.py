#defination of the function required in the question
def bunnyEars2(n):
 if n ==0:
   return 0 
 # return 0 if there no bunny left
 if n % 2 ==0:
   return 3 + bunnyEars2(n-1) # call function with addtion of 3 if bunny is at even position
 else:
   return 2 + bunnyEars2(n-1) # call function with addtion of 2 if bunny is not in even position (then bunny should be at odd position)

# checking of required outputs
print(bunnyEars2(0))
print(bunnyEars2(1))
print(bunnyEars2(2))