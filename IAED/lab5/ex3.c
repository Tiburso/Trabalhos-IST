#include <stdio.h>
#include <string.h>
#define TITULOS 1000

typedef struct stock {
  char nome[10];
  float valor;
  float rendimento;
}Stock;

Stock leStock(){
  Stock x;

  scanf("%s %f %f", x.nome,&x.valor,&x.rendimento);

  return x;
}

Stock maiorStock(int n, Stock v[]){
  Stock maior = {' ',0,0};

  for (size_t i = 0; i < n; i++) {
    if (v[i].rendimento > maior.rendimento) {
      strcpy(maior.nome, v[i].nome);
      maior.valor = v[i].valor;
      maior.rendimento = v[i].rendimento;
    }
  }

  return maior;
}

void escreveStock(Stock n) {
  printf("%s %.2f %.2f\n", n.nome, n.valor, n.rendimento);
}

int main() {
  int n;
  Stock v[TITULOS], maior;

  scanf("%d", &n);
  for (size_t i = 0; i < n && i < TITULOS; i++) {
    v[i] = leStock();
  }

  maior = maiorStock(n, v);

  escreveStock(maior);

  return 0;
}
