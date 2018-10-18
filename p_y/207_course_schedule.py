class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree = {}
        graph = {}
        for i in range(numCourses):
            indegree[i] = 0
            graph[i] = []
        
        for a, b in prerequisites:
            indegree[a] += 1
            graph[b].append(a)
        
        courses = [k for k in indegree if indegree[k] == 0]
        count = 0
        while courses:
            c = courses.pop(0)
            count += 1
            for n in graph[c]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    courses.append(n)
        return count == numCourses
        
