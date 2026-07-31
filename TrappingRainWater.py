class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = []
        for i, height in enumerate(heights):
            while stack and stack[-1] <= height:
                numidx = stack.pop()
                ans = numidx 

# mono stack
# add distance between next elt that is equal or greater to the current elt to total
# add distance between elt - next elt and elt that pops - elt before * distance + 
