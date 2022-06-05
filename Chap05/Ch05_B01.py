INF = 2

def dfs(graph, v, visited):
    visited[v] = True
    #print(v, end = ' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


N, M = map(int, input().split())

plate = []
icecream = 0
graph = [[] for _ in range(N * M)]
visited = [False for _ in range(N * M)]
count = -1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
di = [-M, 1, M, -1]


for _ in range(N):
    plate.append(input())

for i in range(N):
    for j in range(M):
        count += 1

        if plate[i][j] == '1':
            visited[count] = True
            continue

        for move in range(4):
            next_x = i + dx[move]
            next_y = j + dy[move]
            dest = count + di[move]

            if(next_x < 0 or next_x >= N or next_y < 0 or next_y >= M):
                continue
            else:
                if(plate[next_x][next_y] == '0'):
                    graph[count].append(dest)


for i in range(N * M):
    if visited[i] == False:
        dfs(graph, i, visited)
        icecream += 1
        
print(icecream)
            
            

