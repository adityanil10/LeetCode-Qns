class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ''
        #creating a 2D array of dimensions len(s)*len(s) with values 0 for DP
        dp = [[0]*len(s) for _ in range(len(s))]
        #filling out diagonal by 1 since single char is palin
        for i in range(len(s)):
            dp[i][i] = True
        longest_palindrome = s[0]

        #filling the dp table
        for i in range(len(s)-1, -1, -1):
            #j starts from ith loc : to only work on upper side of diag
            for j in range(i+1,len(s)):
                if s[i] == s[j]: #if chars matches
                # if len slicied sub_string is just one letter if the characters are equal, we can say they are palindomr dp[i][j] =True 
                    #if the slicied sub_string is longer than 1, then we should check if the inner string is also palindrom (check dp[i+1][j-1] is True)
                    if j-i ==1 or dp[i+1][j-1] is True:
                        dp[i][j] = True
                        # we also need to keep track of the maximum palindrom sequence 
                        if len(longest_palindrome) < len(s[i:j+1]):
                            longest_palindrome = s[i:j+1]
                
        return longest_palindrome
