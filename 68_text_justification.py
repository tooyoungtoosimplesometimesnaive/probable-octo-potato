class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if len(words) == 0:
            return []
        
        result = []
        actual_len = []
        i = 0
        while i < len(words):
            current_row = []
            current_width = 0
            while i < len(words) and current_width + len(words[i]) + (1 if len(current_row) > 0 else 0) <= maxWidth:
                current_width += len(words[i]) + (1 if len(current_row) > 0 else 0)
                current_row.append(words[i])
                i += 1
            result.append(current_row)
            actual_len.append(current_width - (len(current_row) - 1))
            
        
        # print(result)
        # print(actual_len)
        
        text_result = []
        for i, row in enumerate(result):
            spaces = maxWidth - actual_len[i]
            if i == len(result) - 1:# last row should be handled separately
                text = " ".join(row)
                spaces -= len(row) - 1
                text += " " * spaces
                text_result.append(text)
            else:
                num_of_slots = len(row) - 1
                text = ""
                i = 0
                while i < len(row):
                    text += row[i]
                    i += 1
                    space = self.get_spaces(spaces, num_of_slots)
                    text += " " * space
                    spaces -= space
                    num_of_slots -= 1
                text_result.append(text)
            
        return text_result

    # if spaces = 5, slots = 3 -> 2
    #             5          2 -> 3
    def get_spaces(self, spaces, slots):
        if slots <= 0:
            return spaces
        elif spaces % slots == 0:
            return spaces // slots
        else:
            return spaces // slots + 1

