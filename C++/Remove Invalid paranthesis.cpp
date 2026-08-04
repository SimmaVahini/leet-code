class Solution {
public:
    vector<string> ans;

    bool isValid(string s) {
        int count = 0;

        for (char c : s) {
            if (c == '(') {
                count++;
            }
            else if (c == ')') {
                count--;

                if (count < 0)
                    return false;
            }
        }

        return count == 0;
    }

    void solve(string s, int index, int removals, int minRemovals) {

        if (removals == minRemovals) {

            if (isValid(s)) {
                ans.push_back(s);
            }

            return;
        }

        for (int i = index; i < s.length(); i++) {

            // Avoid duplicate removals
            if (i > index && s[i] == s[i - 1])
                continue;

            // Only parentheses need to be removed
            if (s[i] != '(' && s[i] != ')')
                continue;

            string next = s.substr(0, i) + s.substr(i + 1);

            solve(next, i, removals + 1, minRemovals);
        }
    }

    vector<string> removeInvalidParentheses(string s) {

        ans.clear();

        int balance = 0;
        int minRemovals = 0;

        // Find minimum number of invalid parentheses
        for (char c : s) {

            if (c == '(') {
                balance++;
            }
            else if (c == ')') {

                if (balance > 0) {
                    balance--;
                }
                else {
                    minRemovals++;
                }
            }
        }

        // Remaining unmatched '(' must be removed
        minRemovals += balance;

        solve(s, 0, 0, minRemovals);

        return ans;
    }
};
