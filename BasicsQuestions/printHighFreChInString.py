text = "programming"
freq = {}

for i in text:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

max_count = 0
most_freq =""

for j in freq:
    if freq[j] > max_count:
        max_count = freq[j]
        most_freq = j

# print(max_count)
print(most_freq)