#penambahan(a, b)
def penambahan(a, b):
    return a+b
result = penambahan(2, 5)
print(result)

#pengurangan(a, b)
def pengurangan(a, b):
    return a-b
result = pengurangan(10, 4)
print(result)

#perkalian(a, b)
def perkalian(a,b):
    return a*b
result = perkalian(5, 2)
print(result)

#pembagian(a,b)
def pembagian(a, b):
    if b == 0:
        return a/b
result = pembagian(10, 2)
print(result)
    
#modulus(a, b)
def modulus(a, b):
    return a%b
result = modulus(10, 3)
print(result)

#fibonacci(n)
def fibonacci(n):
    deret : []
    a, b = 0, 1

foe i in range(n):
