#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include <conio.h>

#define MAX 20

void read_polynomial(char *poly, int p[]);
void poly_add(int p1[], int p2[], int p3[]);
void poly_multiply(int p1[], int p2[], int p3[]);
void poly_differentiate(int p1[], int p3[]);
int p1[MAX], p2[MAX], p3[MAX], p4[MAX];
char s[2] = {0};
int main()
{

  int i, k = 0, l = 0, m = 0;
  int expo1, expo2;

  char poly1[20];
  char poly2[20];
  char s[2] = {0};
  printf("please, enter the first polynomial: ");
  gets(poly1);
  printf("please, enter the second polynomial: ");
  gets(poly2);

  for (size_t i=0, j=0; poly2[j]=poly2[i]; j+=!isspace(poly2[i++]));
  for (size_t i=0, j=0; poly1[j]=poly1[i]; j+=!isspace(poly1[i++]));

  read_polynomial(poly1, p1);
  read_polynomial(poly2, p2);

  int option;

  do
  {
    printf("\nWhich operation you want to do? \n");
    printf("1) Add\n");
    printf("2) Multiply\n");
    printf("3) Differentiate first polynomial\n");
    printf("4) Differentiate second polynomial\n");
    printf("5) To exit.");

    scanf("%d", &option);

    switch(option){
      case 1: printf("Addition is: "); poly_add(p1, p2, p3);
              break;
      case 2:
              printf("Multiplication is: "); poly_multiply(p1, p2, p3);
              break;
      case 3: printf("Differentiation is: "); poly_differentiate(p1, p3);
              break;
      case 4: printf("Differentiation is: "); poly_differentiate(p2, p3);
              break;
    }
  } while(option != 5);
}
void read_polynomial(char *poly, int p[]){
  int k = 0;
  for(int i = 0, n = strlen(poly); i < n;)
  {
    if (poly[i] == '(' && poly[i+2] == ',')
    {
      s[0] = poly[i+1];
      p[poly[i + 3] - 48] = s[0] - 48;
      i += 3;
    }
    else if(poly[i] == '(' && poly[i+3] == ',')
    {
      s[0] = poly[i+1];
      int temp = atoi(s) * 10;
      s[0] = poly[i+2];
      temp += s[0];
      p[poly[i + 4] - 48] = temp;
      i += 4;
    }
    else i ++;
  }
}
void poly_add(int p1[], int p2[], int p3[])
{
  int last = 0;
  for(int i = 0; i < MAX; i++)
  {
    p3[i] = p1[i] + p2[i];
    if (p3[i] > 0) last = i;
  }
  printf("\n");
  for(int i = 0; i < MAX; i++)
  {
    if(p3[i] > 0)
    {
      if(i == 0)
      {
        printf("%d", p3[i]);
      }
      else if(i == 1)
      {
        printf("%dx", p3[i]);
      }
      else
      {
      printf("%dx**%d", p3[i], i);
      }
      if (i < last) printf(" + ");
    }
  }
    printf("\n");
}
void poly_multiply(int p1[], int p2[], int p3[])
{
  int last = 0;
  for(int i = 0; i < MAX; i++)
  {
    for(int j = 0; j < MAX; j++)
    {
      p3[i+j] += p1[i] * p2[j];
      if (p3[i] > 0) last = i;
    }
  }
  printf("\n");
  for(int i = 0; i < MAX; i++)
  {
    if(p3[i] > 0)
    {
      if(i == 0)
      {
        printf("%d", p3[i]);
      }
      else if(i == 1)
      {
        printf("%dx", p3[i]);
      }
      else
      {
      printf("%dx**%d", p3[i], i);
      }
      if (i < last) printf(" + ");
    }
  }
  printf("\n");
}

void poly_differentiate(int p1[], int p3[])
{
  int last = 0;
  for(int i = 0; i < MAX; i++)
  {
    p3[i-1] = p1[i] * i;
  }
  for (int i = 0; i < MAX; i ++)
    if (p3[i] > 0) last = i;

  printf("\n");
  for(int i = 0; i < MAX; i++)
  {
    if(p3[i] > 0)
    {
      if(i == 0)
      {
        printf("%d", p3[i]);
      }
      else if(i == 1)
      {
        printf("%dx", p3[i]);
      }
      else
      {
      printf("%dx**%d", p3[i], i);
      }
      if (i < last ) printf(" + ");
    }
  }
  printf("\n");
}
