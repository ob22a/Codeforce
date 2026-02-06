class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        map1 = {}
        map2 = {}
        
        n1 = len(a)
        n2 = len(b)
        
        if(n1!=n2): return False
        
        for num in a: map1[num] = map1.get(num, 0)+1
        for num in b: map2[num] = map2.get(num,0)+1
        
        return map1==map2
