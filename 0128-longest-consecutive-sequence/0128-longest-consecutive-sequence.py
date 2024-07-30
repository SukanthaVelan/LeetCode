class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums = list(set(nums))
        nums.sort()
        
        print(nums)
        total = 1
        counter = 1
        for i in range (len(nums)-1):
            if nums[i] == nums[i+1]-1:
                counter = counter +1
                print(counter)
            elif counter >= total:
                total = counter 
                counter = 1
            else:
                counter = 1
        if counter > total:
            return counter
        else:
            return total
            
                