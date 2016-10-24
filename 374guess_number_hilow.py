# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher,
# otherwise return 0
# def guess(num):


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n

        while start <= end:
            midpoint = (start+end)/2
            guess_result = guess(midpoint)
            if guess_result is 0:
                return midpoint
            elif guess_result is -1:
                end = midpoint-1
            else:
                start = midpoint+1
        return -1
