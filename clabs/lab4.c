#include <stdio.h>
#include <math.h>
#include <locale.h>
int main (void)
{
setlocale(LC_ALL, "Rus");
float a, x, g, f, y, s, mf[100], mg[100], my[100], mg_max = -10, mf_max = -10, my_max = -10;
int word, l, i, c = 0, op;

printf("Введите числа, не равные нулю:\n");
printf("Введите х: ");
scanf("%f", &x);

printf("Введите a: ");
scanf("%f", &a);

printf("Введите сколько считать: ");
scanf("%i",&l);

printf("Введите шаг: ");
scanf("%f",&s);

printf("1 - вычислить функцию G, 2 - вычислить функцию F, 3 - вычислить функцию Y:");
scanf("%i",&word);
for (i = 0; i <l; i++)
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
                if (mg_max < g)
                {
                    mg_max = g;
                }
                mg[i] = g;
                printf("g=%f\n\n",g);
                x += s;
                a += s;
                c += 1;
                break;
            }
        case 2:
            f = cos(9*a*a-13*a*x-10*x*x);
            if (mf_max < f)
                {
                    mf_max = f;
                }
            mf[i] = f;
            printf("f=%f\n\n",f);
            x += s;
            a += s;
            c += 1;
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
                if (my_max < y)
                {
                    my_max = y;
                }
                my[i] = y;
                printf("y=%f\n\n",y);
                x += s;
                a += s;
                c += 1;
                break;
            }
        default:
            printf(" неправильный ввод.\n");
    }

        printf("Способ вывода? (1-таблица, 2-строка: ");
        scanf("%d", &op);
        if ((op != 1) && (op != 2))
        {
            printf("ERROR");
        }
        else
        {
        switch(op)
        {
            case 1:
                if (word == 1)
                {
                    printf("Максимальный элемент массива: %d\n", mg_max);
                    for (i = 0; i < c; i++)
                        printf("%f\n", mg[i]);
                }
                if (word == 2)
                {
                    printf("Максимальный элемент массива: %d\n", mf_max);
                    for (i = 0; i < c; i++)
                        printf("%f\n", mf[i]);
                }
                if (word == 3)
                {
                    printf("Максимальный элемент массива: %d\n", my_max);
                    for (i = 0; i < c; i++)
                        printf("%f\n", my[i]);
                }
            case 2:
                if (word == 1)
                {
                    printf("Максимальный элемент массива: ", mg_max);
                    printf("\n");
                    for (i = 0; i < c; i++)
                        printf("%f ", mg[i]);
                }
                if (word == 2)
                {
                    printf("Максимальный элемент массива: ", mf_max);
                    printf("\n");
                    for (i = 0; i < c; i++)
                        printf("%f ", mf[i]);
                }
                if (word == 3)
                {
                    printf("Максимальный элемент массива: ", my_max);
                    printf("\n");
                    for (i = 0; i < c; i++)
                        printf("%f ", my[i]);
                }
        }
        }
}
