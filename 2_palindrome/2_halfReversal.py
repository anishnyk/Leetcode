class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        # negative and multiples of 10 are automatically not palindromes
        if x<0 or (x%10==0 and x!= 0):
            return False
        
        # Half reversals for faster processing
        y = 0
        while x > y:
            y = 10*y + x%10
            x /= 10
            # print x,y
            
        return x == y or x == y/10