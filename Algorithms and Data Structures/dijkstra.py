#!/usr/bin/env python3

import pydot
import sys

#graph = [[ 0, 4,  0, 0,  0,  0,  0, 8,  0],
#         [ 4, 0,  8, 0,  0,  0,  0, 11, 0],
#         [ 0, 8,  0, 7,  0,  4,  0, 0,  2],
#         [ 0, 0,  7, 0,  9,  14, 0, 0,  0],
#         [ 0, 0,  0, 9,  0,  10, 0, 0,  0],
#         [ 0, 0,  4, 14, 10, 0,  2, 0,  0],
#         [ 0, 0,  0, 0,  0,  2,  0, 1,  6],
#         [ 8, 11, 0, 0,  0,  0,  1, 0,  7],
#         [ 0, 0,  2, 0,  0,  0,  6, 7,  0]]
#src = 0
#dst = 5

         # Silicon Valley graph from lecture
names = ['SF', 'SR', 'RM', 'OL', 'SM', 'HW', 'PA', 'FM', 'SJ', 'SCL', 'SV', 'WV', 'SCR', 'HMB', 'P']
         # SF  SR  RM  OL  SM  HW  PA  FM  SJ SCL  SV  WV SCR HMB   P
graph = [[  0, 18,  0, 12, 20,  0,  0,  0,  0,  0,  0,  0,  0,  0, 15], # SF
         [ 18,  0, 15,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], # SR
         [  0, 15,  0, 15,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], # RM
         [ 12,  0, 15,  0,  0, 20,  0,  0,  0,  0,  0,  0,  0,  0,  0], # OL
         [ 20,  0,  0,  0,  0, 20, 18,  0,  0,  0,  0,  0,  0, 25,  0], # SM
         [  0,  0,  0, 20, 20,  0,  0, 14,  0,  0,  0,  0,  0,  0,  0], # HW
         [  0,  0,  0,  0, 18,  0,  0,  0,  0, 10,  0,  0,  0,  0,  0], # PA
         [  0,  0,  0,  0,  0, 14,  0,  0, 20,  0,  0,  0,  0,  0,  0], # FM
         [  0,  0,  0,  0,  0,  0,  0, 20,  0, 15,  0, 60,  0,  0,  0], # SJ
         [  0,  0,  0,  0,  0,  0, 10,  0, 15,  0, 35,  0,  0,  0,  0], # SCL
         [  0,  0,  0,  0,  0,  0,  0,  0,  0, 35,  0,  0, 10,  0,  0], # SV
         [  0,  0,  0,  0,  0,  0,  0,  0, 60,  0,  0,  0, 70,  0,  0], # WV
         [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10, 70,  0, 50,  0], # SCR
         [  0,  0,  0,  0, 25,  0,  0,  0,  0,  0,  0,  0, 50,  0, 15], # HMB
         [ 15,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 15,  0]] # P
src = 1  # SR
dst = 11 # WV


def dijkstra(graph, source):
    """
    Runs Dijkstra's algorithm on a graph starting from source.
    Returns the shortest distance to all nodes from source and the predecessor
    for each nodes on the shortest path.
    """
    num_vert = len(graph)
    dist = [sys.maxsize] * num_vert
    prev = [None] * num_vert
    vset = set(range(num_vert))
    dist[source] = 0

    def min_distance():
        """ Return node with lowest distance in the set of remaining nodes."""
        min_dist = sys.maxsize
        min_v = sys.maxsize
        for v in vset:
            if dist[v] < min_dist:
                min_dist = dist[v]
                min_v = v
        return min_v

    while vset:
        u = min_distance()
        if u == sys.maxsize:
            print("none of the remaining nodes reachable")
            return dist, prev
        vset.remove(u)
        for v in vset:
            if graph[u][v] > 0: # is there a connection from u to v?
                if dist[v] > dist[u] + graph[u][v]:
                    dist[v] = dist[u] + graph[u][v]
                    prev[v] = u

    return dist, prev


def find_path(prev, dst):
    """Extract the shortest path from the predecessor list."""
    stack = []
    u = dst
    if prev[u] is not None:
        while u is not None:
            stack.insert(0, u)
            u = prev[u]
    return stack


def write_graph(graph, src, dist, path=None):
    """Write the graph, shortest paths, and the shortest path from the predecessor list."""
    digraph = pydot.Dot(graph_type='digraph')
    for i in range(len(graph)):
        digraph.add_node(pydot.Node(i, label=names[i]))
    for i in range(len(graph)):
        for j in range(i, len(graph)): # assume undirected graph, process only lower triangular matrix
            if graph[i][j] > 0:
                digraph.add_edge(pydot.Edge(i, j, arrowhead='none', label=graph[i][j]))
    for i in range(len(graph)):
        if i != src
        # blue edges for all shortest paths starting from 'src'
        digraph.add_edge(pydot.Edge(src, i, label=dist[i], fontcolor='blue', color='blue'))
    if path:
        s = path[0]
        c = 0
        for n in path[1:]:
            # red edges for the shortest paths from 'src' to 'dst'
            c += graph[s][n]
            digraph.add_edge(pydot.Edge(s, n, label=c, fontcolor='red', color='red'))
            s = n
    digraph.write_pdf('graph.pdf')


dist, prev = dijkstra(graph, src)
path = find_path(prev, dst)
print(f"path from {src} to {dst}: {path} with distance {dist[dst]}")
print(f"dist: {dist}")
print(f"prev: {prev}")
write_graph(graph, src, dist, path)
