class Solution {
    public int numDecodings(String s) {
        int n = s.length();

        // Edge case
        if (s.charAt(0) == '0') return 0;

        int prev2 = 1; // dp[i-2]
        int prev1 = 1; // dp[i-1]

        for (int i = 1; i < n; i++) {
            int current = 0;

            // 1-digit check
            if (s.charAt(i) != '0') {
                current += prev1;
            }

            // 2-digit check
            int twoDigit = Integer.parseInt(s.substring(i - 1, i + 1));
            if (twoDigit >= 10 && twoDigit <= 26) {
                current += prev2;
            }

            prev2 = prev1;
            prev1 = current;
        }

        return prev1;
    }
}
