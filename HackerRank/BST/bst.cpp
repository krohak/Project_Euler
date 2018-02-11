 bool checkBST(Node* root, int min, int max) {

       if(root==NULL){
           return true;
       }

       if(root->data > max || root->data < min){
           return false;
       }

      return ( checkBST(root->left, min, root->data-1) && checkBST(root->right, root->data+1, max) );

}


bool checkBST(Node* root) {

    return checkBST(root,0,10000);
}
