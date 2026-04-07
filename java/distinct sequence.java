class Solution {
    public int numDistinct(String s, String t) {
        int n = t.length();
        // dp[j] will store the number of distinct subsequences for t.substring(0, j)
        int[] dp = new int[n + 1];
        
        // Base case: an empty string t is a subsequence of any string s in 1 way
        dp[0] = 1;
        
        // Iterate through each character in the source string s
        for (char charS : s.toCharArray()) {
            // Update dp array in reverse to avoid using the same character 
            // of s multiple times for the same subsequence.
            for (int j = n; j >= 1; j--) {
                // If characters match, add the ways to form the prefix t[0...j-2]
                if (charS == t.charAt(j - 1)) {
                    dp[j] += dp[j - 1];
                }
            }
        }
        
        return dp[n];
    }
}
