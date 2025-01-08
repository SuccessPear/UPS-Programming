class UnionFind:
    def __init__(self, n, nodes):
        self.parent = {node: node for node in nodes}
        self.rank = {node: 1 for node in nodes}
    
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
    nodes = []
    for a, b, weight in edges:
        if a not in nodes:
            nodes.append(a)
        if b not in nodes:
            nodes.append(b)
    uf = UnionFind(n, nodes)
    mst_weight = 0
    result = []
    edges.sort(key = lambda e: e[2])
    for a, b, weight in edges:
        if uf.union(a, b):
            result.append([a, b, weight])
            mst_weight += weight
    # if all node is not connected
    if max(uf.rank.values()) != n:
        return [], -1
    return result, mst_weight

edges = [['A', 'B', 1], ['A', 'C', 5],
         ['B', 'C', 2], ['B', 'D', 4],
         ['C', 'D', 3]]

print(kruskal_mst(edges, 4))