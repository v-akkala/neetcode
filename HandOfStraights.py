class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        i = 0
        while hand:
            num = hand[0]
            for j in range(groupSize):
                if num + j in hand:
                    hand.pop(hand.index(num + j))
                else:
                    return False
        return True
