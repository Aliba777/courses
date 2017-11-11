#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include <conio.h>

#define MAX 20

typedef struct stack {
  int data[MAX];
  int top;
} stack;

void init(stack *s);
void push(stack *s, int x);
char pop(stack *s);
int top(stack *s);
bool isEmpty(stack *s);
bool isFull(stack *s);
int priority(char ch);

int main()
{
  char polynomial[20];
  stack operators;
  init(&operators);
  printf("Please, enter an infix notation: ");
  gets(polynomial);
  char ch;
  char s[2] = {0};
  // s[0] = poly[i+1];
  // int temp = atoi(s) * 10;
  // s[0] = poly[i+2];
  //char *p = "3 * X + (Y - 12) - Z";

  for (int i = 0, n = strlen(polynomial); i < n; i++) {
    if (isalnum(polynomial[i])) {
      printf("%c", polynomial[i]);
    }
    else
      if(polynomial[i] == '(') {
        push(&operators, '(');
      }
      else {
        if (polynomial[i] == ')') {
          while((ch = pop(&operators)) != '(')
            printf("%c", ch);
        }
        else {
            while(priority(polynomial[i]) <= priority(top(&operators)) && !isEmpty(&operators)) {
              ch = pop(&operators);
              printf("%c", ch);
          }
          push(&operators, polynomial[i]);
        }
      }
    }
  while(!isEmpty(&operators)) {
    ch = pop(&operators);
    printf("%c", ch);
  }
  printf("\nEnter any key to continue: ");
  getchar();
}

int priority(char ch) {
  if(ch == '(') {
    return(0);
  }
  if(ch == '+' || ch == '-') {
    return(1);
  }
  if(ch == '*' || ch == '/' || ch == '%') {
    return(2);
  }
  return(3);
}
void init(stack *s) {
  s->top =- 1;
}
void push(stack *s, int x) {
  s->top = s->top + 1;
  s->data[s->top] = x;
}
char pop(stack *s) {
  int x;
  x = s->data[s->top];
  s->top=s->top-1;

  return(x);
}
int top(stack *s) {
  return s->data[s->top];
}
bool isEmpty(stack *s) {
  return (s->top == -1);
}

bool isFull(stack *s) {
  return (s->top == MAX-1);
}
