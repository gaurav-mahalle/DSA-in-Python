text = "swiss"
freq = {}

for i in text:
    if i in freq :
        freq[i] += 1

    else:
        freq[i] = 1

for j in freq:
    if freq[j] == 1:
        print(j)
        break
    