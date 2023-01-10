year = int(input())
#윤년은 4의 배수면서 100의 배수가 아닐 떄 똔ㄴ 400
print(1) if(year%4==0 and year%100!=0) or (year%400==0) else print(0)