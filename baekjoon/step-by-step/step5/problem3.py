def is_hansu(n):
    n = list(n)
    if (int(n[0])-int(n[1])) == (int(n[1])-int(n[2])):
        return True
    else: return False

num = input()
result = 0
if len(num)<=2:
    print(num)
elif len(num)>=3:
    if len(num)==4: n = str(int(num)-1)
    result = 99
    for n in range(100, int(num)+1):
        if not is_hansu(str(n)): continue
        result+=1
    print(result)