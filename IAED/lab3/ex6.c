#include <stdio.h>

int main(int argc, char const *argv[]) {
  int c, total = 0;
  printf("Escreva um número:");
  while ((c = getchar()) != '\n') {
    total = total + (c - 48);
  }
  if (total % 9 == 0) {
    printf("yes\n");
  }
  else
    printf("no\n");
  return 0;
}
