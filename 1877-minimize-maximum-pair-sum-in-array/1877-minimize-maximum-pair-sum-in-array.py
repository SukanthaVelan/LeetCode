class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        l = []
        nums.sort()
        for i in range (len(nums)//2):
            l.append(nums[i]+nums[-(i+1)])
        return max(l)
            