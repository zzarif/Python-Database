class Solution:
    def searchMatrix(self, matrix, target):

        # fn to search row num
        def bs_searchRow_fromMatrix(l, r):
            if l > r:
                return -1
            
            mid = l + ((r - l) // 2)

            if matrix[mid][0] <= target <= matrix[mid][m-1]:
                return mid
            elif target < matrix[mid][0]:
                return bs_searchRow_fromMatrix(l, mid-1)
            else:
                return bs_searchRow_fromMatrix(mid+1, r)
            
        # fn to do binary search on a single row
        def bs_searchElem_fromRow(nums, l, r):
            if l > r:
                return False
            
            mid = l + ((r - l) // 2)

            if target == nums[mid]:
                return True
            elif target < nums[mid]:
                return bs_searchElem_fromRow(nums, l, mid-1)
            else:
                return bs_searchElem_fromRow(nums, mid+1, r)
        

        n = len(matrix)
        m = len(matrix[0])
        row = bs_searchRow_fromMatrix(0, n-1)

        if row == -1:
            return False
        else:
            return bs_searchElem_fromRow(matrix[row], 0, m-1)
        
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))