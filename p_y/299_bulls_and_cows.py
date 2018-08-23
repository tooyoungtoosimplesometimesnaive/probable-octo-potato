class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        l = len(secret)
        bull = 0
        secret_map = dict()
        for s in secret:
            if s in secret_map:
                secret_map[s] += 1
            else:
                secret_map[s] = 1

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1

            if guess[i] in secret_map:
                secret_map[guess[i]] -= 1

        unmatched_number = 0
        for key, value in secret_map.items():
            if value > 0:
                unmatched_number += value

        return str(bull) + 'A' + str(l - unmatched_number - bull) + 'B'
