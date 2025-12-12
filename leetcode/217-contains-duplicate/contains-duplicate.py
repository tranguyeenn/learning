class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        noDup = set(nums)
        seen = list(noDup)

        if len(seen) == len(nums):
            return False
        else:
            return True