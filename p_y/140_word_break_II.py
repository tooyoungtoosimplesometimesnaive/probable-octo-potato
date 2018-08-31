class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        word_dict = set(wordDict)
        if not self.can(s, word_dict):
            return []

        result = []
        self.helper(s, word_dict, 0, [], result)
        return result
    def can(self, s, word_dict):
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

    def helper(self, s, word_dict, last_idx, current_row, result):
        if last_idx >= len(s):
            result.append(' '.join(current_row))
            return
        
        i = last_idx
        while i < len(s):
            if s[last_idx:i + 1] in word_dict:
                current_row.append(s[last_idx:i + 1])
                self.helper(s, word_dict, i + 1, current_row, result)
                current_row.pop(-1)
            i += 1

                
        
