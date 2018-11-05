class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        workers = sorted([(w / q, q, w) for q, w in zip(quality, wage)])
        #print(workers)
        pool = []
        ans = float('inf')
        
        sumq = 0
        for ratio, q, w in workers:
            heapq.heappush(pool, -q)
            sumq += q
            
            if len(pool) > K:
                sumq += heapq.heappop(pool)
            
            if len(pool) == K:
                ans = min(ans, ratio * sumq)
        return ans

