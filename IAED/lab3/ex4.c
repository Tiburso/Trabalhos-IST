#include <stdio.h>
#define ZERO 0
#define VALUE 1

int main(int argc, char const *argv[]) {
  int c,ch,estado = ZERO;

  while ((c = getchar()) != EOF) {
    if (c == '0' && estado == ZERO);
    else if (estado == VALUE && (c == ' ' || c == '\t' || c == '\n')) {
      putchar(c);
      estado = ZERO;
    }
    else if (estado == ZERO && (c == ' ' || c == '\t' || c == '\n')) {
      printf("0%c", c);
      estado = ZERO;
    }
    else if ((estado == ZERO && c != '0') || estado == VALUE) {
      putchar(c);
      estado = VALUE;
    }
  }
  return 0;
}
