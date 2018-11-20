class Solution:
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = [0] * 26
        start = 0
        max_count = 0
        max_length = 0
        for end in range(len(s)):
            count[ord(s[end]) - ord('A')] += 1
            max_count = max(max_count, count[ord(s[end]) - ord('A')])
            while end - start + 1 - max_count > k:
                count[ord(s[start]) - ord('A')] -= 1
                start += 1
            max_length = max(max_length, end - start + 1)
        return max_length

