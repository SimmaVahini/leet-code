import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> row = new ArrayList<>();
        // Base case: the first element is always 1
        row.add(1);
        
        for (int i = 1; i <= rowIndex; i++) {
            // Update the row from right to left
            // to avoid using the "new" values from the current iteration
            for (int j = i - 1; j >= 1; j--) {
                row.set(j, row.get(j) + row.get(j - 1));
            }
            // Every row ends with 1
            row.add(1);
        }
        
        return row;
    }
}
