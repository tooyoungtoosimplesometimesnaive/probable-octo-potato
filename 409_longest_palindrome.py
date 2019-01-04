class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = collections.defaultdict(int)
        for c in s:
            m[c] += 1
        
        ans = 0
        has_even = False
        for v in m.values():
            ans += v // 2 * 2
            if v % 2 == 1:
                has_even = True
        
        return 1 + ans if has_even else ans
        

