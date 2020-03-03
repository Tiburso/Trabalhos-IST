#include <stdio.h>

void piramide(int N) {
  for (size_t i = 1; i <= N; i++) {
    for (int tab = 1; tab <= i; tab++) {
      if (tab < i) {
        }
      else {
        printf("' '");
        }
      }
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
