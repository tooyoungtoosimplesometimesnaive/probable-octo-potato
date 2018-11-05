class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        slow = 0
        fast = 0
        substr_set = set()
        max_len = 0
        # s = list(s)
        while fast < len(s):
            #print("slow={}, s[slow]={}, fast={}, s[fast]={}, set={}".format(slow,s[slow], fast, s[fast], substr_set))
            if s[fast] in substr_set:
                while s[fast] in substr_set:
                    #print("here")
                    substr_set.remove(s[slow])
                    slow += 1

            substr_set.add(s[fast])
            fast += 1
            if fast - slow > max_len:
                max_len = fast - slow
        return max_len


# Take 2
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_map = set()

        start = 0
        end = 0
        result = 0
        while start < len(s) and end < len(s):
            # move the two pointers to a stable state
            while start <= end and s[end] in char_map:
                char_map.remove(s[start])
                start += 1

            char_map.add(s[end])

            # do calculation
            result = max(result, end - start + 1)
            end += 1

        return result

