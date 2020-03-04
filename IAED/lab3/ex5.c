#include <stdio.h>
#define SLASH 0
#define WORD 1
#define SPACE 2

 int main(int argc, char const *argv[]) {
   int c, state = SPACE;

   while ((c = getchar()) != EOF) {
     if (state == SPACE && c == '"') {
       state = WORD;
     }
     else if (state == WORD && c == '\\') {
       state = SLASH;
     }
     else if (state == WORD && c != '"') {
       putchar(c);
     }
     else if (state == WORD && c == '"') {
       printf("\n");
       state = SPACE;
     }
     else if (state == SLASH && (c == '"' || c == '\\')) {
       putchar(c);
       state = WORD;
     }
   }
   return 0;
 }
