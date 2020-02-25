#include <stdio.h>

int main() {
  int N;
  float max,min,x;

  printf("Escreva um limite:");
  scanf("%d", &N);
  for (int i = 0; i < N; i++) {
    printf("Escreva um número:");
    scanf("%f", &x);
    if (x > max) {
      max = x;
    }
    else if (x < min) {
      min = x;
    }
    else
      continue;
  }
  printf("min: %f, max: %f\n", min, max);
  return 0;
}
