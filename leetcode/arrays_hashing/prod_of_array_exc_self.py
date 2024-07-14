class Solution:
    def productExceptSelf(self, nums):
        products = []

        # store pre products (prefix)
        prefix = 1
        products.append(prefix)
        for i in range(1, len(nums)):
            products.append(nums[i-1] * prefix)
            prefix *= nums[i-1]
        
        # store post products (postfix)
        # update the whole product as well
        postfix = 1
        for i in range(len(nums)-2, -1, -1):
            products[i] *= nums[i+1] * postfix
            postfix *= nums[i+1]
        
        return products


if __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelf([-1,1,0,-3,3]))
        