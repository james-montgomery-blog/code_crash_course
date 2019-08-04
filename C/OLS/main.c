#include <stdio.h>
#include <stdlib.h>
#include "cblas.h"
#include "utils.h"

void fetch_column(int rows, int cols, double data[rows][cols], int target_column, double arr[rows][1]) {
   for(int i = 0; i < rows; i++) {
      arr[i][0] = data[target_column][i];
   }
}

int main() {

   int success_flag = 1;
   char * data_path = "../Test_Data/linear.csv";

   int cols = column_count(data_path);
   int rows = row_count(data_path) -1;
   double data[rows][cols];

   int success = read_data(data_path, rows, cols, data);

   double x[rows][1];
   double y[rows][1];

   fetch_column(rows, cols, data, 1, x);
   fetch_column(rows, cols, data, 2, y);

   return success_flag;
}
