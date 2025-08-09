
num = [1,2,2,3,3,3,4,4,4,4,5]
freq:dict = {}
for n in num:
    freq[n] = freq.get(n,0) + 1

print(freq)
