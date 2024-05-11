#!/usr/bin/env python3

import pydot

# use dictionary as adjacency list
graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

def write_graph(graph):
    digraph = pydot.Dot(graph_type='digraph')
    for node in graph:
        digraph.add_node(pydot.Node(node))
    for node in graph:
        for neighbor in graph[node]:
            digraph.add_edge(pydot.Edge(node, neighbor))
    digraph.write_pdf('dfs-graph.pdf')
    digraph.write_png('dfs-graph.png')
    digraph.write_dot('dfs-graph.dot')

def dfs(graph, node, visited=None):
    if visited is None:
        visited = []
    if node not in visited:
        # logic to handle node
        visited.append(node)
        for neighbor in graph[node]:
            visited = dfs(graph, neighbor, visited)
    return visited


write_graph(graph)
order = dfs(graph, 'A')
print(order)
order = dfs(graph, 'B')
print(order)

path1 = dfs(graph, 'A')
path2 = dfs(graph, 'B', [])
print(' '.join(path1))
print(' '.join(path2))
