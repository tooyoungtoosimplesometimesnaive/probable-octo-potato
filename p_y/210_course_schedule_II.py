class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        indegree = [0 for i in range(numCourses)]
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for a, b in prerequisites:
            indegree[a] += 1
            graph[b].append(a)
        
        courses = [i for i in range(numCourses) if indegree[i] == 0]
        count = 0
        result = []
        while courses:
            c = courses.pop(0)
            result.append(c)
            count += 1
            for n in graph[c]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    courses.append(n)
        return [] if count != numCourses else result
