#include <stdio.h>

int main() {
  int a,b,c;

  printf("Escreva três numeros:");
  scanf("%d%d%d", &a,&b,&c);
  if (a > b && a > c) {
    printf("O seu número é %d\n", a);
  }
  else if (b > a && b > c) {
    printf("Os seu número é %d\n", b);
  }
  else
    printf("O seu número é %d\n", c);
  return 0;
}
