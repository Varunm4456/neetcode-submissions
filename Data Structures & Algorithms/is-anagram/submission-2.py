class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        scount = { }
        tcount = { }

        for i, j in zip(s,t):
            scount[i] = scount.get(i), 1
            tcount[j] = tcount.get(j), 1
        
        if scount != tcount:
            return False
        else:
            return True