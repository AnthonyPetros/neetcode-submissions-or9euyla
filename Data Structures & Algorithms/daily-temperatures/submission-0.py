class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            curr = temperatures[i]
            while stack and curr > stack[-1][0]:
                top, topi = stack.pop()
                res[topi] = i - topi
            stack.append((curr, i))
        return res
