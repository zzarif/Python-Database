class Solution:
    def generateParenthesis(self, n):
        res = []

        def backtrack(combination, openN, closedN):
            # base condition
            if openN == closedN == n:
                res.append(combination)
                return
            
            # if '(' can be added
            if openN < n:
                backtrack(combination+'(', openN+1, closedN)
            
            # if ')' can be added
            if closedN < openN:
                backtrack(combination+')', openN, closedN+1)

        backtrack("", 0, 0)
        return res
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.generateParenthesis(5))