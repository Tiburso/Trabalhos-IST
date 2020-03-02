#include <stdio.h>

void piramide(int N) {
  for (size_t i = 0; i < N; i++) {
    for (int tab = 0; tab < i; tab++) {
      printf("' '");
    }
    printf("%s\n", );
  }
}

int main(int argc, char const *argv[]) {
  int N;
  do {
    printf("Escreva um limite:");
    scanf("%d", &N);
  } while(N < 2);
  piramide(N);
  return 0;
}
