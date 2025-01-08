# Idea: find the MST of the full graph MST1,
# remove the one edge at a time, then find the MST,
# Which one make the MST total weight increase and appear in MST1, that one is the critical one
# If we remove an edge and still find the same weight as MST1, that's another MST for the full graph

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self,  v1):
        while v1 != self.parent[v1]:
            self.parent[v1] = self.parent[self.parent[v1]]
            v1 = self.parent[v1]
        return v1
    
    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

def kruskal_mst(edges, n):
    uf = UnionFind(n)
    mst_weight = 0
    result = []
    for a, b, weight, i in edges:
        if uf.union(a, b):
            result.append([a, b, weight, i])
            mst_weight += weight
    # if all node is not connected
    if max(uf.rank) != n:
        return [], -1
    return result, mst_weight
        
def find_critical_and_pesudo_critical_edges(edges, n):
    # keep the original index of the edges
    for i, edge in enumerate(edges):
        edge.append(i)
    
    # sort edges by the weight
    edges.sort(key=lambda e: e[2])
    
    # find the mst with the full graph
    list_edges, min_mst = kruskal_mst(edges, n)
    
    # for all edge in list_edge, try remove them and calculate the mst again
    # if it cannot connect to all node or new MST > min_mst then it is a critical edge
    # if it can create a new MST = min_mst then it is a pseudo_critical edge
    # add edge in new found mst in the list_edge
    
    criticals = []
    pseudo_critical = []
    
    observed_edge = [0 for i in range(len(edges))]
    while(len(list_edges)>0):
        edge = list_edges.pop()
        # mark as observed
        observed_edge[edge[3]] = 1
        # create a new list except this edge
        tmp_edges = []
        for element in edges:
            if element[3] != edge[3]:
                tmp_edges.append(element)
        
        tmp_list_edge, tmp_min_mst = kruskal_mst(tmp_edges, n)
        if tmp_min_mst == -1 or tmp_min_mst > min_mst:
            criticals.append(edge[3])
        
        elif tmp_min_mst == min_mst:
            pseudo_critical.append(edge[3])
            # Join tmp_list_edge and list_edge, just add the edge that doesnt appear on observed list
            
            set1 = set(tuple(x) for x in list_edges)
            tmp_list = [x for x in tmp_list_edge if observed_edge[x[3]] == 0]
            set2 = set(tuple(x) for x in tmp_list)
            list_edges = list(set1.union(set2))
    
    return criticals, pseudo_critical

edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
n = 5
print(find_critical_and_pesudo_critical_edges(edges, n))