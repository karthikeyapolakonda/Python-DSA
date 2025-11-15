class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curr_sum = 0
        for n in nums:
            curr_sum = max(curr_sum, 0)
            curr_sum += n
            res = max(curr_sum, res)
        return res
#or
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        max_sum = nums[0]
        for n in nums[1:]:
            if curr_sum < 0:
                curr_sum = n
            else:
                curr_sum = curr_sum + n
            max_sum = max(max_sum, curr_sum)
        return max_sum
