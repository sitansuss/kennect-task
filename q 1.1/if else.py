x = 15
if x > 20:
    print("x is greater than 20")
elif x > 10:
    print("x is greater than 10 but not greater than 20")
else:
    print("x is not greater than 10")



"""
In this example, x is assigned the value 15. The if block checks if x is greater than 20, 
since it's not, it goes to the elif block, which checks if x is greater than 10, which is
 true, so the code in that block is executed and the output is "x is greater than 10 but
  not greater than 20"

It's worth noting that the if block will only execute if the condition is true, if the 
condition is false, it skips the block and goes to the next one. Also, elif (short for 
"else if") can be used multiple times in a single statement to check multiple conditions, 
It's executed only if the condition above it is false.

"""