class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        curr_sum = 0
        min_length = float('inf')
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                length = right - left +1
                if length < min_length :
                    min_length = length
                curr_sum -= nums[left]
                left +=1
        if min_length == float('inf'):
            return 0
        return min_length