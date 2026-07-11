class Solution(object):
    def twoSum(self, nums, target):
        
        hashmap = {}
        for i in range(len(nums)):
            required = target - nums[i]
            if required in hashmap:
                return [hashmap[required], i]
            hashmap[nums[i]] = i
        return []