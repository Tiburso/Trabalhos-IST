#include <stdio.h>

int pot(int n,int b){
  if (b == 0){
    return 1;
  }
  int total = 1;
  for (size_t i = 0; i < b; i++) {
    total = total * n;
  }
  return total;
}

int main(int argc, char const *argv[]) {
  int n,b,l;
  scanf("%d %d", &n,&b);
  l = pot(n,b);
  printf("%d\n", l);
  return 0;
}
