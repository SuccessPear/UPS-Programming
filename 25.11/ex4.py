from collections import deque
def find_shortest_path(graph):
    # initialize to result (in this case the step)
    result = 0
    
    n = len(graph)
    
    # value inside the set and queue is in format (node, state)
    # node is in node itself
    # state is the bimask that store the visited_state like 1001, it means we have visited the 4th node and 1st node
    visited_set = set()
    queue_node = deque()
    
    # Add all the (node, state) in the set and queue
    # At this time the state of each node is all 0 except for the node
    # For example 1st node: (1, 1), 2nd node: (2, 2), 3rd node: (3, 4)
    for i in range(n):
        state = 1 << i
        visited_set.add((i, state))
        queue_node.append((i, state))
    
    while True:
        # loop through all value in queue_node, this is the step "result"
        for i in range(len(queue_node)):
            
            node, state = queue_node.popleft()
            
            # if all nodes have been visited, if n = 4 then 1111 mean all nodes are visited
            # if yes return result
            if state == (1<<n) - 1:
                return result
            
            # For each neighbor of the node
            for neighbor in graph[node]:
                # we add the neighbor to the state
                new_state = state | (1 << neighbor)
                # If the (neighbor, new_state) has not been visited, add it to the queue and set
                if (neighbor, new_state) not in visited_set:
                    visited_set.add((neighbor, new_state))
                    queue_node.append((neighbor, new_state))
        
        # increase the step
        result += 1

graph = [[1,2,3],[0],[0],[0]]
print(find_shortest_path(graph))
            