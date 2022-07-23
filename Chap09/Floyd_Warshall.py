# Floyd - Warshall Algorithm
# Python
# Time Complexity : O(N^3) ('N' is # of Vertices)

INF = int(1e9)

num_of_nodes = int(input())
num_of_edges = int(input())

# graph initiation
graph = [[INF] * (num_of_nodes + 1) for _ in range(num_of_nodes + 1)]

for a in range(1, num_of_nodes + 1):
    for b in range(1, num_of_nodes + 1):
        if a == b:
            graph[a][b] = 0


# receive graph information
for _ in range(num_of_edges):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# step01 ~
for k in range(1, num_of_nodes + 1):
    for a in range(1, num_of_nodes + 1):
        for b in range(1, num_of_nodes + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


# print shortest distance for each (start, end)
for a in range(1, num_of_nodes + 1):
    for b in range(1, num_of_nodes + 1):
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")

    print()

