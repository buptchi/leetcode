__author__ = 'chi'


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k == 0:
            return False
        if t < 0:
            return False
        ll = len(nums)
        if ll == 1:
            return False
        if k > ll:
            k = ll

        dd = []
        dmin = nums[0]
        dmax = nums[0]

        for i in range(0, k):
            if nums[i] > dmax:
                dmax = nums[i]
            if nums[i] < dmin:
                dmin = nums[i]

            if (dmax-dmin) < t:
                dd.append(nums[i])
            else:
                return False

        for i in range(0, len(nums)-k):
            dd.append(nums[i+k])
            dmax = max(dd)
            dmin = min(dd)
            if (dmax-dmin) < t:
                dd.pop(i)
            else:
                return False

        return True

if __name__ == "__main__":

    kk = 1
    tt = 0
#    nn = [1, 3, 1, 2, 7]
    nn=[-1, -1]
    ss = Solution()
    print ss.containsNearbyAlmostDuplicate(nn, kk, tt)




























