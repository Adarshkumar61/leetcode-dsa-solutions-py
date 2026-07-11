class Solution(object):
    def pivotIndex(self, nums):
        left = 0
        total_sum = sum(nums)
        for current_element in range(len(nums)):
            right_sum = total_sum - left - nums[current_element]
            if left == right_sum:
                return current_element
            left += nums[current_element]
        return -1