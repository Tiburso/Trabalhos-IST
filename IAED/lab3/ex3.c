#include <stdio.h>

void cruz(int N) {
  for (size_t linhas = 0; linhas < N; linhas++) {
    for (size_t write = 0; write < N; write++) {
      if (write == N-linhas-1 || write == linhas) {
        printf("* ");
      }
      else
        printf("- ");
    }
    printf("\n");
  }
}

int main(int argc, char const *argv[]) {
  int N;
do {
  printf("Escreva um numero:");
  scanf("%d", &N);
} while(N < 1);
  cruz(N);
  return 0;
}
