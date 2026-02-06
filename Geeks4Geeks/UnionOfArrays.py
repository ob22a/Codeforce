class Solution:    
    def findUnion(self, a, b):
        unique = set([*a,*b])
        return list(unique)
