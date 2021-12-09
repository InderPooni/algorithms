from collections import defaultdict, deque


class Graph:
	def __init__(self) -> None:
		self.graph = defaultdict(list)
	
	def iterative_dfs(self, source):
		visited = set()

		stack = deque([source])
		visited.add(source)
		while stack:

			node = stack.pop()

			print(node, end=" ")

			for neighbor in self.graph[node]:
				if not neighbor in visited:
					stack.append(neighbor)
					visited.add(neighbor)
				
	
	def bfs(self, source):
		visited = set()
		q = deque([source])
		visited.add(source)

		while q:
			node = q.popleft()
			print(node, end=" ")

			for neighbor in self.graph[node]:
				if neighbor not in visited:
					q.append(neighbor)
					visited.add(neighbor)
	

	def connected_components(self):
		n = len(self.graph)
		visited = [False] * (len(self.graph) + 1)
		connectedComponents = []

		for vertex in range(n):
			if visited[vertex] == False:
				temp = []
				connectedComponents.append(self.dfsUtil(temp, vertex, visited))
		
		return connectedComponents
	
	def dfsUtil(self, temp, vertex, visited):
		visited[vertex] = True

		temp.append(vertex)

		for neighbor in self.graph[vertex]:
			if visited[neighbor] == False:
				temp = self.dfsUtil(temp, neighbor, visited)
		
		return temp

	def add_edge(self, source, destination):
		self.graph[source].append(destination)
		self.graph[destination].append(source)

	
if __name__ == "__main__":
	graph = Graph()
	graph.graph = defaultdict(list)
	graph.add_edge(1, 0)
	graph.add_edge(2, 3)
	graph.add_edge(3, 4)
	graph.add_edge(5, 0)
	connected_components = graph.connected_components()

	print(connected_components)

	