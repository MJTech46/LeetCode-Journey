class Solution:
    def reverse(self, x: int) -> int:
        neg_limt=0-2**(31)
        pos_limt=2**(31)-1
        if neg_limt<=x and x<=pos_limt: 
            if x>=0: x=int(str(x)[::-1])
            else: x=0-int(str(x)[:0:-1])
            return x if neg_limt<=x and x<=pos_limt else 0
        else: return 0