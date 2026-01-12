from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        """
        The minimum time to move between two points (x1, y1) and (x2, y2)
        is the maximum of the absolute differences of their coordinates:
        max(abs(x2 - x1), abs(y2 - y1)).
        This is because we can move diagonally to cover both dimensions 
        simultaneously as much as possible, then move horizontally or vertically.
        """
        total_time = 0
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i+1]
            total_time += max(abs(x2 - x1), abs(y2 - y1))
        return total_time

if __name__ == "__main__":
    sol = Solution()
    # Example 1
    print(f"Example 1: {sol.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])}") # Expected: 7
    # Example 2
    print(f"Example 2: {sol.minTimeToVisitAllPoints([[3,2],[-2,2]])}")       # Expected: 5
