class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = l + (r - l) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in nums:
            if nums[len(nums)-1]>nums[0]:
                return nums[0]
            temp = nums.pop(0)
            nums.append(temp)
        return nums[0]
