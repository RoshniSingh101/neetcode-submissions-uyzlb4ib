class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cntS, cntT = {}, {}
        for x in range(len(s)):
            cntS[s[x]] = 1 + cntS.get(s[x], 0)
            cntT[t[x]] = 1 + cntT.get(t[x], 0)
        return cntS == cntT
