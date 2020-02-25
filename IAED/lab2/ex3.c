#include "stdio.h"

int main() {
  int n;

  int total = 0;
  printf("Escreva um inteiro: ");
  scanf("%d", &n);
  for (int i = 1; i < n+1; i++) {
    if (n % i == 0) {
      total = total + 1;
    }
  }
  printf("O total de divisores é %d\n", total);
  return 0;
}
