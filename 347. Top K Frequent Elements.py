class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Dict = Counter(nums)
        bucket = [0]*(len(nums) + 1)
        for num, freq in Dict.items():
            if bucket[freq] == 0:
                bucket[freq] = []
            bucket[freq].append(num)
        res = []
        for i in range(len(nums), -1, -1):
            if bucket[i] != 0:
                res += bucket[i]
            if len(res) == k:
                return res
        return res

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        arr = []
        for num, cnt in freq.items():
            arr.append([cnt, num])
        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

class Solution(object):
    def topKFrequent(self, nums, k):
        Dict = {}
        for i in nums:
            Dict[i] = 1 + Dict.get(i, 0)
        freq = [[] for i in range(len(nums)+1)]
        for key, cnt in Dict.items():
            freq[cnt].append(key)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
