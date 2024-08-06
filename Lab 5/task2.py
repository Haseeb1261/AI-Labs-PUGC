from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbour):
        if node not in self.graph:
            self.graph[node] = []
        if neighbour not in self.graph:
            self.graph[neighbour] = []
        self.graph[node].append(neighbour)

    def breadth_first_search(self, start,goal):
        visited = set()
        queue = deque([start])

        visited.add(start)

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            if node == goal:
                print("\nFound target")
                return

            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

        print("\nTarget not found")
        return

dataGraph = {
    'A': {'B', 'C', 'D'},
    'B': {'E', 'F'},
    'C': {'G'},
    'D': {},
    'E': {},
    'F': {},
    'G': {}
}

graph = Graph()
for node, neighbours in dataGraph.items():
    for neighbour in neighbours:
        graph.add_edge(node, neighbour)

graph.breadth_first_search('A', 'G')
