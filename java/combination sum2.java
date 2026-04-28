import java.util.*;

class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(candidates); // Step 1: sort
        backtrack(candidates, target, 0, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(int[] candidates, int target, int start,
                           List<Integer> current, List<List<Integer>> result) {

        // Base case
        if (target == 0) {
            result.add(new ArrayList<>(current));
            return;
        }

        for (int i = start; i < candidates.length; i++) {

            // Step 2: skip duplicates
            if (i > start && candidates[i] == candidates[i - 1]) continue;

            // If number exceeds target → stop
            if (candidates[i] > target) break;

            // Choose
            current.add(candidates[i]);

            // Move to next index (i + 1 → use only once)
            backtrack(candidates, target - candidates[i], i + 1, current, result);

            // Backtrack (remove)
            current.remove(current.size() - 1);
        }
    }
}
