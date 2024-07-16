class Solution:
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1

        while l < r:
            # escape non alphanum  chars from left
            while l < r and not self.isAlnum(s[l]):
                l += 1
            
            # escape non alphanum chars from right
            while l < r and not self.isAlnum(s[r]):
                r -= 1

            # if not the same
            if s[l].lower() != s[r].lower():
                return False
            
            # proceed pointers
            l, r = l + 1, r - 1

        # no issues found
        return True
    
    def isAlnum(self, c):
        return (
            ord('a') <= ord(c) <= ord('z')
         or ord('A') <= ord(c) <= ord('Z')
         or ord('0') <= ord(c) <= ord('9')
        )
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome("A man, a plan, a canal: Panama"))