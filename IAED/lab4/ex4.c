#include <stdio.h>
#include <string.h>
#define MAX 80

void clear(char v[],int size);

int main() {
  int i,dim,l = 0;
  char v1[MAX], v2[MAX],str[MAX];

  clear(v1,MAX);
  clear(v2,MAX);
  printf("Escreva uma palavra:");
  scanf("%s", str);
  for (dim = 0; str[dim] != '\0'; dim++);
  for (i = 0; i < dim/2; i++) {
    v1[i] = str[i];
  }
  for (i = dim-1; i > dim/2-1; i--) {
    v2[l] = str[i];
    l++;
  }
  if (strcmp(v1,v2) == 0){
    printf("yes\n");
  }
  else{
    printf("no\n");
  }
  return 0;
}

void clear(char v[],int size) {
  for (size_t i = 0; i < size; i++) {
    v[i] = ' ';
  }
}
