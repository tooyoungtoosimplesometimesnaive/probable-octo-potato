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

                
        
# Take 2: DP:
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if s == None or len(s) == 0:
            return []

        word_dict = set(wordDict)

        # can_break[i] from 0 to i, can break or not. so can_break[0] (0 to 0 , empty string) is true,
        can_break = [False] * (len(s) + 1)
        can_break[0] = True

        back_index = [[] for _ in range(len(s) + 1)]

        for i in range(len(s) + 1):
            if s[:i] in word_dict:
                can_break[i] = True
                # DO NOT add here
                # back_index[i].append(0)

            for j in range(i):
                if can_break[j] and s[j:i] in word_dict:
                    can_break[i] = True
                    back_index[i].append(j)

        # print(can_break)
        if not can_break[-1]:
            return []
        result = []
        self.construct_ans(s, back_index, len(s), [], result)
        # print(back_index)
        # print(result)
        return list(map(lambda k: " ".join(k), result))

    def construct_ans(self, s, back_index, index, curr_result, result):
        if index == 0:
            result.append(curr_result.copy())
        for start in back_index[index]:
            curr_result.insert(0, s[start:index])
            self.construct_ans(s, back_index, start, curr_result, result)
            curr_result.pop(0)

