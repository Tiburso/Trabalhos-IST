#include <stdio.h>
#define MAXVEC 100

int main() {
  int n;
  int vec[MAXVEC];

  printf("Escreva um número:");
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &vec[i]);
  }
  for (int i = 0; i < n && i < MAXVEC; i++) {
      for (int j = 0; j < vec[i]; j++) {
        putchar('*');
      }
      putchar('\n');
  }
  return 0;
}
