'''A quick print vs return example'''

# define a function that returns the input 'x', multipled by 2
def return_2x(x):
    return 2*x

# call the function and print its return value
print(return_2x(3))


# define a new function that prints the result of multiplying the input 'x' by 2
def print_2x(x):
    print(2*x)

# call the function to see the result
print_2x(3)


# What happens if we call print() on our print_2x function? Can you explain the output?
print(print_2x(3))


'''
Galvanize Data Science Prep
https://www.galvanize.com/data-science/prep
'''
