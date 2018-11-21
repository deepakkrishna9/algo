from collections import defaultdict

print("Implementing BFS algorithm!!!")

class Node:
	def __init__(self, id):
		self.node_id = id


class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def add_edge(self, u, v):
		self.graph[u].append(v)

	def bfs_search(self, node):
		print(self.graph)
		visited = [False]*(len(self.graph))

		queue = []

		queue.append(node)
		visited[node] = True

		while queue:
        	# Dequeue a vertex from  
            # queue and print it 
			print("Current queue %s"%(str(queue)))
			s = queue.pop(0) 
			print("Traversing from %s found %s"%(str(s),str(self.graph[s])))
			print("#######################")
			# print (s, end = " ")
			# Get all adjacent vertices of the 
			# dequeued vertex s. If a adjacent 
			# has not been visited, then mark it 
			# visited and enqueue it 
			for i in self.graph[s]: 
			    if visited[i] == False: 
			        queue.append(i) 
			        visited[i] = True
  

# Driver code 

# Create a graph given in 
# the above diagram 
g = Graph() 
g.add_edge(0, 1) 
g.add_edge(0, 2) 
g.add_edge(1, 2) 
g.add_edge(2, 0) 
g.add_edge(2, 3) 
g.add_edge(3, 3)
g.add_edge(1, 4)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 6) 
  
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)") 
g.bfs_search(2) 