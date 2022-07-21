# Simple(But slow) Dijkstra Algorithm
# Python
# Time Complexity : O(V^2) ('V' is # of Vertices)


import sys
input = sys.stdin.readline
INF = int(1e9)

num_of_nodes, num_of_edges = map(int, input().split())
start_node = int(input())


# graph, visited, distance information initiation
graph = [[] for _ in range(num_of_nodes + 1)]
visited = [False] * (num_of_nodes + 1)
distance = [INF] * (num_of_nodes + 1)


# receive graph information
for _ in range(num_of_edges):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def get_smallest_node():
    min_distance = INF
    index_of_min_distance = 0

    for i in range(1, num_of_nodes + 1):
        if (distance[i] < min_distance) and not visited[i]:
            min_distance = distance[i]
            index_of_min_distance =  i

    return index_of_min_distance


def dijkstra(start):

    # step_0
    distance[start] = 0
    visited[start] = True

    # step_1
    for (dest, distan) in graph[start]:
        distance[dest] = distan


    # step_2 ~
    for i in range(num_of_nodes - 1):
        current_node = get_smallest_node()
        visited[current_node] = True

        for (dest, distan) in graph[current_node]:
            cost = distance[current_node] + distan

            if cost < distance[dest]:
                distance[dest] = cost



dijkstra(start_node)


# print shortest distance for each node
for i in range(1, num_of_nodes + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])


