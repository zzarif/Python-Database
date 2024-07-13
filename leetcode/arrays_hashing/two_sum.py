class Solution:
    def twoSum(self, nums, target):
        dict_nums = {}
        for idx, num in enumerate(nums):
            if target - num in dict_nums:
                return [dict_nums.get(target - num), idx]
            dict_nums[num] = idx



if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([3,3], 6))
    