class Solution:
    def reverse(self, x: int) -> int:
        n = x
        r = 0
        if n<0:
            n=n*-1
        while(n>0):
            temp = (n%10)
            r = r*10+temp
            n = (n-temp)/10
        if (r < (-2)**31 or r > (2**31)-1):
            return 0 
        if x>0:
            return int(r)
        else:
            return -int(r)
            
        