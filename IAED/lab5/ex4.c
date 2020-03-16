#include <stdio.h>
#define MAXDIM 100

int ganha(int dim, char v[][MAXDIM], char team){
  int counter = 0;

  for (size_t i = 0; i < dim; i++) {
    for (size_t l = 0; l < dim; l++) {
      if (v[i][l] == team) {
        counter++;
      }
      else
        counter = 0;
    }
    if (counter == 3) {
      return 1;
    }
  }
  counter = 0;

  for (size_t i = 0; i < dim; i++) {
    for (size_t l = 0; l < dim; l++) {
      if (v[l][i] == team) {
        counter++;
      }
      else
        counter = 0;
    }
    if (counter == 3) {
      return 1;
    }
  }
  counter = 0;

  for (size_t i = 0; i < dim; i++) {
    if (v[i][i] == team) {
      counter++;
    }
    if (counter == 3){
      return 1;
    }
  }
  counter = 0;

  for (size_t i = 0; i < dim; i++) {
    if (v[i][(dim-1)-i] == team){
      counter++;
    }
    if (counter == 3) {
      return 1;
    }
  }

  return 0;
}

int main() {
  char tabuleiro[MAXDIM][MAXDIM], team;
  int n,d,x,y;

  scanf("%d", &d);
  for (size_t i = 0; i < d; i++) {
    for (size_t l = 0; l < d; l++) {
      tabuleiro[i][l] = ' ';
    }
  }

  scanf("%d", &n);
  for (size_t i = 0; i < n; i++) {
    scanf("%d %d %c", &x, &y, &team);
    tabuleiro[x][y] = team;
  }

  if (ganha(d, tabuleiro, 'o') == 1) {
    printf("o\n");
  }
  else if (ganha(d, tabuleiro, 'x') == 1) {
    printf("x\n");
  }
  else {
    printf("?\n");
  }

  return 0;
}
