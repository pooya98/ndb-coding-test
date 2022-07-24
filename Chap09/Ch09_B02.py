N, M = map(int, input().split())
INF = int(1e9)

graph = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(0, N + 1):
    graph[i][i] = 0

for _ in range(M):
    v1, v2 = map(int, input().split())

    graph[v1][v2] = 1
    graph[v2][v1] = 1

X, K = map(int, input().split())

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

if graph[1][K] != INF and graph[K][X] != INF:
    print(graph[1][K] + graph[K][X])
else:
    print("-1")