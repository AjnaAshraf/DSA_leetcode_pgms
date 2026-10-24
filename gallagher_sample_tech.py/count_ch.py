s = "banana"

frq = {}

for ch in s:
    if ch in frq:
        frq[ch] += 1
    else:
        frq[ch] = 1
print(frq)