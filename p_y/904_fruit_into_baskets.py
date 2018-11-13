class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        start = 0
        end = 0
        
        fruit_map = {}
        result = 0
        while end < len(tree):
            #print(fruit_map)
            fruit_map[tree[end]] = end

            while start < end and len(fruit_map) > 2:
                left = min(fruit_map.values())
                fruit_map.pop(tree[left])
                start = left + 1

            result = max(result, end - start + 1)
            end += 1
            
        return result

# Take 2:
class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        start = 0
        end = 0

        fruit_count = {}
        result = 0
        while end < len(tree):
            #print(fruit_count)
            if tree[end] not in fruit_count:
                fruit_count[tree[end]] = 1
            else:
                fruit_count[tree[end]] += 1

            while start < end and len(fruit_count) > 2:
                fruit_count[tree[start]] -= 1
                if fruit_count[tree[start]] == 0:
                    fruit_count.pop(tree[start])

                start += 1

            result = max(result, end - start + 1)
            end += 1
        return result

