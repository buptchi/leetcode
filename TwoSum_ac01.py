__author__ = 'chi'

"""
稍微看了眼思路，想出来了
根据题目特性，值是唯一的
用dict的快速查询

"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        mm = {}
        same = []
        if target % 2 == 0:
            j = 1
            for ii in nums:
                if ii == target/2:
                    same.append(j)
                j += 1
        if len(same) == 2:
            return same

        j = 1
        for ii in nums:
            mm[ii] = [target - ii, j]
            j += 1
        for ii in nums:
            if ii == target-ii:
                continue
            if mm.get(mm[ii][0]):
              return mm[ii][1], mm[mm[ii][0]][1]

if __name__ == '__main__':
    ss = Solution()
    nums = [1, 2, 3, 4, 4, 9, ]
    target = 8
    print ss.twoSum(nums, target)

















