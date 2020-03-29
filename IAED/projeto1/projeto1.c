/*
 * Ficheiro:  projeto1.c
 * Autor:  Manuel Costa
 * Descricao: Um programa que permite gerir inventario e fazer
   e gerir encomendas
*/

#include <stdio.h>
#include <string.h>

/* inicializar tamanho da descricao */
#define TAMANHO_DS 64

/* inicializar tamanho maximo dos produtos */
#define TAMANHO_ID 10000

/* inicializar tamanho maximo das encomendas */
#define MAX_ENCOMENDAS 500

/* definir tamanho maximo do peso */
#define LIM_PESO 200

/* diferenciar entre strings e inteiros para sort */
#define STRING 0
#define INTEIRO 1

/* definir a estrutura do produto */
typedef struct Produto{
  char ds[TAMANHO_DS];
  int preco;
  int peso;
  int qtd;
}produto;

/* definir a estrutura da encomenda */
typedef struct Encomenda{
  produto produtos[TAMANHO_ID];
  int peso;
}encomenda;

/* inicializar os vetores globais dos produtos e das encomendas */
produto prods[TAMANHO_ID] = {0};
encomenda encomends[MAX_ENCOMENDAS] = {0};

int idproduto = 0; /* variavel global do id dos produtos */
int idencomenda = 0;/* variavel global do id das encomendas */

/* adiciona um produto ao vetor prods*/
void novoProduto() {
  /* criar o novo produto */
  produto p;

  /* ler os inputs do novo produto */
  scanf(" %[^:]:%d:%d:%d", p.ds, &p.preco, &p.peso, &p.qtd);

  prods[idproduto] = p;

  printf("Novo produto %d.\n", idproduto);

  /* incrementa o indice global do id dos produtos */
  idproduto++;
}

/* adiciona stock a um produto no vetor prods */
void adicionaStock() {
  /* inicializar a variavel quantidade e o id do produto*/
  int q, idp;

  scanf("%d:%d", &idp, &q);

  /* verifica se o produto existe */
  if (idp >= idproduto) {
    printf("Impossivel adicionar produto %d ao stock. Produto inexistente.\n", idp);
  }
  else
    /* adiciona stock ao produto */
    prods[idp].qtd += q;
}

/* cria uma nova encomenda */
void novaEncomenda() {
  /* cria uma nova encomenda */
  printf("Nova encomenda %d.\n", idencomenda);

  /* incrementa o indice global do id das encomendas */
  idencomenda++;
}

/* adiciona um produto a encomenda selecionada */
void adicionaProdEncomenda() {
  /* inicializa as variaveis a ler */
  int idp, ide, q;
  scanf("%d:%d:%d", &ide, &idp, &q);

  /* verifica se a encomenda existe */
  if (ide >= idencomenda) {
    printf("Impossivel adicionar produto %d a encomenda %d. Encomenda inexistente.\n", idp, ide);
  }
  /* verifica se o produto existe */
  else if (idp >= idproduto) {
    printf("Impossivel adicionar produto %d a encomenda %d. Produto inexistente.\n", idp, ide);
  }
  /* verifica se o stock a retirar nao e maior que o existente */
  else if (prods[idp].qtd - q < 0) {
    printf("Impossivel adicionar produto %d a encomenda %d. Quantidade em stock insuficiente.\n", idp, ide);
  }
  /* verifica se o peso total nao excede o limite */
  else if (encomends[ide].peso + q*prods[idp].peso > LIM_PESO) {
    printf("Impossivel adicionar produto %d a encomenda %d. Peso da encomenda excede o maximo de 200.\n", idp, ide);
  }
  /* adiciona o produto a encomenda */
  else {
    /* verifica se o produto ja existe na encomenda */
    if (encomends[ide].produtos[idp].ds[0] != '\0') {
      encomends[ide].peso += q*prods[idp].peso;
      encomends[ide].produtos[idp].qtd += q;
      prods[idp].qtd -= q;
    }
    else {
      strcpy(encomends[ide].produtos[idp].ds, prods[idp].ds);
      encomends[ide].produtos[idp].preco = prods[idp].preco;
      encomends[ide].produtos[idp].peso = prods[idp].peso;
      encomends[ide].produtos[idp].qtd = q;
      prods[idp].qtd -= q;
      encomends[ide].peso += q*prods[idp].peso;
    }
  }
}

/* retira stock a um produto no vetor produtos */
void removeStock() {
  /* inicializa as variaveis a ler */
  int s, id;

  scanf("%d:%d", &id, &s);

  /* verifica se o produto existe */
  if (id >= idproduto) {
    printf("Impossivel remover stock do produto %d. Produto inexistente.\n", id);
  }
  else {
    /* verifica se o stock a retirar nao e maior que o existente */
    if (prods[id].qtd - s < 0) {
      printf("Impossivel remover %d unidades do produto %d do stock. Quantidade insuficiente.\n", s, id);
    }
    else
      /* retira stock ao produto */
      prods[id].qtd -= s;
  }
}

/* remove um produto a encomenda selecionada */
void removeProdEncomenda() {
  /* inicializa as variaveis a ler */
  int ide, idp;

  scanf("%d:%d", &ide, &idp);

  /* verifica se a encomenda existe */
  if (ide >= idencomenda) {
    printf("Impossivel remover produto %d a encomenda %d. Encomenda inexistente.\n", idp, ide);
  }
  /* verifica se o produto existe */
  else if (idp >= idproduto) {
    printf("Impossivel remover produto %d a encomenda %d. Produto inexistente.\n", idp, ide);
  }
  else {
    /* apaga o produto da encomenda */
    prods[idp].qtd += encomends[ide].produtos[idp].qtd; /* retorna o stock aos produtos em stock */
    encomends[ide].peso -= encomends[ide].produtos[idp].peso*encomends[ide].produtos[idp].qtd; /* retira o peso do produto ao total */
    memset(encomends[ide].produtos[idp].ds, 0, TAMANHO_DS);
    encomends[ide].produtos[idp].preco = 0;
    encomends[ide].produtos[idp].peso = 0;
    encomends[ide].produtos[idp].qtd = 0;
  }
}

/* calcula o custo total da encomenda selecionada */
void calculaCusto() {
  /* inicializa a variavel a ler */
  int ide;
  int total = 0; /* inicializa a variavel total */
  int i;

  scanf("%d", &ide);

  /* verifica se a encomenda existe */
  if (ide >= idencomenda) {
    printf("Impossivel calcular custo da encomenda %d. Encomenda inexistente.\n", ide);
  }
  else {
    /* soma o custo total da encomenda */
    for (i = 0; i < TAMANHO_ID; i++) {
      total += encomends[ide].produtos[i].preco*encomends[ide].produtos[i].qtd;
    }
    printf("Custo da encomenda %d %d.\n", ide, total);
  }
}

/* altera o preco de um produto tanto no vetor dos produtos como nas encomendas */
void alteraPreco() {
  /* inicializa as variaveis a ler */
  int novop,idp;
  int i;

  scanf("%d:%d", &idp, &novop);

  /* verifica se o produto existe */
  if (idp >= idproduto) {
    printf("Impossivel alterar preco do produto %d. Produto inexistente.\n", idp);
  }
  else {
    /* altera o preco nos produtos */
    prods[idp].preco = novop;

    /* altera o preco nas encomendas */
    for (i = 0; i < idencomenda; i++) {
      if (encomends[i].produtos[idp].ds[0] != '\0') {
        encomends[i].produtos[idp].preco = novop;
      }
    }
  }
}

/* escreve a descricao e a quantidade do produto selecionado na encomenda selecionda */
void listaDsQtdEmEncomenda() {
  /* inicializa as variaveis a ler */
  int ide, idp;

  scanf("%d:%d", &ide, &idp);

  /* verifica se a encomenda existe */
  if (ide >= idencomenda) {
    printf("Impossivel listar encomenda %d. Encomenda inexistente.\n", ide);
  }
  /* verifica se o produto existe */
  else if (idp >= idproduto) {
    printf("Impossivel listar produto %d. Produto inexistente.\n", idp);
  }
  /* escreve o descricao e a quantidade */
  else {
    printf("%s %d.\n", prods[idp].ds, encomends[ide].produtos[idp].qtd);
  }
}

/* escreve o indice do produto, o indice da encomenda e a sua quantidade
   na encomenda que contem a maior quantidade do produto selecionado */
void listaProdemEncomenda() {
  /* inicializa a variavel a ler  */
  int idp;
  int maior = 0, qtdM = 0; /* variavel que guarda a maior quantidade e o indice desse produto */

  scanf("%d", &idp);

  /* verifica se o produto existe */
  if (idp >= idproduto) {
    printf("Impossivel listar maximo do produto %d. Produto inexistente.\n", idp);
  }
  else {
    int i;

    /* loop pela encomenda para guardar qual o produto com maior quantidade  */
    for (i = 0; i < idencomenda; i++) {
      if (encomends[i].produtos[idp].qtd > qtdM) {
        maior = i;
        qtdM = encomends[i].produtos[idp].qtd;
      }
    }
    if (qtdM != 0) {
      printf("Maximo produto %d %d %d.\n", idp, maior, qtdM);
    }
  }
}

/* funcao auxiliar para a funcao merge sort que organiza os vetores depois de divididos */
void merge(produto v[], int l, int m, int r, int Tipo) {
  int i,j,k;
  int n1 = m - l + 1;
  int n2 = r - m;
  /* cria os vetores temporarios */
  produto L[TAMANHO_ID], R[TAMANHO_ID];

  /* copia os produtos para os vetores temporarios */
  for (i = 0; i < n1; i++) {
    L[i] = v[l+ i];
  }
  for (i = 0; i < n2; i++) {
    R[i] = v[m + 1 + i];
  }

  i = 0; /* indice do primeiro vetor */
  j = 0; /* indice do segundo vetor */
  k = l; /* indice inicial do vetor final */

  /* verifica se e um inteiro ou uma string */
  if (Tipo == INTEIRO) {
    while (i < n1 && j < n2) {
      if (L[i].preco <= R[j].preco) {
        v[k] = L[i];
        i++;
      }
      else {
        v[k] = R[j];
        j++;
      }
      k++;
    }
  }
  else {
    while (i < n1 && j < n2) {
      if (strcmp(L[i].ds, R[j].ds) <= 0) {
        v[k] = L[i];
        i++;
      }
      else {
        v[k] = R[j];
        j++;
      }
      k++;
    }
  }

  /* copia o resto do vetor maior */
  while (i < n1) {
    v[k] = L[i];
    i++;
    k++;
  }

  while (j < n2) {
    v[k] = R[j];
    j++;
    k++;
  }
}

/* funcao de organizacao de vetores mergesort que divide o vetor original ao meior
   recebe um indice para indicar se estamos a organizar uma string ou um inteiro */
void mergeSort(produto v[],int l,int r, int Tipo) {
  if (l < r) {

    /*  indice do meio do vetor */
    int m = l+(r-l)/2;

    /* organiza a primeira e a segunda metades*/
    mergeSort(v, l, m, Tipo);
    mergeSort(v, m+1, r, Tipo);

    merge(v, l, m, r, Tipo);
  }
}

/* cria uma lista de todos os produtos em stock organizados por preco */
void listaTodosProds() {
  produto v[TAMANHO_ID];
  int i;

  /* cria um novo vetor com todos os produtos */
  for (i = 0; i < idproduto; i++) {
    v[i] = prods[i];
  }

  /* organiza o vetor por maior quantidade */
  mergeSort(v, 0, idproduto-1, INTEIRO);

  printf("Produtos\n");
  for (i = 0; i < idproduto; i++) {
    printf("* %s %d %d\n", v[i].ds, v[i].preco, v[i].qtd);
  }
}

/* cria uma lista de todos os produtos numa encomenda selecionada organizados
   por ordem alfabetica da descricao */
void listaTodosProdsemEncomenda() {
  int ide, counter = 0;
  int i;
  produto v[TAMANHO_ID];

  scanf("%d", &ide);

  if (ide >= idencomenda) {
    printf("Impossivel listar encomenda %d. Encomenda inexistente.\n", ide);
  }
  else {
    /* cria um novo array com todos os produtos da encomenda */
    for (i = 0; i < idproduto; i++) {
      /* verifica se existe produto no indice que estamos a adicionar */
      if (encomends[ide].produtos[i].ds[0] != '\0') {
        v[counter] = encomends[ide].produtos[i];
        counter++;
      }
    }

    /* organiza o vetor */
    mergeSort(v, 0, counter -1, STRING);

    printf("Encomenda %d\n", ide);
    for (i = 0; i < counter; i++) {
      printf("* %s %d %d\n", v[i].ds, v[i].preco, v[i].qtd);
    }
  }
}

/* funcao principal que le o input do comando que queremos fazer */
int main() {
  /* inicializa a variavel de leitura */
  char c;

  do {
    switch (c = getchar()) {
      case 'a':
        novoProduto();
        break;
      case 'q':
        adicionaStock();
        break;
      case 'N':
        novaEncomenda();
        break;
      case 'A':
        adicionaProdEncomenda();
        break;
      case 'r':
        removeStock();
        break;
      case 'R':
        removeProdEncomenda();
        break;
      case 'C':
        calculaCusto();
        break;
      case 'p':
        alteraPreco();
        break;
      case 'E':
        listaDsQtdEmEncomenda();
        break;
      case 'm':
        listaProdemEncomenda();
        break;
      case 'l':
        listaTodosProds();
        break;
      case 'L':
        listaTodosProdsemEncomenda();
        break;
      default:
        break;
    }
    /* programa acaba quando escrevemos x */
  } while(c != 'x');
  return 0;
}
