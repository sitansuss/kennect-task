"""
n Python, a closure is a nested function that remembers the values in its enclosing 
lexical scope even when the program flow is no longer in that scope. In other words, a 
closure allows a function to remember the state of its environment when it was defined, 
and to continue to access that state even when the function is invoked outside of that 
environment.
"""


def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)
print(closure(5))  # 15


