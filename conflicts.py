def add(a):
    return a+10
    
print(add(1))

def multiply(*args) :
    prod = 1
    for a in args :
        prod *= a
    return prod
        

