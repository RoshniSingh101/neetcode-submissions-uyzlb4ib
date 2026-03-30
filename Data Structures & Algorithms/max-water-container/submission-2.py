class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0
        while l < r:
            curr_area = min(heights[l], heights[r]) * (r-l)
            max_area = max(max_area, curr_area)
            # if temp_area > max_area:
            #     max_area = temp_area # why?
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1 # why?
        return max_area