class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        # graph[i][j] -> cost from i to j, 0 if no edge exists
        graph = [[0 for _ in range(n)] for _ in range(n)]
        for s, d, cost in flights:
            graph[s][d] = cost
        
        cost = [float('inf') for _ in range(n)]
        stop = [float('inf') for _ in range(n)]
        
        pool = []
        heapq.heappush(pool, (0, src, 0)) # (accumulated cost, src, stop used)

        while len(pool):
            current_cost, head, stop_used = heapq.heappop(pool)
            
            if head == dst:
                return current_cost
            if stop_used > K:
                continue
            for i in range(n):
                if graph[head][i] == 0: continue
                next_cost = current_cost + graph[head][i]
                if next_cost < cost[i]:
                    cost[i] = next_cost
                    heapq.heappush(pool, (next_cost, i, stop_used + 1))
                elif stop_used + 1 < stop[i]:
                    stop[i] = stop_used + 1
                    heapq.heappush(pool, (next_cost, i, stop_used + 1))
         
        return -1
# Other:
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        # graph[i][j] -> cost from i to j, 0 if no edge exists
        graph = [[0 for _ in range(n)] for _ in range(n)]
        for s, d, cost in flights:
            graph[s][d] = cost

        pool = []
        heapq.heappush(pool, (0, src, 0)) # (accumulated cost, src, stop used)

        while len(pool):
            current_cost, head, stop_used = heapq.heappop(pool)

            if head == dst:
                return current_cost
            if stop_used > K:
                continue
            for i in range(n):
                if graph[head][i] == 0: continue
                next_cost = current_cost + graph[head][i]
                heapq.heappush(pool, (next_cost, i, stop_used + 1))

        return -1

