class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        l = 0
        r = len(heights)-1

        while l < r:
            width = r-l
            current_height = min(heights[l] , heights[r])
            current_area = width * current_height
            maxarea = max(maxarea , current_area)

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return maxarea
        