/*comment*/
#include <stdio.h>
#include <math.h>

int main(void)
{
float a,x,g,f,y;
printf("Введите х ");
scanf("%f", &x);
printf("Введите a ");
scanf("%f", &a);

g = 9*(7*a*a-19*a*x+10*x*x)/(25*a*a+30*a*x+9*x*x);
f = cos(9*a*a-13*a*x-10*x*x);
y = log(-80*a*a-46*a*x+21*x*x+1);

printf("g=%f\n\n",g);
printf("f=%f\n\n",f);
printf("y=%f\n\n",y);
}
