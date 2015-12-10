__author__ = 'chi'


# best time to buy and sell stock 2
# it is about analyze
"""
class Solution:
  # @param prices, a list of integer
  # @return an integer
  def maxProfit(self, prices):
    ans = 0
    for i in range(0,len(prices)-1):
      if (prices[i+1]-prices[i]>0):
        ans = ans + prices[i+1]-prices[i]
    return ans

"""


# divide to small problem
# record temp result

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxprofit(self, prices):
        if len(prices) == 0:
            return 0
        maxprice = prices[-1]
        ans = 0
        for i in range(len(prices)-1, -1, -1):
            maxprice = max(maxprice, prices[i])
            ans = max(ans, maxprice - prices[i])

        return ans


if __name__ == "__main__":

    ll = [1, 4, 3, 5, 9, 6]
    sol = Solution()
    an = sol.maxprofit(ll)
    print(an)
