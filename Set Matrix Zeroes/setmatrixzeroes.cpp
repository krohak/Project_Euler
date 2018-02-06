class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        
        vector<vector<int>>::iterator itr_row;
        vector<int>::iterator itr_col;
        
        vector<int>::iterator itr_row_1;
        
        bool row_0 = 0;
        bool col_0 = 0;
        
        itr_row_1 = (*matrix.begin()).begin();
        
        for (itr_row=matrix.begin(); itr_row!=matrix.end(); itr_row++){
            for(itr_col = (*itr_row).begin(); itr_col != (*itr_row).end(); itr_col++){
                
                if( *itr_col == 0 && itr_row == matrix.begin()){
                
                     row_0 = 1;
                     //col_0 = 1;
                }
                
                
                if( *itr_col == 0 && itr_col == (*itr_row).begin()){
                
                     //row_0 = 1;
                     col_0 = 1;
                }
                
                 if( *itr_col == 0 && itr_col != (*itr_row).begin() ){
                    
                    *itr_row_1 = 0;
                    (*itr_row)[0] = 0;
                    
                     //row_0 = 1;
                     //col_0 = 1;
                }
                
                itr_row_1++;
            
            }
            
            itr_row_1 = (*matrix.begin()).begin();
        }
        
        
        
        
        itr_row_1 = (*matrix.begin()).begin()+1;
        
        for (itr_row=matrix.begin()+1; itr_row!=matrix.end(); itr_row++){
            for(itr_col = (*itr_row).begin()+1; itr_col != (*itr_row).end(); itr_col++){
                
                if( *itr_row_1 == 0 || (*itr_row)[0] == 0){
                    *itr_col = 0;
                }
                
               //  if( *itr_row_1 == 0){row_0 = 1;}
               // if( (*itr_row)[0] == 0){col_0 = 1;}
                
                itr_row_1++;
            
            }
            
            itr_row_1 = (*matrix.begin()).begin()+1;
        }
        
        
        if( *(*matrix.begin()).begin() == 0){row_0=1; col_0=1;}
        
        for (itr_row=matrix.begin(); itr_row!=matrix.end(); itr_row++){
            
            
            cout << col_0 << row_0;
            
            if(col_0 == 1 ){(*itr_row)[0] = 0;}
            
            if( itr_row == matrix.begin() && row_0 == 1){
                for(itr_col = (*itr_row).begin()+1; itr_col != (*itr_row).end(); itr_col++){
                    *itr_col = 0;
                }    
            }
            
        }
    
    
    
    }
};
