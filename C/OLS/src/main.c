#include <stdio.h>
#include <stdlib.h>
#include "cblas.h"
#include "utils.h"

int main() {

   int success_flag = 1;
   char * data_path = "../../Test_Data/linear.csv";

   int cols = column_count(data_path);
   int rows = row_count(data_path) -1;
   double data[rows][cols];

   int success = read_data(data_path, rows, cols, data);

   double x[rows][1];
   double y[rows][1];

   fetch_column(rows, cols, data, 1, x);
   fetch_column(rows, cols, data, 2, y);


   double C[rows];
   cblas_dgemm(CblasRowMajor, "C", "N", 1, 1, rows, 1.0, x, 1, x, rows, 0.0, C, 1);

   return success;
}
