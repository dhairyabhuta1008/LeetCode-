class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if(len(s)>len(t)):
            return False
        if(len(s)==0):
            return True
        for i in range(0,len(t)):
            if(t[i]==s[0]):
                return self.isSubsequence(s[1:],t[i+1:])
        return False