class Solution:
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        in_block = False
        result = []
        new_line = []
        for line in source:
            i = 0
            while i < len(line):
                if line[i:i+2] == '/*' and not in_block:
                    in_block = True
                    i += 1
                elif line[i:i+2] == '*/' and in_block:
                    in_block = False
                    i += 1
                elif line[i:i+ 2] == '//' and not in_block:
                    break
                elif not in_block:
                    new_line.append(line[i])
                i += 1
            if len(new_line) > 0 and not in_block:
                result.append("".join(new_line))
                new_line = []
        return result

