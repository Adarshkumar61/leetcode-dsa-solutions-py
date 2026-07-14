class Solution(object):
    def maxSubArray(self, nums):
        curr_sum = nums[0]
        max_sum = nums[0]
        start = 0
        end = 9
        temp = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i]+ curr_sum:
                curr_sum = nums[i]
                temp = i
            else:
                curr_sum += nums[i]
            if curr_sum > max_sum:
                max_sum = curr_sum
                start = temp
                end = i

        return max_sum # nums[start:end+1]      