#include <stdio.h>

int main() {
  int a,b;

  printf("Escreva dois números inteiros: \n");
  scanf("%d%d", &a, &b);
  if (a > b) {
    printf("O maior número é %d\n e o menor número é %d\n", a,b);
  }
  else {
    printf("O maior números é %d\nO menor número é %d\n", b,a);
  }
  return 0;
}
