# Idea: Dijkstra algorithm, we find the shortest path from node K to all other Node.
# Return the largest distance, if it is inf (cant reach some nodes) then return -1
# First we need to create a relative dictionary to store all the route of one node its neighbor
# This is one side route

# Use PriorityQueue to reduce time to find the smallest distance
from queue import PriorityQueue

# Create the neighbor dictionary from the input times
def create_neighbor_dict(times, N):
    neighbor_dict = {}
    for i in range(N):
        neighbor_dict[i] = []
        
    for [source, dest, weigh] in times:
        neighbor_dict[source-1].append([dest-1, weigh])
    return neighbor_dict
    
def find_signal_tranmission_time(times, N, source):
    # Transform to 0-index
    source -= 1
    
    neighbor_dict = create_neighbor_dict(times, N)

    visited_nodes = set()
    
    # Initialize all distance as infinite except the source
    distances = {node: float('inf') for node in range(N)}
    distances[source] = 0
    
    # push source to priority queue with distance = 0
    pri_queue = PriorityQueue()
    pri_queue.put([0, source])
    
    while pri_queue.qsize():
        distance, node = pri_queue.get()
        
        if node in visited_nodes:
            continue
        
        visited_nodes.add(node)
        
        for neighbor, distance_neighbor in neighbor_dict[node]:
            if neighbor in visited_nodes:
                continue
            tmp = distance + distance_neighbor
            if (tmp < distances[neighbor]):
                distances[neighbor] = tmp
                pri_queue.put([distances[neighbor], neighbor])
    
    # After getting the shortest distances from source to all other node
    # Find the largest, inf means this node can't be reach from source
    _, max_distance = max(distances.items())
    if (max_distance == float('inf')):
        return -1
    return max_distance

times = [[2,1,1],[2,3,1],[3,4,1]]
N = 4
K = 2

print(find_signal_tranmission_time(times, N, K))