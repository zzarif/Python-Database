class Solution:
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                top, topIdx = stack.pop()
                res[topIdx] = idx - topIdx
            stack.append((temp, idx))

        return res
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73]))