#include <fstream>
#include <string>
int main()
{
  std::ifstream file("../test.csv");
  if (file.is_open()) {
      std::string line;
      while (getline(file, line)) {
          // using printf() in all tests for consistency
          printf("%s \n", line.c_str());
      }
      file.close();
  }
}
