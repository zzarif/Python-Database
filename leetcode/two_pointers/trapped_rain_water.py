class Solution:
    def trap(self, height):
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        trapped_water = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                trapped_water += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                trapped_water += rightMax - height[r]

        return trapped_water
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))