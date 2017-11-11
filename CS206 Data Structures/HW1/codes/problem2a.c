#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdbool.h>
#include <conio.h>
#include <malloc.h>

#define MAX 20

int main(void)
{
    char polynomial[20];
    printf("Print a polynomial: ");
    gets(polynomial);
    int k = 0;
    char s[2] = {0};
    for (size_t i=0, j=0; polynomial[j]=polynomial[i]; j+=!isspace(polynomial[i++]));

    for(int i = 0, n = strlen(polynomial); i < n; i++)
    {
      if (polynomial[i] == 'x')
      {
        while(k < i)
        {
          printf("%c",polynomial[k]);
          k++;
        }
        k += 2;
        s[0] = polynomial[i+1];
        if(atoi(s) > 1)
        {
          printf("%c**%c%c", polynomial[i], polynomial[i+1], polynomial[i+2]);
        }
        else if (atoi(s) == 0) {
          continue;
        }
        else
        {
          printf("%c%c", polynomial[i], polynomial[i+2]);
        }
        i += 2;
        k += 1;
      }
    }
    printf("\n\nEnter any key to exit");
    getchar();
}
