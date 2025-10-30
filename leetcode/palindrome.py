class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        reversed_x = x[::-1]
        return x == reversed_x

print(Solution().isPalindrome(121))