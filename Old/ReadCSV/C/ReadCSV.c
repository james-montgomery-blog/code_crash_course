#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    FILE *fp;

    fp = fopen("../test.csv", "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);

    char buf[1024];
    while (fgets(buf, sizeof(buf), fp) != NULL)
    {
      buf[strlen(buf) - 1] = '\0'; // eat the newline fgets() stores
      printf("%s\n", buf);
    }

    fclose(fp);
    exit(EXIT_SUCCESS);
}
