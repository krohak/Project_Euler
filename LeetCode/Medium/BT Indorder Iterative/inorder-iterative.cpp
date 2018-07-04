class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        stack <TreeNode*> Stack;
        vector <int> result;
        TreeNode * head = root;
        
        // do the below while either the stack is not empty or the current node is not null
        while (!Stack.empty() || head != NULL){
            
            // if node is null, pop from stack, visit node, go right.
            if (head == NULL){
                head = Stack.top(); Stack.pop();
                result.push_back(head->val);
                head = head->right;
            }
            
            // if node left exists, push in stack and keep going left
            else if (head->left != NULL){
                Stack.push(head);
                head = head->left;
            }
            
            // if node left null, visit node and go right
            else if (head->left == NULL){
                result.push_back(head->val);
                head = head->right;
            }
        }
        
        // if stack empty and node is null
        return result;
    }
};
