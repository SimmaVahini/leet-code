class Solution {
public:
    int minPatches(vector<int>& nums, int n) {

        long long reach = 1;
        int patches = 0;
        int i = 0;

        while (reach <= n) {

            if (i < nums.size() && nums[i] <= reach) {
                reach += nums[i];
                i++;
            }
            else {
                reach += reach;
                patches++;
            }
        }

        return patches;
    }
};
