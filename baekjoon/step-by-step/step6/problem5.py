word = input().upper()
counts = [0]*26
for i in range(len(word)):
    counts[ord(word[i])-65] += 1
maxindex = [i for i in range(len(counts)) if counts[i]==max(counts)]
if len(maxindex)==1: print(chr(maxindex[0]+65))
else: print("?")