class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        
        result = collections.defaultdict(int)
        for s in cpdomains:
            num, domain = s.split(" ")
            num = int(num)
            result[domain] += num
            for i, itr in enumerate(domain):
                if itr == '.':
                    #print(i)
                    result[domain[i + 1:]] += num
        
        def transform(t):
            a, b = t
            return str(b) + " " + a
        

        return map(transform, result.items())
        
