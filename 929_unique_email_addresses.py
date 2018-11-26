class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        email_set = set()
        for email in emails:
            local_name, domain_name = re.split('@', email)
            plus_index = local_name.find('+')
            if plus_index != -1:
                local_name = local_name[:plus_index]
            
            local_name = local_name.replace('.', '')
            email_set.add(local_name + '@' + domain_name)
        
        #print(email_set)
        return len(email_set)

