# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        binary search
        """
        first = 1
        last = n

        while first < last:
            midpoint = (first+last)/2
            if isBadVersion(midpoint) is True:
                last = midpoint
            elif isBadVersion(midpoint) is False:
                first = midpoint+1

        return first
