class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x<0:
            return False
        
        z = x
        y = 0
        while x > 0:
            y = 10*y + x%10
            x /= 10
            
        if y == z:
            return True
        return False