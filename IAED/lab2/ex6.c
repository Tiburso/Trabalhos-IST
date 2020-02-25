#include "stdio.h"

int main(int argc, char const *argv[]) {
  int N;
  int i = 0;
  int soma = 0;

  printf("Escreva um número:");
  scanf("%d", &N);
  while (N > 0) {
    soma = soma + N%10;
    i = i + 1;
    N = N/10;
  }
  printf("O número é composto por %d digitos\nA soma dos digitos é %d\n", i,soma);
  return 0;
}
