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
