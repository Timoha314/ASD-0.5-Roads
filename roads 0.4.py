class UnionFind:
    def __init__(self, n):
        self.size = [1 for _ in range(n)]
        self.parent = [i for i in range(n)]
        self.components = n

    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.size[root_u] < self.size[root_v]:
                root_u, root_v = root_v, root_u
            self.parent[root_v] = root_u
            self.size[root_u] += self.size[root_v]
            self.components -= 1


with open('input.txt', 'r') as file:
    with open('output.txt', 'w') as output_file:
        n, q = map(int, file.readline().split())
        uf = UnionFind(n)
        results = []
        for _ in range(q):
            u, v = map(int, file.readline().split())
            uf.union(u - 1, v - 1)
            results.append(uf.components)
        output_file.write('\n'.join(map(str, results)) + '\n')
