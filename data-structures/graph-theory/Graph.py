from collections import defaultdict
from typing import Set

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)
	
	def bfs(self, s):
		visited = set()

		queue = []

		queue.append(s)

		visited.add(s)

		while queue:
			v = queue.pop(0)

			print(v, end=" ")

			for i in self.graph[v]:
				if i not in visited:
					visited.add(i)
					queue.append(i)

	def dfs_recursive(self,s):
		visited = set()

		self.dfs_driver(visited, s)
	
	def dfs_driver(self,visited: Set[int], source):
		if source not in visited:
			print(source, end=" ")
			visited.add(source)

			for neighbor in self.graph[source]:
				self.dfs_driver(visited, neighbor)


	def dfs_iterative(self,s):
		pass


if __name__ == "__main__":	
	g = Graph()
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(1, 2)
	g.addEdge(2, 0)
	g.addEdge(2, 3)
	g.addEdge(3, 3)


	g.dfs_recursive(2)