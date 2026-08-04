class Solution {
public:
    vector<string> result;

    void solve(string &num, int target, int index,
               long long value, long long prev,
               string expression) {

        if (index == num.size()) {
            if (value == target) {
                result.push_back(expression);
            }
            return;
        }

        for (int i = index; i < num.size(); i++) {

            // Leading zero is not allowed
            if (i > index && num[index] == '0')
                break;

            string part = num.substr(index, i - index + 1);
            long long current = stoll(part);

            // First number
            if (index == 0) {
                solve(num, target, i + 1,
                      current, current, part);
            }
            else {
                // +
                solve(num, target, i + 1,
                      value + current,
                      current,
                      expression + "+" + part);

                // -
                solve(num, target, i + 1,
                      value - current,
                      -current,
                      expression + "-" + part);

                // *
                solve(num, target, i + 1,
                      value - prev + prev * current,
                      prev * current,
                      expression + "*" + part);
            }
        }
    }

    vector<string> addOperators(string num, int target) {
        result.clear();

        solve(num, target, 0, 0, 0, "");

        return result;
    }
};
