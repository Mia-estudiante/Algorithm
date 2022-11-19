string = input()
alpha = list()
result = 0 
for s in string:
    if s.isalpha():
        alpha.append(s)
    else:
        result += int(s)

print(''.join(sorted(alpha))+str(result))

'''
1) 숫자가 하나도 없는 경우도 생각하자
2) list -> string
'''