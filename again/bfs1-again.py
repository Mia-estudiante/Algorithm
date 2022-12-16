from collections import deque

def bfs(start, graph, visited):
    #1. 방문 시작할 첫 노드를 queue에 넣기
    queue = deque([start])

    #2. 방문 시작할 첫 노드, 방문 표시
    visited[start] = True

    #3. queue에 노드가 없을 때까지 반복
    while queue:
        now = queue.popleft()
        print(now, end=' ')
        for node in graph[now]:
            if visited[node]:
                continue
            queue.append(node)
            visited[node] = True
            
    return queue

#1. graph 생성
graph = [[],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]]

#2. 방문표시
visited = [False] * len(graph)

#3. bfs 수행
ret = bfs(1, graph, visited)
