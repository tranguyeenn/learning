class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        result = []
        current = 0
        for b in nums:
            current = (current * 2 + b) % 5
            result.append(current == 0)
        return result