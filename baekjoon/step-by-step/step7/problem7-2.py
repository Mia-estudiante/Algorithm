sugar = int(input())
result = 0

while(sugar>=0):
    if not sugar%5: 
        result += sugar//5
        print(result)
        break
    sugar-=3
    result+=1
else:
    print(-1)

'''
while문에서 sugar=0이 되었을 경우,
0도 5의 배수이기에 break를 통해 while문을 나온다.
'''
