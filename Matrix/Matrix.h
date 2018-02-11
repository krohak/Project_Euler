 #ifndef MATRIX_H
 #define MATRIX_H

 #include <iostream>
 #include <vector>

using namespace std;
class Matrix
{
private:
int row,col;
float **values;
bool flag;

public:
Matrix();
Matrix(int r, int c);
~Matrix();
Matrix& operator= (const Matrix& m);

Matrix(const Matrix& m);       //copy constructor

Matrix(Matrix&& m);        //move constructor

int get_row_dimension() const;        // the number of rows;
int get_column_dimension() const;
float get_entry(const int &x, const int &y) const;
void row_switching(int i, int j);
void row_multiplication(int i, float k);
void row_addition(int i, int j, float k);

void transpose();

friend Matrix operator + (const Matrix& a, const Matrix& b);
friend Matrix operator * (const Matrix& m, const float& c);
friend Matrix operator * (const float& c, const Matrix& m);
friend Matrix operator * (const Matrix& a, const Matrix& b);


void transpose_prime();


friend ostream& operator << (ostream& cout, const Matrix& M);
friend istream& operator >> (istream& cin, Matrix& M);

};

ostream& operator << (ostream& cout, const Matrix& M);
istream& operator >> (istream& cin, Matrix& M);
Matrix operator + (const Matrix& a, const Matrix& b);
Matrix operator * (const Matrix& m, const float& c);
Matrix operator * (const float& c, const Matrix& m);
Matrix operator * (const Matrix& a, const Matrix& b);



 #endif
