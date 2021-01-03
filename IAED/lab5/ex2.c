#include <stdio.h>

typedef struct complexo{
  float real;
  float im;
}Complexo;

Complexo somaComplexos(Complexo a, Complexo b){

  Complexo soma = {0,0};

  soma.real = a.real + b.real;
  soma.im = a.im + b.im;

  return soma;
}

Complexo LeComplexo(){
  Complexo n;
  char sign, i;

  scanf("%f%c%f%c", &n.real,&sign,&n.im,&i);
  if (sign == '-') {
    n.im *= -1;
  }
  
  return n;
}

void escreveComplexo(Complexo n){
  if (n.im < 0 ) {
    printf("%.2f%.2fi\n", n.real,n.im);
  }
  else
    printf("%.2f+%.2fi\n", n.real, n.im);
}
int main() {
  Complexo a,b,soma;

  a = LeComplexo();
  b = LeComplexo();

  soma = somaComplexos(a, b);

  escreveComplexo(soma);

  return 0;
}
