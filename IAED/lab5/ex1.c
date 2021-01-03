#include <stdio.h>
#define ALUNOS 10
#define DISCIPLINAS 5

long score_disciplina(int disciplina, int valores[][DISCIPLINAS]){
  int total = 0;

  for (size_t i = 0; i < ALUNOS; i++) {
    total += valores[i][disciplina];
  }
  return total/ALUNOS;
}

long score_aluno(int aluno, int valores[][DISCIPLINAS]){
  int total = 0;

  for (size_t i = 0; i < DISCIPLINAS; i++) {
    total += valores[aluno][i];
  }
  return total/DISCIPLINAS;
}


int main() {
  int N,A,D,maxn = 0,maxa = 0, n, a;
  int valores[ALUNOS][DISCIPLINAS];

  for (size_t i = 0; i < ALUNOS; i++) {
    for (size_t l = 0; l < DISCIPLINAS; l++) {
      valores[i][l] = 0;
    }
  }

  scanf("%d", &N);

  for (size_t i = 0; i < N; i++) {
    scanf("%d %d", &A,&D);
    scanf("%d", &valores[A][D]);
  }

  for (size_t i = 0; i < DISCIPLINAS; i++) {
    if (maxn < score_disciplina(i, valores)) {
      maxn = score_disciplina(i, valores);
      n = i;
    }
  }

  for (size_t i = 0; i < ALUNOS; i++) {
    if (maxa < score_aluno(i, valores)) {
      maxa = score_aluno(i, valores);
      a = i;
    }
  }

  printf("%d\n%d\n", n, a);

  return 0;
}
