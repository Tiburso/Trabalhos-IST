#include <stdio.h>

int fact(int n){
  int x = 1;
  if (n == 0) {
    return x;
  }
  else {
    for (size_t i = 1; i <= n; i++) {
      x = x * i;
    }
  }
  return x;
}

int comb(int n, int k){
  return fact(n)/(fact(k)*fact(n-k));
}

int main() {
  int n;
  printf("Escreva uma linha do triangulo de pascal:");
  scanf("%d", &n);
  for (size_t linha = 0; linha <= n-1; linha++) {
    for (size_t i = 0; i <= linha; i++) {
      printf("%d ", comb(linha,i)); }
    printf("\n"); }
  return 0;
}
