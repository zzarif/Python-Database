class Solution:
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            curr_area = min(height[l], height[r]) * (r - l)
            
            if curr_area > max_area:
                max_area = curr_area
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_area
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxArea([1,8,6,2,5,4,8,3,7]))