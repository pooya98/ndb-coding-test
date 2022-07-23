# Hard(But fast) Dijkstra Algorithm
# Python
# Time Complexity : O(E*logV) ('V' is # of Vertices, and 'E' is # of Edges)

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

num_of_nodes, num_of_edges = map(int, input().split())
start_node = int(input())

# graph, distance information initiation
graph = [[] for _ in range(num_of_nodes + 1)]
distance = [INF] * (num_of_nodes + 1)

# receive graph information
for _ in range(num_of_edges):
    a, b, c = map(int, input().split())

    graph[a].append((b, c))


def dijkstra(start):
    q = []

    # step_0
    heapq.heappush(q, (0, start))
    distance[start] = 0

    # step_1 ~
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for (next_dest, next_dist) in graph[now]:
            cost = dist + next_dist

            if cost < distance[next_dest]:
                distance[next_dest] = cost
                heapq.heappush(q, (cost, next_dest))


dijkstra(start_node)


# print shortest distance for each node
for i in range(1, num_of_nodes + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])