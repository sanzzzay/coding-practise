class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_number = prices[0]
        max_diff = 0
        for i in range(1, len(prices)):
            # get the minimum value
            if prices[i] < min_number:
                min_number = prices[i]
            # get the maximum difference among the elements minus minimum value
            if max_diff < prices[i] - min_number:
                max_diff = prices[i] - min_number
        print(min_number, max_diff)
        return max_diff