#include <stdio.h>
#include <stdint.h>
typedef uint32_t T;
#define DIM_LOG 3
#define DIM (1<<DIM_LOG)

int P(T c, int row){
  return c>>row*DIM_LOG & DIM-1;
}

void print(T c) {
    int col, row;
    for (row = 0; row < DIM; row++)  {
        const int ix = P(c, row);
        for (col = 0; col < DIM; col++)
            printf("|%c", ix == col  ? '*' : ' ');
        printf("|\n");
    }
    printf("\n");
}

int valido(T c) {

  for (int row = 0; row < DIM ; row++) {
    const int col_n = P(c, row);

    for (int i = row+1; i < DIM; i++) {
      const int col = P(c, i);
      if (col_n == col || row-col_n == i-col || row+col_n == i+col) {
        return 0;
      }
    }
  }
  return 1;
}

int main() {
  T c = (1<<DIM_LOG*DIM) - 1;
  int total = 0;

  for (T i = 0; i < c; i++) {
    if (valido(i) == 1) {
      print(i);
      total++;
    }
  }
  printf("%d\n", total);
  return 0;
}
