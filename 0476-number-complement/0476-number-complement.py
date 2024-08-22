class Solution:
    def findComplement(self, num: int) -> int:
        l = []
        number = 0
        power = 0
        while num > 0:
            l.append(num%2)
            num = num //2

        
        for i in range(len(l)):
            if l[i] == 0:
                l[i] = 1
            else:
                l[i] = 0
        
        for i in range(len(l)):
            if l[(i)] == 1:
                number = number + 2**power
                
            power = power + 1
        return number