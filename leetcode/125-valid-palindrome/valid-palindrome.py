class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean = []
        
        for c in s:
            if c.isalnum():
                clean.append(c.lower())
        
        clean_str = "".join(clean)
        return clean_str == clean_str[::-1]