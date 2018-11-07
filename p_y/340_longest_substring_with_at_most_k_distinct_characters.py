class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        char_map = dict()
        left = 0
        right = 0
        result = 0
        while right < len(s):
            if len(char_map) <= k:
                char_map[s[right]] = right

            if left <= right and len(char_map) > k:
                #print(char_map)
                left = min(char_map.values())
                char_map.pop(s[left])
                left += 1
                #char_map.remove(s[left])

            #print(s[left:right + 1])
            result = max(result, right - left + 1)

            right += 1
        return result

