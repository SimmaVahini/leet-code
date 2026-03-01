class Solution:
    def twoSum(self, nums, target):
        lookup = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in lookup:
                return [lookup[complement], i]
            lookup[nums[i]] = i
