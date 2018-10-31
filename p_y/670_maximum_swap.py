class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_list = [i for i in str(num)]
        last_occur = {x: i for i, x in enumerate(num_list)}
#         print(num_list)
#         print(last_occur)
        
        for i, n in enumerate(num_list):
            for p in range(9, int(n), -1):
                if str(p) in last_occur and last_occur[str(p)] > i:
                    num_list[last_occur[str(p)]], num_list[i] = num_list[i], num_list[last_occur[str(p)]]
                    return int("".join(num_list))
        return num

