class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        expected = len(nums) * (len(nums) + 1) // 2
        actual = sum(nums)
        return expected - actual
        
        