#include "stdio.h"

int main(int argc, char const *argv[]) {
  int N;

  printf("Escreva um número de segundos:" );
  scanf("%d", &N);
  int horas = N/3600;
  int minutos = N%3600/60;
  int segundos = N%3600%60;
  printf("%d:%d:%d\n", horas,minutos,segundos);
  return 0;
}
