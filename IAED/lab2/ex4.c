#include "stdio.h"

int main(int argc, char const *argv[]) {
  int N;
  float n;
  float total = 0;
  printf("Escreva um limite: ");
  scanf("%d", &N);
  for (int i = 0; i < N; i++) {
    printf("Escreva um valor:");
    scanf("%f", &n);
    total = total + n;
  }
  float media = total/N;
  printf("%.2f\n", media);
  return 0;
}
