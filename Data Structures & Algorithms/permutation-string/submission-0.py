class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if s1 == s2:
            return True
        char1,char2 = [0]*26, [0]*26
        for c in s1:
            char1[ord(c)-ord('a')] +=1
        l,r = 0,len(s1)-1
        for i in range(len(s1)):
            char2[ord(s2[i])-ord('a')] +=1
        if char1 == char2:
            return True
        while r < len(s2)-1:
            char2[ord(s2[l])-ord('a')] -=1
            r+=1
            char2[ord(s2[r])-ord('a')] +=1
            
            l+=1
            
            if char1 == char2:
                return True
            
        return False