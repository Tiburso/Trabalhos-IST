#include <stdio.h>
#define SUM 0
#define SUB 1
#define NUM 2
#define OPT 3

int pot(int n,int b){
  if (b == 0){
    return 1;
  }
  int total = 1;
  for (size_t i = 0; i < b; i++) {
    total = total * n;
  }
  return total;
}

int main(int argc, char const *argv[]) {
  int c,i = 0,n = 0, op = SUM,estado = NUM;
  while ((c = getchar()) != '\n') {
    if (estado == OPT){
      while (c != ' '){
        if (c == '+') {
        op = SUM;
        }
        else if (c == '-') {
        op = SUB;
        }
      estado = NUM;
      }
    }
    else if (estado = NUM) {
      if (op == SUM) {
        while (c != ' '){
          n = n + (c-48)*pot(10,i);
          i++;
        i = 0;
        estado = OPT;
        }
      }
      if (op == SUB) {
        while (c != ' '){
          n = n - (c-48)*pot(10,i);
          i++;
        i = 0;
        estado = OPT;
        }
      }
    }
  }
  printf("%d\n", n);
  return 0;
}
