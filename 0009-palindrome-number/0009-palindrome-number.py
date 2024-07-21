class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        num = x
        check = 0
        while num!=0:
            check = check*10+(num%10)
            num=(num-(num%10))//10
        return check == x