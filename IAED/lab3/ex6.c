#include <stdio.h>

int main(int argc, char const *argv[]) {
  int c;
  printf("Escreva um número:");
  while (c = getchar() != EOF) {

  }
  if (c % 9 == 0) {
    printf("yes");
  }
  else
    printf("no");
  return 0;
}
