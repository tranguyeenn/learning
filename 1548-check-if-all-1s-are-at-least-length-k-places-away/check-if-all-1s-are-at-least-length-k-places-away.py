class Solution(object):
    def kLengthApart(self, nums, k):
        numAparts = []

        for num in range(len(nums)):
            if nums[num] == 1:
                numAparts.append(num)

        for j in range(len(numAparts) - 1):
            if numAparts[j+1] - numAparts[j] - 1 < k:
                return False
        
        return True