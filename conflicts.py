def add(a, b):
    return a+b

def multiply(*args) :
    prod = 1
    for a in args :
        prod *= a
    return prod
        

print(add(1,2))
