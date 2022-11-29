from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    result = 0
    while queue:
        x, y = queue.popleft()

        for i in range(len(dirx)):
            dx = x + dirx[i]
            dy = y + diry[i]

            if (dx >= m) or (dy >= n) or (dx < 0) or (dy < 0):
                continue
            
            if graph[dx][dy] == 0:
                continue
            
            if graph[dx][dy] == 1:
                result +=1 
                graph[dx][dy] += 1 # 방문 표시
                queue.append((dx, dy))
    return result
n, m = map(int, input().split())

graph = []
for _ in range(n):
    # graph.append(list(map(int, input())))
    graph.append(list(map(int, input().split())))

# 상, 하, 좌, 우
dirx = [0, 0, -1, 1]
diry = [-1, 1, 0, 0]

print(bfs(0, 0))