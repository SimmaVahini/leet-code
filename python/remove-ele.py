class Solution(object):
    def removeElement(self, nums, val):
        # k tracks the index for the next non-val element
        k = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                # Place the valid element at the k-th position
                nums[k] = nums[i]
                k += 1
        
        # k is now the count of elements not equal to val
        return k
