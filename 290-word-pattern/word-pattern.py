class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        uni_p = []
        uni_s = []
        for char in pattern:
            if char not in uni_p:
                uni_p=uni_p + [char]
        for word in s.split(" "):
            if word not in uni_s:
                uni_s=uni_s + [word]
        
        if len(uni_p) == len(uni_s):
            map_dict = {}
            for i in range(len(uni_p)):
                map_dict[uni_s[i]] = uni_p[i]
            
            new_p = ""
            for s in s.split(" "):
                new_p = new_p + map_dict[s]
            
            if new_p == pattern:
                return True
        
        return False
