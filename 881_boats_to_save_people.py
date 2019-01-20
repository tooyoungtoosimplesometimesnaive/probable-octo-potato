class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        
        i = 0
        j = len(people) - 1
        result = 0
        while i < j:
            if people[j] <= limit:
                j -= 1
            if people[i] <= limit - people[j + 1]:
                i += 1
            result += 1
        
        # print(i, j)
        if j == i:
            # print('here')
            result += 1
        return result

