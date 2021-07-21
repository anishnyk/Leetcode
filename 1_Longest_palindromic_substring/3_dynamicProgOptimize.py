class Solution(object):
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        pal = ""
        
        #xrange faster than range
        #max function to compare length of 2 strings
        for i in xrange(len(s)):
        
            #Longest palindrome starting from single letter
            mPal = self.maxPal(s, i, i)
            pal = max(pal, mPal, key=len)
                
            #longest palindrome starting from double letter word    
            mPal = self.maxPal(s, i, i+1)
            pal = max(pal, mPal, key=len)
            
        return pal
        
    def maxPal(self, s, i, j):
        while i>=0 and j<len(s) and s[i]==s[j]:
            i -= 1
            j += 1
        
        return s[i+1:j]
        
        
       