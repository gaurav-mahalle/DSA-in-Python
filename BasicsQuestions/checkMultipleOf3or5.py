num = int(input())

if num % 3 == 0 and num % 5 ==0:
    print("Multiple of both")

elif num % 3 == 0:
    print("Multiple of 3")

elif num % 5 == 0:
    print("Multiple of 5")

else:
    print("Neither multiple of 3 nor 5")