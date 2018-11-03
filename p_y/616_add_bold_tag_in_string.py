class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        if len(dict) == 0:
            return s

        intervals = []
        for word in dict:
            start_idx = 0
            while True:
                idx = s.find(word, start_idx)
                if idx < 0:
                    break
                start_idx = idx + 1
                intervals.append([idx, idx + len(word) - 1])
                
            for m in re.finditer(word, s):
                intervals.append([m.start(), m.start() + len(word) - 1])

        if len(intervals) == 0:
            return s
        
        intervals = sorted(intervals, key=lambda k: k[0])

        a = intervals[0]
        merged_intervals = []
        for i in range(1, len(intervals)):
            b = intervals[i]
            if a[1] < b[0] - 1:
                merged_intervals.append(a)
                a = b
            else:
                a[1] = max(a[1], b[1])
        merged_intervals.append(a)
        # print(intervals)
        # print(merged_intervals)
        
        start = 0
        result = ""
        for interval in merged_intervals:
            result += s[start:interval[0]]
            result += '<b>' + s[interval[0]:interval[1] + 1] + '</b>'
            start = interval[1] + 1
        if start < len(s):
            result += s[start:]
        return result
