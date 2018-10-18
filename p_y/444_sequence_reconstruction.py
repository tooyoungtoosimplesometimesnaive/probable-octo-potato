class Solution:
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        graph = {}
        indegree = {}
        dedup_set = set()
        for l in seqs:
            if len(l) == 0:
                continue
            if len(l) == 1:
                if l[0] not in graph:
                    graph[l[0]] = []
                if l[0] not in indegree:
                    indegree[l[0]] = 0
                continue
            i, j = 0, 1
            while j < len(l):
                if l[i] not in graph:
                    graph[l[i]] = []
                if l[j] not in graph:
                    graph[l[j]] = []
                if l[i] not in indegree:
                    indegree[l[i]] = 0
                if l[j] not in indegree:
                    indegree[l[j]] = 0
                if (l[i], l[j]) in dedup_set:
                    i += 1
                    j += 1
                    continue
                dedup_set.add((l[i], l[j]))
                graph[l[i]].append(l[j])
                indegree[l[j]] += 1
                i += 1
                j += 1
        print(indegree)
        if len(org) != len(indegree):
            return False
        starts = [k for k in indegree if indegree[k] == 0]
        org_idx = 0
        while starts and org_idx < len(org):
            if len(starts) > 1:
                return False
            top = starts.pop(0)
            if top != org[org_idx]:
                return False
            org_idx += 1
            for top_n in graph[top]:
                indegree[top_n] -= 1
                if indegree[top_n] == 0:
                    starts.append(top_n)
        print(org_idx)
        return org_idx == len(org)
                
