#include <stdio.h>
#define ZERO 0
#define VALOR 1

int main(int argc, char const *argv[]) {
  int c,ch,estado = ZERO;

  while ((c = getchar()) != EOF) {
    if (c == '0') {
      estado = ZERO;
    }
    else if (estado == ZERO || estado == VALOR) {
      putchar(c);
      estado = VALOR;
    }
    else if (estado == VALOR && (c == ' ' || c == '\n' || c == '\t')){
      putchar(c);
      estado = ZERO;
    }
    else {
      printf("0");
    }
  }
  printf("\n");
  return 0;
}
