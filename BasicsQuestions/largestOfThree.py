def largest_of_three(a , b , c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else :
        return c

result = largest_of_three(12 , 13 , 7)
print(result)