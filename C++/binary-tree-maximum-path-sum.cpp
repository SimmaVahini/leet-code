class Solution {
public:
    int ans = INT_MIN;

    int solve(TreeNode* root) {

        if (root == nullptr)
            return 0;

        // Ignore negative paths
        int left = max(0, solve(root->left));
        int right = max(0, solve(root->right));

        // Path passing through current node
        int currentPath = root->val + left + right;

        // Update maximum answer
        ans = max(ans, currentPath);

        // Return one side to parent
        return root->val + max(left, right);
    }

    int maxPathSum(TreeNode* root) {
        solve(root);
        return ans;
    }
};
