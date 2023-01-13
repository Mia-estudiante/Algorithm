def d(i):
    dn = i
    # while i>0:
    while i:
        dn+=i%10
        i//=10
    return dn

self_numbers = [1]*10000 # 해당 수가 self number가 아니면 0

for i in range(1, 10000):
    dn = d(i)
    if dn<10000: self_numbers[dn] = 0 
    if self_numbers[i]: print(i)
'''
이때 dn은 i보다 항상 크다 그리고 i는 이미 이전 dn을 통해 지나침
(즉, 앞으로의 i들에 의해서 지금의 i가 나중에 dn이 될 리 없다는 것)
그래서 self_numbers 탐색과 동시에 print를 할 수 있는 것
'''
# for i in range(1, 10000):
#     if self_numbers[i]:
#         print(i)
