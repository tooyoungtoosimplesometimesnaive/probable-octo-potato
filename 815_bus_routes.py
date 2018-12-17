# TLE version, actually the set could be replaced by list.
class Solution:
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T:
            return 0
        next_stops = collections.defaultdict(set)
        
        for route in routes:
            for i in range(len(route)):
                for k in range(len(route)):
                    if k != i:
                        next_stops[route[i]].add(route[k])
                        
        #print(next_stops)
        queue = []
        visited = set()
        visited.add(S)
        for n in next_stops[S]:
            if n == T:
                return 1
            visited.add(n)
            queue.append(n)
        
        result = 1
        while queue:
            for i in range(len(queue)):
                top = queue.pop(0)
                if top == T:
                    return result
                for n in next_stops[top]:
                    if n not in visited:
                        visited.add(n)
                        queue.append(n)
            result += 1
        
        return -1

# Working solution:
class Solution:
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T:
            return 0
        graph = collections.defaultdict(set)

        routes = list(map(set, routes))
        visited = set()
        targets = set()
        queue = []
        for i in range(len(routes)):
            if S in routes[i]:  # possible starting route number
                visited.add(i)
                queue.append((i, 1))

            if T in routes[i]:  # possible ending route number
                targets.add(i)

            for j in range(i + 1, len(routes)):
                if routes[j] & routes[i]:  # set intersection to check if route_i and route_j are connected
                    graph[i].add(j)
                    graph[j].add(i)

        while queue:
            cur, count = queue.pop(0)
            if cur in targets:
                return count
            for n in graph[cur]:
                if n not in visited:
                    queue.append((n, count + 1))
                    visited.add(n)

        return -1

