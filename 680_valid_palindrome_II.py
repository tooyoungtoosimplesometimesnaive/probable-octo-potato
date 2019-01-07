class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        def is_palindrome(i, j):
            return all(s[k] == s[j-k+i] for k in range(i, j))
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - i - 1]:
                j = len(s) - i - 1
                # print(s[i + 1:j + 1])
                # print(s[i:j])
                return is_palindrome(i + 1,j) or is_palindrome(i,j - 1)
        return True

