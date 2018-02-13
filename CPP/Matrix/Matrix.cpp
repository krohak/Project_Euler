#include <iostream>
#include "Matrix.h"
#include "Equation_solving.h"
#include <cstdlib>
using namespace std;


Matrix::Matrix(){
        row =0, col=0, flag=0;
}


Matrix::Matrix(int r, int c){
        if(r==0 || c==0)
        {
                cout<<"Invalid number of rows or columns!";
        }
        else
        {
                row = r;
                col = c;
                flag = 0;
                values = new float* [row];
                for(int i=0; i<row; i++)
                {
                        values[i] = new float [col];
                }

                for(int i=0; i<row; i++)
                {
                        for(int j=0; j<col; j++)
                                values [i][j] = 0;
                }

        }
}


Matrix::Matrix(const Matrix &m){

        row = m.row; col = m.col; flag = m.flag;

        values = new float* [row];
        for(int i=0; i<row; i++)
        {
                values[i] = new float [col];
        }
        for(int i=0; i<m.row; i++)
        {
                for(int j=0; j<m.col; j++)
                {
                        values[i][j]=m.values[i][j];
                }
        }


}

Matrix::Matrix(Matrix&& m){

        row = m.row; col = m.col; flag=m.flag;


        values = new float* [row];
        for(int i=0; i<row; i++)
        {
                values[i] = new float [col];
        }
        for(int i=0; i<m.row; i++)
        {
                for(int j=0; j<m.col; j++)
                {
                        values[i][j]=m.values[i][j];
                }
        }


        //this = Matrix(m);

        /*  for (int i = 0; i < m.row; i++) {
                //delete [] m.values[i];
                free(m.values[i]);
                m.values[i] = 0;
            }*/
        m.~Matrix();

        //delete[]
        //free(m.values);


}

Matrix::~Matrix(){

        if (row!=0 && col !=0) {
                for (int i = 0; i < row; i++) {
                        delete [] values[i];
                        //values[i] = 0;

                } delete[] values;
                row=0; col=0;
        }
        else {}


}



Matrix& Matrix::operator= (const Matrix& m){

        row=m.row; col=m.col; flag=m.flag;


        values = new float* [row];
        for(int i=0; i<row; i++)
        {
                values[i] = new float [col];
        }
        for(int i=0; i<m.row; i++)
        {
                for(int j=0; j<m.col; j++)
                {
                        values[i][j]=m.values[i][j];
                }
        }


}


ostream& operator << (ostream& cout, const Matrix& M){

        if (M.flag==0) {
                for(int i=0; i<M.row; i++)
                {
                        for(int j=0; j<M.col; j++)
                        {
                                cout<<M.values[i][j]<<" ";
                        }
                        cout<<endl;
                }
        }
        else {

                for(int i=0; i<M.col; i++)
                {
                        for(int j=0; j<M.row; j++)
                        {
                                cout<<M.values[j][i]<<" ";
                        }
                        cout<<endl;
                }

        }

        return cout;
}

istream& operator >> (istream& cin, Matrix& M){
        for(int i=0; i<M.row; i++)
        {
                for(int j=0; j<M.col; j++)
                {
                        cin>>M.values[i][j];
                }
        }
        return cin;
}

float Matrix::get_entry(const int &x, const int &y) const {
        if(x>=row || y>=col)
        {
                cout<<"Index out of range!";
                exit(-1);
        }
        else
                return values[x][y];
}

int Matrix::get_column_dimension() const {
        return col;
}

int Matrix::get_row_dimension() const {
        return row;
}

void Matrix::row_switching(int i, int j){
        if(i>=row || j>=row)
        {
                cout<<"Index out of range!";
                exit(-1);
        }
        for(int k=0; k<col; k++)
        {
                float temp = values[i][k];
                values[i][k] = values[j][k];
                values[j][k] = temp;
        }
}



void Matrix::row_multiplication(int i, float k){
        if(k==0)
        {
                cout<<"Cannot be multiplied by a zero constant!";
                exit(-1);
        }
        for(int j=0; j<col; j++)
        {
                values[i][j]*=k;
        }
}

void Matrix::row_addition(int i, int j, float k){
        if(i==j)
        {
                cout<<"Cannot be the same row!";
                exit(-1);
        }
        for (int a=0; a<col; a++)
        {
                values[i][a]+=values[j][a]*k;
        }
}

void Matrix::transpose(){
        Matrix m(col,row);
        for(int i=0; i<col; i++)
        {
                for(int j=0; j<row; j++)
                {
                        m.values[i][j]= values[j][i];
                }
        }

        row = col;
        col = m.col;
        for(int i=0; i<row; i++)
                for(int j=0; j<col; j++)
                        values[i][j]=m.values[i][j];


        for (int i = 0; i < m.row; i++) {
                delete [] m.values[i];
                m.values[i] = 0;
        }


}

void Matrix::transpose_prime(){
        if (flag==0) {
                flag = 1;
        }
        else {flag=0;}

}

Matrix operator + (const Matrix& a, const Matrix& b){
        if(a.row!=b.row || a.col!=b.col)
        {
                cout<<"Cannot do the matrix addition!";
                exit(-1);
        }
        Matrix sum(a.row,a.col);
        for(int i=0; i<a.row; i++)
        {
                for(int j=0; j<a.col; j++)
                {
                        sum.values[i][j]=a.values[i][j]+b.values[i][j];
                }
        }
        return sum;
}

Matrix operator * (const Matrix& m, const float& c){


        if (m.flag==0) {
                Matrix n(m.row,m.col);
                for(int i=0; i<m.row; i++)
                {
                        for(int j=0; j<m.col; j++)
                        {
                                n.values[i][j] = c*m.values[i][j];
                        }
                } return n;
        }
        else if (m.flag==1) {
                Matrix n(m.col,m.row);
                for(int i=0; i<m.col; i++)
                {
                        for(int j=0; j<m.row; j++)
                        {
                                n.values[i][j] = c*m.values[j][i];
                        }
                }
                return n;
        }


}

Matrix operator * (const float& c, const Matrix& m){


        if (m.flag==0) {
                Matrix n(m.row,m.col);
                for(int i=0; i<m.row; i++)
                {
                        for(int j=0; j<m.col; j++)
                        {
                                n.values[i][j] = c*m.values[i][j];
                        }
                } return n;
        }
        else if (m.flag==1) {
                Matrix n(m.col,m.row);
                for(int i=0; i<m.col; i++)
                {
                        for(int j=0; j<m.row; j++)
                        {
                                n.values[i][j] = c*m.values[j][i];
                        }
                }
                return n;
        }


}


Matrix operator * (const Matrix& a, const Matrix& b){
        if (a.flag==0 && b.flag == 0) {
                if(a.col!=b.row)
                {
                        cout<<"Cannot do the matrix multiplication!";
                        exit(-1);
                }
                Matrix prod(a.row,b.col);
                //cout << a.row << "x" << b.col << endl;
                for(int i=0; i<a.row; i++)
                {
                        for(int j=0; j<b.col; j++)
                        {
                                for(int k=0; k<a.col; k++)
                                {
                                        prod.values[i][j]+=(a.values[i][k]*b.values[k][j]);
                                }
                        }
                }
                return prod;
        }

        if (a.flag==1 && b.flag==0) {
                if(a.row!=b.row)
                {
                        cout<<"Cannot do the matrix multiplication!";
                        exit(-1);
                }
                Matrix prod(a.col,b.col);
                //cout << a.col << "/x" << b.col << endl;
                for(int i=0; i<a.col; i++)
                {
                        for(int j=0; j<b.col; j++)
                        {
                                for(int k=0; k<a.row; k++)
                                {
                                        prod.values[i][j]+=(a.values[k][i]*b.values[k][j]);
                                }
                        }
                }
                return prod;
        }

        if (a.flag==0 && b.flag==1) {
                if(a.col!=b.col)
                {
                        cout<<"Cannot do the matrix multiplication!";
                        exit(-1);
                }
                Matrix prod(a.row,b.row);
                //cout << a.row << "~x" << b.row << endl;
                for(int i=0; i<a.row; i++)
                {
                        for(int j=0; j<b.row; j++)
                        {
                                for(int k=0; k<a.col; k++)
                                {
                                        prod.values[i][j]+=(a.values[i][k]*b.values[j][k]);
                                }
                        }
                }
                return prod;
        }

        if (a.flag==1 && b.flag==1) {
                if(a.row!=b.col)
                {
                        cout<<"Cannot do the matrix multiplication!";
                        exit(-1);
                }
                Matrix prod(a.col,b.row);
                //cout << a.col << "+x" << b.row << endl;
                for(int i=0; i<a.col; i++)
                {
                        for(int j=0; j<b.row; j++)
                        {
                                for(int k=0; k<a.row; k++)
                                {
                                        prod.values[i][j]+=(a.values[k][i]*b.values[j][k]);
                                }
                        }
                }
                return prod;
        }



}
