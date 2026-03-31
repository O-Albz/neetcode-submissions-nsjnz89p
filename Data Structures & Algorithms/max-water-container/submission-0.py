class Solution:
    def maxArea(self, heights: List[int]) -> int:

        def calculate_area(indices: List[int]):
            heightss = [heights[indices[0]], heights[indices[1]]]
            height = min(heightss)
            width = max(indices) - min(indices)
            return height * width

        MAX_AREA = 0
        L, R = 0, len(heights) - 1

        for i in range(len(heights)):
            area = calculate_area([L, R])
            if area > MAX_AREA:
                MAX_AREA = area
            
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1

        return MAX_AREA
        