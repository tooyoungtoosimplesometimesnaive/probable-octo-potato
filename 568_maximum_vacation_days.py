class Solution(object):
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        city_num = len(flights)
        week_num = len(days[0])
        
        # dp[i][j] -> max days for city i and week j
        # dp[i][j] = max(
        #               dp[i][j - 1] + days[i][j] (stays at city i)
        #               dp[c][j - 1] + days[i][j] (from other city)
        #            )
        dp = [[-1 for _ in range(week_num)] for _ in range(city_num)]
        dp[0][0] = days[0][0]
        result = dp[0][0]

        for city in range(1, city_num):
            if flights[0][city]:
                dp[city][0] = days[city][0]
                result = max(result, dp[city][0])
            else:
                dp[city][0] = -1

        for week in range(1, week_num):
            for city in range(city_num):
                for other_city in range(city_num):
                    if dp[other_city][week - 1] != -1 and (other_city == city or flights[other_city][city]):
                        dp[city][week] = max(dp[city][week], days[city][week] + dp[other_city][week - 1])
                
                # dp[city][week] = max(dp[city][week], days[city][week] + dp[city][week - 1])

                result = max(result, dp[city][week])
        
        return result

