#include <stdio.h>
#include <stdlib.h>
#include <cblas.h>
#include "utils.h"

void fetch_column(double * out, double * in, int col, int rows, int cols){
    for(int i=0; i<rows; i++){
        out[i]= in[cols*i+col];
    } 
}

void print_matrix(double * data, int n){
    for(int i = 0; i < n; i++){
        printf("%d: %f\n", i, data[i]);
    }
}

int main() {
    int success_flag = 1;
    char * data_path = "../../Test_Data/linear.csv";

    int cols = column_count(data_path);
    int rows = row_count(data_path) - 1;
    printf("rows: %d\n cols: %d\n", rows, cols);
    double data[rows][cols];

    int success = read_data(data_path, rows, cols, data);
    if(success != 0){
        return 1;
    }

    print_matrix(data, rows*cols);

    double *x = (double *) malloc(sizeof(double)*rows);
    double *x2 = (double *) malloc(sizeof(double)*rows);

    fetch_column(x, data, 1, rows, cols);
    fetch_column(x2, data, 1, rows, cols);

    print_matrix(x, rows);

    double C[rows];

    /* optimization: reuse x as read from data, dont read for each vector used */
    cblas_dgemm(CblasRowMajor, CblasNoTrans, CblasTrans, 1, 1, rows, 1, x, rows, x2, rows, 0.0, C, 1 );

    printf("C: %.30f\n", C[0]);

    free(x);
    free(x2);
    return success_flag;
}
