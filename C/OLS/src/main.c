#include <stdio.h>
#include <stdlib.h>
#include <cblas.h>
#include "utils.h"

int main() {
    int success_flag = 1;
    char * data_path = "../Test_Data/linear.csv";

    int cols = column_count(data_path);
    int rows = row_count(data_path) - 1;
    double data[rows][cols];

    int success = read_data(data_path, rows, cols, data);
    if(success != 0){
        return 1;
    }

    double *x = (double *) malloc(sizeof(double)*rows);
    double *y = (double *) malloc(sizeof(double)*rows);

    fetch_column(x, data, 1, rows, cols);
    fetch_column(y, data, 2, rows, cols);

    double xTx[rows];

    /* optimization: reuse x as read from data, dont read for each vector used */
    cblas_dgemm(CblasRowMajor, CblasNoTrans, CblasTrans, 1, 1, rows, 1, x, rows, x, rows, 0.0, xTx, 1 );

    double xTy[rows];

    cblas_dgemm(CblasRowMajor, CblasNoTrans, CblasTrans, 1, 1, rows, 1, x, rows, y, rows, 0.0, xTy, 1 );

    printf("C: %.30f\n", xTx[0]);
    printf("C: %.30f\n", xTy[0]);

    free(x);
    free(y);
    return success_flag;
}
