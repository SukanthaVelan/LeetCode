class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a,b = 0,len(numbers)-1
        while a < b:
            total = numbers[a]+numbers[b]
            if total == target:
                return [a+1,b+1]
            elif total < target:
                a=a+1
            else:
                b=b-1