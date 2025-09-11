#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h> /* For using bool type in Q11 */

int function1(int *);
int *function2(int *);

void Question6(void);
void Question7(void);
void Question8(void);
void Question9(void);
void Question10(void);
void Question11(void);
void Question12(void); /* New function */

void myFunction(int *);

int main(void)
{

    int i = 0;

    i++;
    printf("Hello world! %d \n", i);
    i++;

    Question6();
    Question7();
    Question8();
    Question9();
    Question10();
    Question11();
    Question12(); /* Call new question */

    return 0;
}

void myFunction(int *ip)
{
    printf(" %d", *ip);

    if (!*ip)
        return;

    *ip = *ip - 1;

    myFunction(ip);
}

void Question6(void)
{
    int i = 10;
    int *intp = &i;

    printf("Q6: The values are ");

    myFunction(intp);

    printf("\n");
}

int function1(int *ip)
{
    function2(ip);
    *ip = (*ip) + (*ip);
    return *ip;
}

int *function2(int *q)
{
    *q = *q + *q + 5;
    return q;
}

void Question7(void)
{
    int i = 10;
    printf("Q7: The value is %d \n", function1(function2(function2(&i))));
}

void Question8(void)
{

    int iArr[5][2];
    int i = 0;
    int *ip = (int *)iArr;

    while (i < 10)
    {
        *ip = i;
        i++;
        ip++;
    }

    printf("Q8: The values are %d and %d\n", iArr[1][1], iArr[4][1]);
}

void Question9(void)
{

    static int si = 1;
    volatile int vi = 2;
    const int ci = 3;
    int i = 4;

    si++;
    vi++;
    i++;

    si = vi = i = si + vi + ci + i;

    printf("Q9: The values of si = %d vi = %d ci = %d i = %d\n", si, vi++, ci, ++i);
}

void Question10(void)
{

    static union
    {
        short s;
        char c[2];
    } usc;

    usc.s = 0x55FF;

    if (usc.c[1] == 0b01010101)
        printf("Q10: It is true \n");
    else
        printf("Q10: It is false \n");
}

int passBack(int a, int b)
{

    bool flag = true;
    int retVal;
    int *ipa = &a;

    if (&a < &b)
        flag = false;

    if (flag)
        ipa--;
    else
        ipa++;

    retVal = *ipa;

    return retVal;
}

void Question11(void)
{

    int i = 10;
    int j = 20;
    printf("Q11_1: The value returned is %d\n", passBack(i, j));

    i = 100;
    j = 200;
    printf("Q11_2: The value returned is %d\n", passBack(i, j));
}

/* -----------------------
   NEW Question 12
   ----------------------- */
void swapStrings(char **p1, char **p2)
{
    char *temp = *p1;
    *p1 = *p2;
    *p2 = temp;
}

void Question12(void)
{
    char *str1 = "Pointer";
    char *str2 = "Magic";
    char *ptrArray[2];

    ptrArray[0] = str1;
    ptrArray[1] = str2;

    printf("Q12_Before: str1 = %s, str2 = %s\n", ptrArray[0], ptrArray[1]);

    /* Swap using pointer-to-pointer */
    swapStrings(&ptrArray[0], &ptrArray[1]);

    printf("Q12_After:  str1 = %s, str2 = %s\n", ptrArray[0], ptrArray[1]);
}