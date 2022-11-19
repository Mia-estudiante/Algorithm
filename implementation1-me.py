N = int(input())
data = list(input().split())

loc = [1, 1]

dird = {
    'L': [0, -1],
    'R': [0, 1],
    'U': [-1, 0],
    'D': [1, 0]
}

for d in data:
    loc[0] += dird[d][0]  
    loc[1] += dird[d][1]
    if((loc[0] <1) or (loc[1] < 1) or (loc[1] > N) or (loc[0] > N)):
        loc[0] -= dird[d][0]
        loc[1] -= dird[d][1]
    # print(loc)
print(loc[0], loc[1])