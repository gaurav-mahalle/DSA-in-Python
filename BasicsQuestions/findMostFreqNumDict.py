numbers = [2, 1, 2, 3, 2, 1, 4, 2]
frequency = {}

for num in numbers :
    if num in frequency :
        frequency[num] = frequency[num] + 1

    else:
        frequency[num] = 1

most_freq = 0
max_count = 0

for key in frequency:

    if frequency[key] > max_count :
        max_count = frequency[key]
        most_freq  = key

print(most_freq)