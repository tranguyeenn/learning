class Solution(object):
    def twoSum(self, nums, target):
        for index in range(len(nums)):
            for jindex in range(index + 1, len(nums)):
                if nums[index] + nums[jindex] == target:
                    return(index, jindex)
        
print(Solution().twoSum([2,7,11,15], 9))

    
    