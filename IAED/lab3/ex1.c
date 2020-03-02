#include <stdio.h>

void quadrado(int N) {
  for (int i = 1; i <= N; i++) {
    for (int x = i; x < i+N; x++) {
      printf("%d\t",x);
    }
    printf("\n");
  }
}

int main(int argc, char const *argv[]) {
  int N;
  do {
    printf("Escreva um limite:");
    scanf("%d", &N);
  } while(N < 2);
  quadrado(N);
  return 0;
}
