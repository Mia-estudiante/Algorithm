data = input()
r, c = data[0], int(data[1])
r = int(ord(r))-int(ord('a'))+1
cases = [[1, 2], [-1, -2], [-1, 2], [1, -2], [2, 1],
            [-2, 1], [2, -1], [-2, -1]]
cnt = 0
for ca in cases:
    nr = r + ca[0]
    nc = c + ca[1]
    if nr < 1 or nc < 1 or nr > 8 or nc > 8:
        continue
    cnt += 1
print(cnt)