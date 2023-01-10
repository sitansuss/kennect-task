"""
 the continue statement is used to skip the current iteration of a loop and continue with
  the next one. It is commonly used inside for and while loops.

When a continue statement is encountered inside a loop, the current iteration of the loop
 is terminated, and the program execution jumps to the next iteration of the loop, 
 skipping any remaining statements in the current iteration.

"""




i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
