class Solution:
    def containsDuplicate(self, nums):
        hashset = set()
        for num in nums:
            if num in hashset:
                return "true"
            else:
                hashset.add(num)
        return "false"
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.containsDuplicate([1,2,3,1]))