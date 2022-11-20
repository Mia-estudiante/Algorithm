from collections import deque   # 큐 이용(FIFO)

def bfs(graph, start, visited):
    # 1. 시작 노드를 queue에 넣는다.
    queue = deque([start])

    # 2. 현재 노드를 방문 처리한다.
    visited[start] = True

    while queue: # queue가 빌 때까지 반복
        # 3. queue에서 원소 out 
        v = queue.popleft()
        print(v, end=' ')

        # 4. 방금 queue에서 out한 원소와 인접한 노드 확인
        for i in graph[v]:
            if not visited[i]: # 만약 방문하지 않는 노드라면 queue에 넣어주고
                queue.append(i) # 방문 표시
                visited[i] = True 

# 각 노드가 연결된 그래프 - 2차원 리스트
graph = [
    [],
    [2,3,8],    #1
    [1,7],      #2
    [1,4,5],    #3
    [3,5],      #4
    [3,4],      #5
    [7],        #6
    [2,6,8],    #7
    [1,7]       #8
]

# 각 노드가 방문된 정보 표현 - 1차원 리스트
visited = [False]*len(graph)

# BFS 함수 호출
bfs(graph, 1, visited)