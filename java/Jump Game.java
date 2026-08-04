class Solution {
    public boolean canJump(int[] nums) {

        int maxReach = 0;

        for (int i = 0; i < nums.length; i++) {

            // If current index cannot be reached
            if (i > maxReach) {
                return false;
            }

            // Find the farthest index we can reach
            maxReach = Math.max(maxReach, i + nums[i]);

            // Already reached the last index
            if (maxReach >= nums.length - 1) {
                return true;
            }
        }

        return true;
    }
}
