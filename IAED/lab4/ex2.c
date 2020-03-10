#include <stdio.h>
#define VECMAX 100

int main() {
  int n, max = 1;
  int v[VECMAX];

  printf("Escreva um número:");
  scanf("%d", &n);

  for (size_t i = 0; i < n; i++) {
    scanf("%d", &v[i]);
    if (v[i] > max)
      max = v[i];
  }
  for (size_t i = 0; i < max; i++) {
    for (size_t l = 0; l < n && l < VECMAX; l++) {
      if (v[l] > i) {
        putchar('*');
      }
      else{
        putchar(' ');
      }
    }
    putchar('\n');
  }
  return 0;
}
