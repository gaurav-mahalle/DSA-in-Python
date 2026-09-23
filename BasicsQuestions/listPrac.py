numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[1])
print(numbers[2])

print(numbers[-1])
print(numbers[-2])

numbers[-1] = 60        # lists are mutable

print(numbers)

print(len(numbers))

for i in numbers :
    print(i)

print("Values of list using index while looping:")

for i in range(len(numbers)):

    print(numbers[i])




