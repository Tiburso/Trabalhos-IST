#include "stdio.h"

int main(int argc, char const *argv[]) {
  int N;

  printf("Escreva um número inteiro\n");
  scanf("%d", &N);
  for (int i = 1; i < N+1; i++) {
    printf("%d\n", i);
  }
  return 0;
}
