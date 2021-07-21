class Solution(object):

    #Works O(n3) - extremely slow
    #Try to create O(n2)
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if isPal(s):
            return s
        for i in range(len(s)-1,1,-1):
            for j in range(len(s)-i+1):
                if isPal(s[j:j+i]):
                    return s[j:j+i]
        
        return s[0]
        
    
def isPal(s):
        if len(s) == 1:
            return True
        i = 0
        while i < len(s)//2:
            if s[i] != s[len(s)-i-1]:
                return False
            i+=1
            
        return True