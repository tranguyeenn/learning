class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        first = nums[:n]
        second = nums[n:]
        result = []
        
        for i in range(n):
            result.append(first[i])
            result.append(second[i])
        
        return result