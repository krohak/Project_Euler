/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
class Solution {
public:
    
    // zip the left and right subtree's extreme nodes, 
    // which are facing each other on the inside of the tree
    
    void connect(TreeLinkNode *root) {
        
        if (root == NULL){
            return; 
        }
        
        TreeLinkNode * left = root->left;
        TreeLinkNode * right = root->right;
        
        while (left != NULL && right != NULL){
            
            left->next = right;
            
            left = left->right;
            right = right->left;
        }
        
        connect(root->left);
        connect(root->right);
    }
};
