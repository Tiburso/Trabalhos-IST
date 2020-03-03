#include <stdio.h>
#define ZERO 0
#define VALOR 1

int main(int argc, char const *argv[]) {
  int c,ch,estado = ZERO;
  printf("Escreva uma quantidade arbitraria de numeros:");
  while ((c = getchar()) != EOF) {
    if (c == '0') {
      estado = ZERO;
    }
    else if (estado == ZERO) {
      estado = VALOR;
      printf("%c", c);
    }
    else if (c == '\n' || c == ' ' || c == '\t') {
      estado = ZERO;
    }
  }
  printf("\n");
  return 0;
}
