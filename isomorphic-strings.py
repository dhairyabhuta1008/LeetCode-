class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        w = set()
        for c,i in enumerate(s):
            try:
                if(t[c] != dic[i]):
                    return False
            except:
                l = len(w)
                w.add(t[c])
                k = len(w)
                if(l == k):
                    return False
                else:
                    dic[i] = t[c]
        return True