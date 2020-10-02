#include <stdlib.h>
#include <string.h>
#include <stdio.h>

typedef struct wrestler  
{
	char* nome;
	double peso;

} *Wrestler; 


Wrestler newWrestler(int weight, const char* name);
void deleteWrestler(Wrestler wrestler);
int equalsWrestler(Wrestler self, Wrestler other);
void sleep(Wrestler self, int interval);
void figth(Wrestler self, Wrestler other, const char* msg);

Wrestler newWrestler(int weight, const char* name)
{
	Wrestler wrestler = (Wrestler) malloc(sizeof(struct wrestler));
	if (wrestler != NULL)
	{
		wrestler->nome = malloc(sizeof(char)*strlen(name));
		strcpy(wrestler->nome, name);
		wrestler->peso = weight;
	}

	return wrestler;
}

void deleteWrestler(Wrestler wrestler)
{
	if(wrestler)
	{
		free(wrestler->nome);
		free(wrestler);
	}
}

int equalsWrestler(Wrestler self, Wrestler other) 
{
	if (self == NULL || other == NULL ) return 0;
	return !strcmp(self->nome,other->nome) && self->peso == other->peso;
}

void sleep(Wrestler self, int interval)
{
	printf("%s dorme durante %d segundos \n", self->nome, interval);
}

void figth(Wrestler self, Wrestler other, const char* msg)
{
	printf("%s luta com %s e diz %s \n", self->nome, other->nome, msg);
}

int main(int argc, char const *argv[])
{
	Wrestler wrestler1 = newWrestler(40, "Manuel");
	Wrestler wrestler2 = newWrestler(35, "Joao");

	if(equalsWrestler(wrestler1, wrestler2)) printf(" sao iguais \n");
	else printf("nao sao iguais \n");

	sleep(wrestler1, 30);
	figth(wrestler1, wrestler2, "ola");

	deleteWrestler(wrestler1);
	deleteWrestler(wrestler2);
	
	
	return 0;
}