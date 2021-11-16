# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l <= r:
            mid = (l + r) //2
            if isBadVersion(mid): #True, bad
                if not isBadVersion(mid - 1): #바로 전 False, not bad
                    return mid
                else:
                    r = mid -1
            else:
                l = mid + 1