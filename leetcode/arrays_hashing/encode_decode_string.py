class Solution:
    def encode(self, strs):
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + '#' + s
        return encoded_str

    def decode(self, s):
        if s == '':
            return []
        i = 0
        decoded_strs = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j = j + 1
            length = int(s[i:j])
            decoded_strs.append(s[j+1:j+length+1])
            i = j + length + 1
        return decoded_strs


if __name__ == "__main__":
    solution = Solution()
    print(solution.decode(solution.encode(["we","say",":","yes","!@#$%^&*()"])))
