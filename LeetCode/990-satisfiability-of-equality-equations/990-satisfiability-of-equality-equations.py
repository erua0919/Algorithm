class UnionFind:
    def __init__(self):
        self.parent = [i for i in range(26)]
    
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
    
    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:return True
        if pa != pb:
            self.parent[pb] = pa
        return True


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equal = []
        notequal = []
        uf = UnionFind()
        for q in equations:
            a,op1,op2,b = q[0], q[1],q[2],q[3]
            if op1 == '=':
                equal.append((a, op1, op2, b))
                uf.union(ord(a) - ord('a'), ord(b) - ord('a'))
            elif op1 == '!':
                notequal.append((a, op1, op2, b))
        
        for a, op1, op2, b in notequal:
            
            pa = uf.find(ord(a) - ord('a'))
            pb = uf.find(ord(b) - ord('a'))
            if pa == pb:return False
        return True