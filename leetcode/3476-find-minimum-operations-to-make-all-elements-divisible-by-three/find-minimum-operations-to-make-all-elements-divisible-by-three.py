class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        add = 0

        for num in nums:
            remainder = num % 3
            if remainder != 0:
                add += 1

        return add        