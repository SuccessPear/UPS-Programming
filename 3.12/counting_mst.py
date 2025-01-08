import math
import numpy as np

class CountingMST:
    def __init__(self, graph: dict = {}, mode = 'non-complete'):
        self.graph = graph
        self.mode = mode
    
    def count_mst_complete(self):
        # For a complete graph, total of MST is calculate as follow:
        # T = n^(n-2) with n is the number of nodes
        n = len(self.graph)
        return math.pow(n, n-2)
    
    def count_mst_non_complete(self):
        n = len(self.graph)
        A = [[0]*n for i in range(n)]
        
        for key, edges in self.graph.items():
            key = ord(key) - ord('A')
            A[key][key] = len(edges)
            for node in edges:
                node = ord(node) - ord('A')
                A[key][node] = 1
        
        for i in range(n):
            for j in range(n):
                if i != j and A[i][j] == 1:
                    A[i][j] = -1
        
        # remove the first row and column
        A = np.array(A)
        cofact = A[1:,1:]
        return round(np.linalg.det(cofact))
    
    def count_mst(self):
        if self.mode == 'non-complete':
            return self.count_mst_non_complete()
        else:
            return self.count_mst_complete()

graph = {'A': ['B', 'C', 'D'],
         'B': ['A'],
         'C': ['A', 'D'],
         'D': ['A', 'C']}

count_mst = CountingMST(graph)
print(count_mst.count_mst())