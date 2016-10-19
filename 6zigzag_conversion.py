class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) == 1:
            return s

        cur = 0
        down = True
        lists = ["" for _ in range(numRows)]
        for i in s:
            if cur == numRows-1: down = False
            elif cur == 0: down = True

            lists[cur] += i
            if down: cur+=1
            else: cur-=1

        master = ""
        for i in range(numRows):
            master +=lists[i]
        return master

if __name__ == "__main__":
    test = Solution()
    retString = test.convert("teststring", 3)
    print(retString)
