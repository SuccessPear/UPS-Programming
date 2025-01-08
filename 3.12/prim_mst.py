from queue import PriorityQueue

class Prim_MST:
    def __init__(self, graph: dict = {}):
        self.graph = graph
    
    def prim(self):
        n_node = len(self.graph)
        visited_node = {node: 0 for node in graph}
        
        pq = PriorityQueue()
        curr_vertex = next(iter(self.graph))
        visited_node[curr_vertex] = 1
        for neighbor, weigh in self.graph[curr_vertex]:
            pq.put((weigh, [curr_vertex, neighbor, weigh]))
        
        result = []
        sum_weigh = 0
        while(pq.qsize() > 0 and sum(visited_node.values()) < n_node):
            [curr, neighbor, weigh] = pq.get()[1]
            while(visited_node[neighbor] == 1):
                curr, neighbor, weigh = pq.get()[1]
            
            visited_node[neighbor] = 1
            sum_weigh += weigh
            result.append([curr, neighbor, weigh])
            
            for new_neighbor, new_weigh in self.graph[neighbor]:
                if visited_node[new_neighbor] != 1:
                    pq.put((new_weigh, [neighbor, new_neighbor, new_weigh]))
        
        return result, sum_weigh
            

graph = {'A': [['B', 1], ['C', 3]],
         'B': [['A', 1], ['C', 2], ['D', 4]],
         'C': [['A', 3], ['B', 2], ['D', 5]],
         'D': [['B', 4], ['C', 5]]}
prim_mst = Prim_MST(graph)
print(prim_mst.prim())