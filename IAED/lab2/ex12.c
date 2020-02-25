#include <stdio.h>

int main() {
  int N,M;

  printf("Ecreva dois números inteiros\n");
  scanf("%d%d", &N,&M);
  if (N % M == 0) {
    printf("yes\n");
  }
  else {
    printf("no\n");
  }
  return 0;
}
