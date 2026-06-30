class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        highestafter = prices[0]
        max = 0
        for day in range(0, len(prices)):
            if(lowest > prices[day]):
                lowest = prices[day]
                highestafter = prices[day]
            if(prices[day] > highestafter):
                highestafter = prices[day]
                if(max < (highestafter - lowest)):
                    max = highestafter - lowest
        return max
