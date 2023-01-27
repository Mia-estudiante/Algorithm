sugar = int(input())
result = 0

while(sugar>0):
    if not sugar%5: 
        result += sugar//5
        break
    sugar-=3
    result+=1

print(result) if sugar>=0 else print(-1)
