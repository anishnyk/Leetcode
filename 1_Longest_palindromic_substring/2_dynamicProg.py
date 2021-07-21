class Solution(object):
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        pal = s[0]
        for i in range(len(s)):
        
            #Longest palindrome starting from single letter
            mPal = self.maxPal(s, i, i)
            # print mPal
            if len(mPal)>len(pal):
                pal=mPal
                
            #longest palindrome starting from double letter word    
            mPal = self.maxPal(s, i, i+1)
            # print mPal
            if len(mPal)>len(pal):
                pal=mPal    
            # print 'pal='+pal
            
        return pal
        
    def maxPal(self, s, i, j):
        while i>=0 and j<len(s) and s[i]==s[j]:
            i -= 1
            j += 1
        
        return s[i+1:j]
        
        
       