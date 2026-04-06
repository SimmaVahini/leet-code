import java.util.*;

class Solution {
    Map<String, Boolean> memo = new HashMap<>();

    public boolean isScramble(String s1, String s2) {
        // Base case
        if (s1.equals(s2)) return true;

        // Memo check
        String key = s1 + "#" + s2;
        if (memo.containsKey(key)) {
            return memo.get(key);
        }

        // Pruning: check character frequency
        int[] count = new int[26];
        for (int i = 0; i < s1.length(); i++) {
            count[s1.charAt(i) - 'a']++;
            count[s2.charAt(i) - 'a']--;
        }

        for (int c : count) {
            if (c != 0) {
                memo.put(key, false);
                return false;
            }
        }

        int n = s1.length();

        // Try all splits
        for (int i = 1; i < n; i++) {

            // Case 1: No swap
            if (isScramble(s1.substring(0, i), s2.substring(0, i)) &&
                isScramble(s1.substring(i), s2.substring(i))) {
                memo.put(key, true);
                return true;
            }

            // Case 2: Swap
            if (isScramble(s1.substring(0, i), s2.substring(n - i)) &&
                isScramble(s1.substring(i), s2.substring(0, n - i))) {
                memo.put(key, true);
                return true;
            }
        }

        memo.put(key, false);
        return false;
    }
}
