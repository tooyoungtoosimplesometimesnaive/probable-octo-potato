class Solution:
    def toLowerCase(self, string):
        """
        :type str: str
        :rtype: str
        """
        return ''.join([chr(ord(i) - ord('A') + ord('a')) if i >= 'A' and i <= 'Z' else i for i in string])
        
