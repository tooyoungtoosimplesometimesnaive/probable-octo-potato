

def dfs(nums):
    """
    @:param nums [int]
    @:return [[int]]
    """
    def dfs_helper(nums, i, current_list, res):
        if i >= len(nums):
            res.append(current_list.copy())
            return
        current_list.append(nums[i])
        dfs_helper(nums, i + 1, current_list, res)
        current_list.pop(-1)
        dfs_helper(nums, i + 1, current_list, res)

    result = []
    dfs_helper(nums, 0, [], result)

    return result


def dfs2(nums):
    def dfs2_helper(nums, start, current_list, res):
        res.append(current_list.copy())
        for i in range(start, len(nums)):
            current_list.append(nums[i])
            dfs2_helper(nums, i + 1, current_list, res)
            current_list.pop(-1)
    result = []
    dfs2_helper(nums, 0, current_list=[], res=result)
    return result


def dfs_with_dup(nums):
    """
    @:param nums [int]
    @:return [[int]]
    """
    def dfs_helper(nums, i, current_list, dedup_set, res):
        if i >= len(nums):
            res.append(current_list.copy())
            return
        if nums[i] in dedup_set:
            return
        dedup_set.add(nums[i])
        current_list.append(nums[i])
        dfs_helper(nums, i + 1, current_list, dedup_set, res)
        current_list.pop(-1)

        dedup_set.remove(nums[i])
        dfs_helper(nums, i + 1, current_list, dedup_set, res)

    result = []
    dedup_set = set()
    dfs_helper(nums, 0, [], dedup_set, result)

    return result


def find_sub_sets(nums):
    subs = {()}
    for num in nums:
        subs |= { sub + (num, )
                    for sub in subs
                }
    print(subs)

if __name__ == '__main__':
    for i in dfs([1, 2, 3, 4]):
        print(i)
    print('----')
    for i in dfs2([1, 2, 3, 4]):
        print(i)
    # for i in dfs_with_dup([1, 2, 2]):
    #     print(i)
    # find_sub_sets([1,2,2])
