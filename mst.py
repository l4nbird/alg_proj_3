class Graph:
    def __init__(self, num_of_nodes):
        self.m_num_of_nodes = num_of_nodes
        self.m_graph = []

    def add_edge(self, node1, node2, weight):
        self.m_graph.append([node1, node2, weight])

        # Finds the root node of a subtree containing node `i`
    def find_subtree(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_subtree(parent, parent[i])

    # Connects subtrees containing nodes `x` and `y`
    def connect_subtrees(self, parent, subtree_sizes, x, y):
        xroot = self.find_subtree(parent, x)
        yroot = self.find_subtree(parent, y)
        if subtree_sizes[xroot] < subtree_sizes[yroot]:
            parent[xroot] = yroot
        elif subtree_sizes[xroot] > subtree_sizes[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            subtree_sizes[xroot] += 1


    def kruskals_mst(self):
        # Resulting tree
        result = []
        
        # Iterator
        i = 0
        # Number of edges in MST
        e = 0

        # Sort edges by their weight
        self.m_graph = sorted(self.m_graph, key=lambda item: item[2])
        
        # Auxiliary arrays
        parent = []
        subtree_sizes = []

        # Initialize `parent` and `subtree_sizes` arrays
        for node in range(self.m_num_of_nodes):
            parent.append(node)
            subtree_sizes.append(0)

        # Important property of MSTs
        # number of egdes in a MST is 
        # equal to (m_num_of_nodes - 1)
        while e < (self.m_num_of_nodes - 1):
            # Pick an edge with the minimal weight
            node1, node2, weight = self.m_graph[i]
            i = i + 1

            x = self.find_subtree(parent, node1)
            y = self.find_subtree(parent, node2)

            if x != y:
                e = e + 1
                result.append([node1, node2, weight])
                self.connect_subtrees(parent, subtree_sizes, x, y)
        
        # Print the resulting MST
        for node1, node2, weight in result:
            print("Path: %d - %d ||Weight: %d" % (node1, node2, weight))



graphRun = Graph(9)

graphRun.add_edge(0, 1, 22)
graphRun.add_edge(0, 2, 9)
graphRun.add_edge(0, 3, 12)
graphRun.add_edge(1, 0, 22)
graphRun.add_edge(1, 2, 35)
graphRun.add_edge(1, 5, 36)
graphRun.add_edge(1, 7, 34)
graphRun.add_edge(2, 0, 9)
graphRun.add_edge(2, 1, 35)
graphRun.add_edge(2, 3, 4)
graphRun.add_edge(2, 4, 65)
graphRun.add_edge(2, 5, 42)
graphRun.add_edge(3, 0, 12)
graphRun.add_edge(3, 2, 4)
graphRun.add_edge(3, 4, 33)
graphRun.add_edge(3, 8, 30)
graphRun.add_edge(4, 2, 65)
graphRun.add_edge(4, 3, 33)
graphRun.add_edge(4, 5, 18)
graphRun.add_edge(4, 6, 23)
graphRun.add_edge(5, 1, 36)
graphRun.add_edge(5, 2, 42)
graphRun.add_edge(5, 4, 18)
graphRun.add_edge(5, 6, 39)
graphRun.add_edge(5, 7, 24)
graphRun.add_edge(6, 4, 23)
graphRun.add_edge(6, 5, 39)
graphRun.add_edge(6, 7, 25)
graphRun.add_edge(6, 8, 21)
graphRun.add_edge(7, 1, 34)
graphRun.add_edge(7, 5,24)
graphRun.add_edge(7, 6, 25)
graphRun.add_edge(7, 8, 19)
graphRun.add_edge(8, 3, 30)
graphRun.add_edge(8, 6, 21)
graphRun.add_edge(8, 7, 19)

print("Minimum Spanning Tree: ")
graphRun.kruskals_mst()
