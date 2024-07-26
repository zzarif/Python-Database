class Solution:
    def largestRectangleArea(self, heights):
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                maxArea = max(maxArea, height * (i - idx))
                start = idx
            stack.append((start, h))
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
            
        return maxArea
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.largestRectangleArea(heights = [2,1,5,6,2,3]))