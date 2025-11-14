# Still under construction ^^

sigma = ""
Z = ""

def variogram_function():
    pass

def auxiliary_function_x():
    pass

def auxiliary_function_f():
    pass

lower = Z - 1.96 * (sigma)**0.5
upper = Z + 1.96 * (sigma)**0.5

probability = f'({lower} < Z < {upper}) = 0.95'
print(f'{probability}\n There is 95% of Z grade between {lower} and {upper} bounds')
