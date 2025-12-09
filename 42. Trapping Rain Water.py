class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        l, r = 0, len(height) - 1
        lmax, rmax = 0, height[r]
        while l < r:
            if height[l] <= height[r]:
                if height[l] < lmax:
                    total += lmax - height[l]
                else:
                    lmax = height[l]
                l+=1
            else:
                if height[r] < rmax:
                    total += rmax - height[r]
                else:
                    rmax = height[r]
                r -= 1
        return total
