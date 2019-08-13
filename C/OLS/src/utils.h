#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int column_count(char *filepath) {

  FILE* fp = fopen(filepath, "r");
  int i;
  int column_count = 0;
  //int line_count = 1;

  if (fp == NULL) {
      printf("Could not open file %s", filepath);
      exit(EXIT_FAILURE);
  }

  while((i=fgetc(fp)) != '\n') {
      if (i == ',') {
          ++column_count;
      } else if (i != ',') {
      }
  }

  // while((i=fgetc(fp))!=EOF) {
  //     if (i == ',') {
  //         ++column_count;
  //     } else if (i == '\n') {
  //         line_count++;
  //         column_count = 0;
  //     }
  // }

  fclose(fp);
  return column_count+1;
}

int row_count(char *filepath) {

    FILE* fp = fopen(filepath, "r");
    int count = 0;  // Line counter (result)
    char c;  // To store a character read from file

    if (fp == NULL) {
        printf("Could not open file %s", filepath);
        exit(EXIT_FAILURE);
    }

    // Extract characters from file and store in character c
    for (c = getc(fp); c != EOF; c = getc(fp))
        if (c == '\n') // Increment count if this character is newline
            count = count + 1;

    // Close the file
    fclose(fp);
    return count;
}

int read_data(char *filepath, int rows, int cols, double data[rows][cols]) {

    FILE* fp = fopen(filepath, "r");

    char buf[1024];
    char *tokens;
    int rowIndex = 0;
    int colIndex = 0;

    if (fp == NULL) {
        printf("Could not open file %s", filepath);
        exit(EXIT_FAILURE);
    }

    int header_flag = 1;
    while (fgets(buf, sizeof(buf), fp) != NULL) {

        buf[strlen(buf) - 1] = '\0'; // eat the newline fgets() stores
        //printf("\n%s\n", buf);

        // skip the header
        if (header_flag != 1) {
            colIndex = 0;
            tokens = strtok (buf, ",");
            while (tokens != NULL) {
                data[rowIndex][colIndex] = atof(tokens);
                tokens = strtok (NULL, ",");
                colIndex++;
            }
            rowIndex++;
        }
        header_flag++;
    }

    fclose(fp);

    return 0;
}

// How to use pointers
// https://stackoverflow.com/questions/4352768/how-do-i-declare-an-array-of-undefined-or-no-initial-size

// How to use structs as classes
// https://stackoverflow.com/questions/2750270/c-c-struct-vs-class
