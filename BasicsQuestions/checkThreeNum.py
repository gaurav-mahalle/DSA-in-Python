num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 == num2 and num2 == num3 :
    print("All are equal")

elif num1 == num2 or num2 == num3 or num1 == num3:
    print("Two are equal")

else:
    print("All are different")