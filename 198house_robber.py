class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        memo = [nums[0], max(nums[0], nums[1])]

        if len(nums) == 2:
            return memo[1]

        for i in range(2, len(nums)):
            memo.append(max(memo[i-2] + nums[i], memo[i-1]))

        return memo[len(nums)-1]
