text = "programming"
freq = {}

for i in text:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

count_ch = 0

for j in freq:
    if freq[j] == 1:
        count_ch += 1
        print(j)

print(count_ch)