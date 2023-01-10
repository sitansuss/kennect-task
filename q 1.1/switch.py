def zero():
    return "zero"

def one():
    return "one"

def default():
    return "default"

def switch_case(case):
    cases = {
        0: zero,
        1: one
    }
    return cases.get(case, default)()

print(switch_case(0)) # "zero"
print(switch_case(1)) # "one"
print(switch_case(2)) # "default"
