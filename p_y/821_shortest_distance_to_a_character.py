class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        s_with_idx = list(zip(S, range(len(S))))
        #print(s_with_idx)
        c_idx = []
        result = [0 for i in range(len(S))]
        for i, idx in s_with_idx:
            if i == C:
                c_idx.append(idx)

        for i, idx in s_with_idx:
            #print('{}, {}'.format(i, idx))
            if i == C:
                result[idx] = 0
            else:
                #print('here')
                m = len(S) + 1
                for c_i in c_idx:
                    d = abs(idx - c_i)
                    m = min(m, d)
                result[idx] = m
        return result
    
