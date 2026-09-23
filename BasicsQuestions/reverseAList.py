numbers = [5, 10, 15, 20, 25]
reverse = []

for i in range(len(numbers)-1, -1, -1):
    reverse.append(numbers[i])

print(reverse)