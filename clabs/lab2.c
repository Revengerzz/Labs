/*comment*/
#include <stdio.h>
#include <math.h>

int main(void)
{
float a,x,g,f,y;
int word;
printf("Введите х ");
scanf("%f", &x);
printf("Введите a ");
scanf("%f", &a);
scanf("%i",&word);
switch(word)
{
    case 1:
        g = 9*(7*a*a-19*a*x+10*x*x)/(25*a*a+30*a*x+9*x*x);
        printf("g=%f\n\n",g);
        break;
    case 2:
        f = cos(9*a*a-13*a*x-10*x*x);
        printf("f=%f\n\n",f);
        break;
    case 3:
        y = log(-80*a*a-46*a*x+21*x*x+1);
        printf("y=%f\n\n",y);
        break;
    default:
        printf("неправильный ввод.\n");
}

}

