word = list(input())
arr = [-1]*26
for i in range(len(word)):
    loc = ord(word[i])-97
    if arr[loc]!=-1: continue
    arr[loc] = i #ord 함수는 정수 Unicode code point(ASCII)를 반환
[print(a, end=" ") for a in arr]