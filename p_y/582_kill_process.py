class Solution:
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        tree = collections.defaultdict(list)
        for child, parent in zip(pid, ppid):
            #print("child={}, parent={}".format(child, parent))
            tree[parent].append(child)
        #print(tree)
        q = []
        q.extend(tree[kill])
        result = []
        while len(q) != 0:
            a = q[0]
            q.pop(0)
            result.append(a)
            if a in tree:
                q.extend(tree[a])
        
        result.append(kill)
        return result

        
      
