class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = {}
        for i, j in enumerate(nums):
            if target-j in table:
                return [table[target-j], i]
            table[j] = i
        return []

if __name__ == "__main__":
    test = Solution()
    retArray = test.twoSum([3,5,6,1], 7)
    print(retArray)
