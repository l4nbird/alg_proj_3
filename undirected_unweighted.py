# Algorithms
# Landon Bird

# import random

class Vertex:
  def __init__(self,name):
    self.name = name
    self.neighbors = set()

  def add_neighbor(self, v):
    if v not in self.neighbors:
      self.neighbors = self.neighbors | {v}

class Graph:
  graph = dict()

  def add_vertex(self, vertex):
    if isinstance(vertex, Vertex) and \
      vertex.name not in self.graph:
        self.graph[vertex.name] = vertex

  def add_edge(self, u, v):
    if u in self.graph and v in self.graph:
      for key, value in self.graph.items():
        if key == u:
          value.add_neighbor(v)
        if key == v:
          value.add_neighbor(u)

  def print_graph(self):
    for key in sorted(list(self.graph.keys())):
      print(str(key) + str(self.graph[key].neighbors))

def dfs(graph, start, goal):
  stack = [(start, [start])]
  visited = set()
  while stack:
    (vertex, path) = stack.pop()
    if vertex not in visited:
      if vertex == goal:
        return path
      visited.add(vertex)
      for neighbor in graph[vertex].neighbors:
        stack.append((neighbor, path + [neighbor]))
  if list(path)[-1] != goal:
    print("Goal is not connected to start --> No Path")
    return None

def bfs(graph, start, goal):
  visited, queue = set(), [start]
  p = []
  while queue:
    vertex = queue.pop(0)
    if vertex not in visited:
      visited.add(vertex)
      p.append(vertex)
      if vertex == goal:
        return p
      queue.extend(graph[vertex].neighbors - visited)
  if p[-1] != goal:
    print("Goal is not connected to start --> No Path")
    return None

def main():
  letters = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'}
  g = Graph()
  for i in letters:
    g.add_vertex(Vertex(str(i)))
  edges = ['AB', 'AF', 'AE', 'BC', 'CD', 'CG', 'DG', 'EF', 'EI', 'FI', 'IJ', 'IM', 'GJ', 'MN', 'HK', 'HL', 'KL', 'KO', 'LP']
  for edge in edges:
    g.add_edge(edge[:1], edge[1:])
  g.print_graph()
  
  path = dfs(g.graph, 'A', 'M')
  if path:
    print("DFS:")
    print(list(path))

  path2 = bfs(g.graph, 'A', 'M')
  if path2:
    print("BFS:")
    print(list(path2))

main()