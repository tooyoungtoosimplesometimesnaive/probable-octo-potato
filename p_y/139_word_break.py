class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_dict = set(wordDict)
        can_break = [False for i in range(len(s) + 1)]
        can_break[0] = True
        
        i = 0
        while i < len(s):
            j = i
            while j >= 0:
                if s[j: i + 1] in word_dict:
                    if can_break[j]:
                        can_break[i + 1] = True
                        j -= 1
                        continue
                    else:
                        j -= 1
                        continue
                j -= 1
            i += 1
            
        return can_break[-1]

# Take 2:
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if s == None:
            return False
        if len(s) == 0:
            return True

        word_dict = set(wordDict)
        can_break = [False] * (len(s) + 1)
        can_break[0] = True

        for i in range(len(s) + 1):
            if s[:i] in word_dict:
                can_break[i] = True
            for j in range(i):
                if can_break[j] and s[j:i] in word_dict:
                    can_break[i] = True
        #print(can_break)
        return can_break[-1]

