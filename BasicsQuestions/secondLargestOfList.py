numbers = [10, 45, 23, 67, 12, 89, 34]

largest_no = numbers[0]
second_largest = numbers[0]

for i in range(len(numbers)) :
    if largest_no < numbers[i]:
        largest_no = numbers[i]

for i in range(len(numbers)):
    if second_largest < numbers[i] and numbers[i] != largest_no :
        second_largest = numbers[i]


print(second_largest)

    


