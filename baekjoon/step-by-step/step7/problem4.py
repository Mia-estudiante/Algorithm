a, b, v = map(int, input().split())

day = (v-b)//(a-b)
print(day+1) if (v-b)%(a-b) else print(day)

'''
도달일: x
올라가는 일수: x
내려오는 일수: x-1
=> ax-b(x-1)=v
'''