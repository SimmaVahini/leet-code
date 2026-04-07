import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> triangle = new ArrayList<>();

        for (int i = 0; i < numRows; i++) {
            List<Integer> row = new ArrayList<>();
            // The first element of every row is always 1
            row.add(1);

            for (int j = 1; j < i; j++) {
                // Each middle element is the sum of the two elements above it
                List<Integer> prevRow = triangle.get(i - 1);
                row.add(prevRow.get(j - 1) + prevRow.get(j));
            }

            // The last element of every row (except the first) is 1
            if (i > 0) {
                row.add(1);
            }

            triangle.add(row);
        }

        return triangle;
    }
}
