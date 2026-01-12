class Solution {
    /**
     * The minimum time to move between two points (x1, y1) and (x2, y2)
     * is the maximum of the absolute differences of their coordinates.
     */
    public int minTimeToVisitAllPoints(int[][] points) {
        int totalTime = 0;
        for (int i = 0; i < points.length - 1; i++) {
            int x1 = points[i][0];
            int y1 = points[i][1];
            int x2 = points[i + 1][0];
            int y2 = points[i + 1][1];
            totalTime += Math.max(Math.abs(x2 - x1), Math.abs(y2 - y1));
        }
        return totalTime;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // Example 1
        int[][] points1 = { { 1, 1 }, { 3, 4 }, { -1, 0 } };
        System.out.println("Example 1: " + sol.minTimeToVisitAllPoints(points1)); // Expected: 7

        // Example 2
        int[][] points2 = { { 3, 2 }, { -2, 2 } };
        System.out.println("Example 2: " + sol.minTimeToVisitAllPoints(points2)); // Expected: 5
    }
}
