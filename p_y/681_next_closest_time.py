class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        l = []
        l.append(int(time[0]))
        l.append(int(time[1]))
        l.append(int(time[3]))
        l.append(int(time[4]))
        res_set = []
        self.get_all_possible(l, [], res_set)
        mini = 20000
        res = l
        for t in res_set:
            diff = self.do_compare(l, t)
            if diff > 0 and diff < mini:
                mini = diff
                res = t
        return str(res[0]) + str(res[1]) + ":" + str(res[2]) + str(res[3])
            

    # time1 and time2 are arrs
    # return time2 - time1
    def do_compare(self, time1, time2):
        hour_1 = time1[0] * 10 + time1[1]
        hour_2 = time2[0] * 10 + time2[1]
        min_1 = time1[2] * 10 + time1[3]
        min_2 = time2[2] * 10 + time2[3]
        
        is_next_day = hour_1 * 100 + min_1 > hour_2 * 100 + min_2
        if is_next_day:
            return hour_2 * 60 + min_2 + 3600 - (hour_1 * 60 + min_1)
        else:
            return hour_2 * 60 + min_2 - (hour_1 * 60 + min_1)

    def get_all_possible(self, arr, current, res):
        if len(current) == 4:
            res.append(current.copy())
            return
    
        for i in arr:
            current.append(i)
            if self.is_valid_time(current):
                self.get_all_possible(arr, current, res)
            current.pop(-1)

    # time is arr
    def is_valid_time(self, time):
        if len(time) == 1:
            return time[0] <= 2
        elif len(time) == 2:
            return time[0] * 10 + time[1] <= 23
        elif len(time) == 3:
            return time[0] * 10 + time[1] <= 23 and time[2] <= 5
        elif len(time) == 4:
            return time[0] * 10 + time[1] <= 23 and time[2] * 10 + time[3] <= 59
        else:
            return False


# Take 2:
class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        if time == "00:00":
            return time

        result = []
        time = time[0:2] + time[3:]
        self.get_all(time, 0, "", result)
        #print(result)
        min_diff = float('inf')
        closest_time = time
        time_num = self.to_time(time)
        for r in result:
            if r == time:
                continue
            if self.calc_diff(self.to_time(r), time_num) < min_diff:
                min_diff = self.calc_diff(self.to_time(r), time_num)
                closest_time = r

        return closest_time[:2] + ":" + closest_time[2:]

    def get_all(self, time, i, current, result):
        if i == 4:
            result.append(current)
            return

        for a in time:
            c = current + a
            if len(c) == 2 and int(c) > 23:
                continue
            if len(c) == 4 and int(c[2:]) > 59:
                continue
            self.get_all(time, i + 1, c, result)

    def to_time(self, time):
        return int(time[0:2]) * 60 + int(time[2:])

    def calc_diff(self, time_1, time_2):
        # calc time_1 - time_2:
        # always assume time_1 is later than time_2
        # (so that the answer should always be positive)
        if time_1 > time_2:
            return time_1 - time_2
        else:
            return 24 * 60 + time_1 - time_2

