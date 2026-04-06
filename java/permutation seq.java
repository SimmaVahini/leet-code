import java.util.*;

class Solution {
    public String getPermutation(int n, int k) {

        List<Integer> numbers = new ArrayList<>();
        int[] fact = new int[n + 1];

        // Step 1: Precompute factorial
        fact[0] = 1;
        for (int i = 1; i <= n; i++) {
            fact[i] = fact[i - 1] * i;
        }

        // Step 2: Fill numbers list
        for (int i = 1; i <= n; i++) {
            numbers.add(i);
        }

        // Step 3: Convert k to 0-based
        k = k - 1;

        StringBuilder result = new StringBuilder();

        // Step 4: Build answer
        for (int i = n; i >= 1; i--) {
            int index = k / fact[i - 1];
            result.append(numbers.get(index));
            numbers.remove(index);

            k = k % fact[i - 1];
        }

        return result.toString();
    }
}
