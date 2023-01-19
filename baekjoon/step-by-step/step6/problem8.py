dial = {
    'abc': 3,
    'def': 4,
    'ghi': 5,
    'jkl': 6,
    'mno': 7,
    'pqrs': 8,
    'tuv': 9,
    'wxyz': 10,
}

word = input().lower()
result = 0

for w in word:
    for key in dial.keys():
        if w not in key: continue
        result += dial[key] 
        break

print(result)