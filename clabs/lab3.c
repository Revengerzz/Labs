#include <stdio.h>
#include <math.h>
#include <locale.h>

int main (void)
{
setlocale(LC_ALL, "Rus");
float a,x,g,f,y;
int word;
printf("Введите числа, не равные нулю\n");
printf("Введите х ");
scanf("%f", &x);
printf("Введите a ");
scanf("%f", &a);
printf("1 - вычислить функцию G, 2 - вычислить функцию F, 3 - вычислить функцию Y:");
scanf("%i",&word);
if ((a == 0) && (x == 0)){
    printf("Всё плохо\n");}
else {
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
}

