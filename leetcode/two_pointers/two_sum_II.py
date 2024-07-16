class Solution:
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1

        while l < r:
            if numbers[r] > target - numbers[l]: # right num too big
                r -= 1
            elif numbers[r] < target - numbers[l]: # left num too small
                l += 1
            else: # target found
                return [l + 1, r + 1]
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([-1, 0], -1))
        