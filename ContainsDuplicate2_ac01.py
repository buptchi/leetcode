__author__ = 'chi'


class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums, k):

        if k == 0:
            return False
        ll = len(nums)
        if k > ll:
            k = ll

        dd = {}
        for i in range(0, k):
            if dd.get(nums[i], 0) == 0:
                dd[nums[i]] = 1
            else:
                return True

        for i in range(0, len(nums)-k):
            if dd.get(nums[i+k], 0) == 0:
                dd.pop(nums[i])
                dd[nums[i+k]] = 1
            else:
                return True

        return False

if __name__ == "__main__":

    kk = 1
    nnums = [-1, -1]
    ss = Solution()
    print ss.containsDuplicate(nnums, kk)




























