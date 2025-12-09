class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt = 0
        prod = 1
        for i in nums:
            if i:
                prod *= i
            else:
                zero_cnt += 1
        if zero_cnt > 1:
            return [0] * len(nums)
        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_cnt:
                if c:
                    res[i] = 0
                else:
                    res[i] = prod
            else:
                res[i] = prod // c
        return res


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
