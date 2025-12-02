#include <stdio.h>

int main()
{

  int a;
  int b;
  int c;
  int somma;
  int media;

  printf("inserisci il primo numero ");
  scanf("%d", &a);

  printf("inserisci il secondo numero ");
  scanf("%d", &b);

  printf("inserisci il terzo numero ");
  scanf("%d", &c);

  somma = a + b + c; // sommo

  media = somma / 3.0; // divido per i numeri che ho

  printf("il risultato è: %d", media);

  return 0;
}
