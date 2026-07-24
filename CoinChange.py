class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        change = [-1] * (amount + 1)
        coins = sorted(coins)
        change[0] = 0
        for coin in coins:
            if coin <= amount:
                change[coin] = 1

        for x in range(1, amount + 1):
            temp = []
            if change[x] == 1:
                continue
            for coin in coins:
                if x - coin < 1:
                    continue
                if change[x - coin] != -1:
                    temp.append(change[x - coin] + 1)
            if temp:
                change[x] = min(temp)

        return change[amount]

