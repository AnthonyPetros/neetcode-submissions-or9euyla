class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        res = min(heights[l],heights[r]) * (r-l)
        while l<r:
            if heights[l] <= heights[r]:
                l +=1
            elif heights[l] > heights[r]:
                r -=1
            
            curr = min(heights[l],heights[r]) * (r-l)
            res = max(res,curr)
        return res