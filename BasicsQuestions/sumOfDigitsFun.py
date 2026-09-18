def sum_digits(n):
    total = 0
    while n > 0:
        digit = n % 10 
        total = total + digit
        n = n // 10
    return total

result = sum_digits(12345)
print(result)
