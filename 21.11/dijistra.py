from queue import PriorityQueue # priority queue

class MyGraph():
    def __init__(self, edge_dict: dict = {}):
        self.edge_dict = edge_dict
    
    def add_edge(self, A, B, distance):
        if A not in self.edge_dict:
            self.edge_dict[A] = [[B, distance]]
        else:
            self.edge_dict[A].append([B, distance])
            
        if B not in self.edge_dict:
            self.edge_dict[B] = [[A, distance]]
        else:
            self.edge_dict[B].append([A, distance])
    
    def dijkstra(self, source:str):
        visited_nodes = set()
        
        distances = {node: float('inf') for node in self.edge_dict}
        distances[source] = 0
        
        pri_queue = PriorityQueue()
        pri_queue.put([0, source])
        
        while pri_queue.qsize():
            distance, node = pri_queue.get()
            
            if node in visited_nodes:
                continue
            
            visited_nodes.add(node)
            
            for neighbor, distance_neighbor in self.edge_dict[node]:
                if neighbor in visited_nodes:
                    continue
                tmp = distance + distance_neighbor
                if (tmp < distances[neighbor]):
                    distances[neighbor] = tmp
                    pri_queue.put([distances[neighbor], neighbor])
        
        previous_node = {}
        
        for node in self.edge_dict:
            for neighbor, distance in self.edge_dict[node]:
                if distances[neighbor] == distances[node] + distance:
                    previous_node[neighbor] = node
            
        return distances, previous_node
    def find_shortest_path(self, source, dest):
        distances, previous_node = self.dijkstra(source)
        
        path = []
        path.append(dest)
        node = dest
        while(node != source):
            node = previous_node[node]
            path.append(node)
        path.reverse()
        return distances[dest], path
        

g = MyGraph()
g.add_edge('D', 'A', 4)  # D - A, weight 4
g.add_edge('D', 'E', 2)  # D - E, weight 2
g.add_edge('A', 'C', 3)  # A - C, weight 3
g.add_edge('A', 'E', 4)  # A - E, weight 4
g.add_edge('E', 'C', 4)  # E - C, weight 4
g.add_edge('E', 'G', 5)  # E - G, weight 5
g.add_edge('C', 'F', 5)  # C - F, weight 5
g.add_edge('C', 'B', 2)  # C - B, weight 2
g.add_edge('B', 'F', 2)  # B - F, weight 2
g.add_edge('G', 'F', 5)  # G - F, weight 5

#print(g.dijkstra('D'))
print(g.find_shortest_path('D', 'F'))