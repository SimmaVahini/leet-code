import java.util.*;

class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();

        // Sort the array so duplicates come together
        Arrays.sort(nums);

        boolean[] visited = new boolean[nums.length];

        backtrack(nums, visited, new ArrayList<>(), ans);

        return ans;
    }

    private void backtrack(int[] nums, boolean[] visited,
                           List<Integer> temp,
                           List<List<Integer>> ans) {

        // Base Case
        if (temp.size() == nums.length) {
            ans.add(new ArrayList<>(temp));
            return;
        }

        for (int i = 0; i < nums.length; i++) {

            // Skip if already used
            if (visited[i]) {
                continue;
            }

            // Skip duplicate elements
            if (i > 0 && nums[i] == nums[i - 1] && !visited[i - 1]) {
                continue;
            }

            // Choose
            visited[i] = true;
            temp.add(nums[i]);

            // Recur
            backtrack(nums, visited, temp, ans);

            // Backtrack
            temp.remove(temp.size() - 1);
            visited[i] = false;
        }
    }
}
