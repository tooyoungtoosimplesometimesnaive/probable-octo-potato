class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph += "."
        banned = set(banned)

        dic = {}
        current_word = ""
        most_frequency = 0
        most_frequent_word = None
        for c in paragraph:
            if not c.isalpha():
                if current_word in banned or len(current_word) == 0:
                    current_word = ""
                    continue

                if current_word in dic:
                    dic[current_word] += 1
                else:
                    dic[current_word] = 1

                if dic[current_word] > most_frequency:
                    most_frequent_word = current_word
                    most_frequency = dic[current_word]
                current_word = ""
            else:
                current_word += c.lower()

        return most_frequent_word


# take 2:
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned = set(banned)
        paragraph = re.split("[\s!?',;.]+", paragraph.lower())
        
        m = collections.defaultdict(int)
        for word in paragraph:
            if word != "" and word not in banned:
                m[word] += 1
        #print(m)
        max_freq = 0
        ans = ""
        for k, v in m.items():
            if v > max_freq:
                ans = k
                max_freq = v
        return ans
        
