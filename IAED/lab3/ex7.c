#include <stdio.h>
#define SUM 0
#define SUB 1
#define NUM 2
#define OPT 3

int main(int argc, char const *argv[]) {
  int c,n = 0,total = 0, op = SUM, estado = NUM;

  while ((c = getchar()) != '\n') {
     if (estado == NUM) {
       if (c == ' ') {
         if (op == SUM) {
           total = total + n;
         }
         else if (op == SUB) {
           total = total - n;
         }
         estado = OPT;
         n = 0;
       }
       else {
         n = n*10 + (c-48);
       }
    }
    else if (estado == OPT){
      if (c == ' ') {
        estado = NUM;
      }
      else if (c == '+') {
        op = SUM;
      }
      else if (c == '-') {
        op = SUB;
      }
    }
  }
  if (op == SUM) {
    total = total + n;
  }
  else if (op == SUB) {
    total = total - n;
  }
  printf("%d\n", total);
  return 0;
}
