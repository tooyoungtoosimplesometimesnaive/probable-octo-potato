"""
class Solution {
    public int jump(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }

        int[] jumps = new int[nums.length];
        Arrays.fill(jumps, Integer.MAX_VALUE);

        jumps[0] = 0;
        for (int i = 1; i < nums.length; i ++) {
            for (int k = 0; k < i; k++) {
                if (nums[k] + k >= i) {
                    jumps[i] = Math.min(jumps[i], jumps[k] + 1);
                    break;
                }
            }
        }
        return jumps[nums.length - 1];
    }
}
"""
# Another solution:
"""
class Solution {
    public int jump(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        
        int[] jumps = new int[nums.length];
        Arrays.fill(jumps, Integer.MAX_VALUE);
        
        jumps[0] = 0;
        for (int i = 0; i < nums.length; i ++) {
            if (jumps[i] == Integer.MAX_VALUE) {
                continue;
            }
            
            for (int j = 1; i + j < nums.length && j <= nums[i]; j ++) {
                jumps[i + j] = Math.min(jumps[i + j], jumps[i] + 1);
            }
        }
        return jumps[nums.length - 1];
    }
}
"""


class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) == 0:
            return 0

        # jumps[i]: the minimum number of jumps to reach index i
        # jumps[i] = min( jumps[k] + 1 if nums[k] + k >= i )
        # k : [0, i - 1]
        jumps = [float('inf')] * len(nums)
        jumps[0] = 0
        #result = float('inf')
        for i in range(1, len(nums)):
            for k in range(i):
                if nums[k] + k >= i:
                    jumps[i] = min(jumps[i], jumps[k] + 1)
            #result = min(result, jumps[i])

        print(jumps)
        return jumps[-1]


# Another one:
class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) == 0:
            return 0

        # jumps[i]: the minimum number of jumps to reach index i
        # jumps[i] = min( jumps[k] + 1 if nums[k] + k >= i )
        # k : [0, i - 1]
        jumps = [float('inf')] * len(nums)
        jumps[0] = 0
        #result = float('inf')
        for i in range(0, len(nums)):
            if jumps[i] == float('inf'):
                continue
            k = 0
            while k + i < len(nums) and k <= nums[i]:
                jumps[i + k] = min(jumps[i + k], jumps[i] + 1)
                k += 1

        #print(jumps)
        return jumps[-1]

