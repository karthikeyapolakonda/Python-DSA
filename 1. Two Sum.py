class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Hash = {} #val->idx
        for i in range(len(nums)):
            Hash[nums[i]] = i
        for i, n in enumerate(nums):
            diff = target - n
            if diff in Hash and i != Hash[diff]:
                return [i, Hash[diff]]
        return []

  class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])
        A.sort()
        l, r = 0, len(nums)-1
        while l < r:
            curr = A[l][0] + A[r][0]
            if curr == target:
                return [min(A[l][1], A[r][1]), max(A[l][1], A[r][1])]
            elif curr > target:
                r -= 1
            else:
                l += 1
        return []
