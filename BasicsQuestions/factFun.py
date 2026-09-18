def factorial(n):
    fact = 1
    while n > 0 :
        fact *= n
        n = n - 1
    return fact

result = factorial(5)
print(result)
