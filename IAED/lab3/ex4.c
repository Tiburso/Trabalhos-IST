#include <stdio.h>
#define NUM 0
#define VALOR 1

int main(int argc, char const *argv[]) {
  int c,ch,estado = NUM;

  while ((c = getchar()) != EOF) {
    if (c == '0') {
      estado = NUM;
    }
    else if (estado == NUM || estado == VALOR) {
      putchar(c);
      estado = VALOR;
    }
    else if (estado == VALOR && (c == ' ' || c == '\n' || c == '\t')){
      putchar(c);
      estado = NUM;
    }
    else {
      printf("0");
    }
  }
  printf("\n");
  return 0;
}
