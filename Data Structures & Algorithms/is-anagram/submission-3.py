class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sSet, tSet = [0] * 26, [0] * 26
        for i in range (0,len(s)):
            sSet[ord(s[i]) - ord('a')] += 1
            tSet[ord(t[i]) - ord('a')] += 1
        if sSet == tSet:
            return True
        return False