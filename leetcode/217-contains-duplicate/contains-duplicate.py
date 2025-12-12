class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        noDup = set(nums)

        if len(noDup) == len(nums):
            return False
        else:
            return True