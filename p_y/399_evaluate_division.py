class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # print(list(zip(equations, values)))
        d = self.build_dict(equations, values)
        #print(d)
        result = []
        for [q1, q2] in queries:
            #print("q1={} q2={}".format(q1, q2))
            if q1 == q2 and q1 in d:
                result.append(1.0)
            elif q1 not in d or q2 not in d:
                result.append(-1.0)
            else:
                r = self.find(d, q1, q2, 1.0, set([]))
                #result.append(-1.0 if r == 0 else r)
                result.append(r)
        return result
    
    def find(self, d, q1, q2, current, visited):
        if q1 == q2:
            return current
        r = -1.0
        if q1 not in visited:
            visited.add(q1)
            for [edge, val] in d[q1]:
                r = self.find(d, edge, q2, current * val, visited)
                if r != -1.0:
                    break
            visited.remove(q1)
        return r

    def build_dict(self, equations, values):
        d ={}
        i = 0
        for i in range(len(equations)):
            [a, b] = equations[i]
            v = values[i]
            if a in d:
                d[a].append([b, v])
            else:
                d[a] = [[b, v]]
            if b in d:
                d[b].append([a, 1.0 / v])
            else:
                d[b] = [[a, 1.0 / v]]
        return d


