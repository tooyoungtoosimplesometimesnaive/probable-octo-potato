class UnionFind:
    def __init__(self, size):
        self.ids = [i for i in range(size)]
        self.sizes = [1 for i in range(size)]
    def root(self, a):
        root = a
        while self.ids[root] != root:
            root = self.ids[root]
            
        while a != self.ids[root]:
            t = self.ids[a]
            self.ids[a] = root
            a = t
        return root
    
    def find(self, a, b):
        return self.root(a) == self.root(b)
    
    def union(self, a, b):
        root_a = self.root(a)
        root_b = self.root(b)
        
        if self.sizes[root_a] >= self.sizes[root_b]:
            self.ids[root_b] = root_a
            self.sizes[root_a] += self.sizes[root_b]
        else:
            self.ids[root_a] = root_b
            self.sizes[root_b] += self.sizes[root_a]


class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        """
        [
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["John", "johnnybravo@mail.com"],
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"], 
        ["Mary", "mary@mail.com"]
        ]
        """
        email_count = 0
        email_map = dict() # key: email, value: email number
        email_map_r = dict() # key: email number, value: email
        email_name = dict() # key: email, value: account's name
        for account in accounts:
            a_name = account[0]
            for i in range(1, len(account)):
                if account[i] not in email_map:
                    email_map[account[i]] = email_count
                    email_map_r[email_count] = account[i]
                    email_count += 1
                    email_name[account[i]] = a_name
        

        #print(email_map)
        uf = UnionFind(email_count)
        #print(uf.ids)
        
        for account in accounts:
            a_name = account[0]
            for i in range(1, len(account)):
                uf.union(email_map[account[1]], email_map[account[i]])
        
        #print(uf.ids)
        # prepare results:
        root_dict = dict() #root_id -> 
        for i in range(email_count):
            root_id = uf.root(i)
            if root_id not in root_dict:
                root_dict[root_id] = [email_name[email_map_r[i]], email_map_r[i]]
            else:
                root_dict[root_id].append(email_map_r[i])

        results = []
        for result in root_dict.values():
            emails = result[1:]
            emails.sort()
            r = [result[0]] + emails
            results.append(r)
        return results
        
