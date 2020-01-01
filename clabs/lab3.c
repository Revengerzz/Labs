#include <stdio.h>
#include <math.h>
#include <locale.h>
int main (void)
{
setlocale(LC_ALL, "Rus");
float a, x, g, f, y, s;
int word, l, i = 0;

printf("Введите числа, не равные нулю:\n");
printf("Введите х: ");
scanf("%f", &x); printf("Введите a: "); scanf("%f", &a);

printf("Введите сколько считать: ");
scanf("%i",&l);

printf("Введите шаг: ");
scanf("%f",&s);

printf("1 - вычислить функцию G, 2 - вычислить функцию F, 3 - вычислить функцию Y:");
scanf("%i",&word);

for (i = 1; i <= l; i++)
    switch(word)
    {
        case 1:
            if ((25*a*a+30*a*x+9*x*x) == 0)
            {
                printf("ERROR");
                x += s;
                a += s;
            }
            else
            {
                g = 9*(7*a*a-19*a*x+10*x*x)/(25*a*a+30*a*x+9*x*x);
                printf("g=%f\n\n",g);
                x += s;
                a += s;
                break;
            }
        case 2:
            f = cos(9*a*a-13*a*x-10*x*x);
            printf("f=%f\n\n",f);
            x += s;
            a += s;
            break;
        case 3:
            if ((-80*a*a-46*a*x+21*x*x+1) <= 0)
            {
                printf("ERROR");
                x += s;
                a += s;
            }
            else
            {
                y = log(-80*a*a-46*a*x+21*x*x+1);
                printf("y=%f\n\n",y);
                x += s;
                a += s;
                break;
            }
        default:
            printf(" неправильный ввод.\n");
}
}
