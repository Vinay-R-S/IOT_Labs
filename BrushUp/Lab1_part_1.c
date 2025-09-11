#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void Question1(void);
void Question2(void);
void Question3(void);
void Question4(void);
void Question5(void);

static int sGlobal = 100;
int *ipsGlobal = &sGlobal;

int main(void)
{

    int *ptrSLocal = (&sGlobal) + 2;
    // static int newStaticVar = 3000;

    // printf("size of int is %d\n", sizeof(int));

    printf("main: Ptr to sLocal from the main value is %p\n", ptrSLocal);
    printf("main: The value in sLocal before calling Question1() %d\n", *ptrSLocal);

    Question1();

    ptrSLocal = (&sGlobal) + 2;

    printf("main: The value in sLocal after calling Question1() %d\n", *ptrSLocal);

    printf("Going to call Question1() again ...\n");
    Question1();

    printf("main: The value in sLocal after calling Question1() 2nd time %d\n", *ptrSLocal);

    Question2();
    Question3();
    Question4();
    Question5();

    return 0;
}

void Question1(void)
{

    static int sLocal = 300;
    int *ipsLocal = &sLocal;

    printf("Q1: Value in sLocal on entry is %d\n", sLocal);
    printf("Q1: Addr of ipsLocal is %p\n", &ipsLocal);
    printf("Q1: Addr of sLocal is %p\n", &sLocal);
    printf("Q1: Addr of sGlobal is %p\n", &sGlobal);

    *ipsGlobal = *ipsLocal;

    ipsLocal = ipsGlobal; /* Now ipsLocal is made to point to ipsGlobal */

    (*ipsLocal)++;  /* Changing the sGlobal through ipsLocal pointer */
    (*ipsGlobal)++; /* Changing the same sGlobal through ipsGlobal pointer */

    sLocal = *ipsGlobal; /* Write back the value from the sGlobal to sLocal */

    printf("Q1: The value in sLocal before exiting is %d, sGlobal is %d\n", sLocal, sGlobal);
}

static struct
{
    float f;
    char c[4];
} fc1;

void Question2(void)
{

    fc1.f = 123.4;
    fc1.c[0] = 'A';
    fc1.c[1] = 'B';
    fc1.c[3] = 'C';

    printf("Q2: The values are f = %f, string %s \n", fc1.f, &fc1.c[0]);
}

struct
{
    int *ip;
    char *cp;
    float *fp;
} s1;
struct
{
    void *v1;
    void *v2;
    void *v3;
} s2;
struct
{
    int i;
    char c;
    float f;
} s3;

void Question3(void)
{

    s3.i = 100;
    s3.c = 'a';
    s3.f = 200.0;

    s2.v1 = (void *)&s3.i;
    s2.v2 = (void *)&s3.c;
    s2.v3 = (void *)&s3.f;

    memcpy(&s1, &s2, sizeof(s2)); /* memcpy(destptr, srcptr, len); */

    s3.i = (*s1.ip) + (*((int *)s2.v1)) + 1;

    s3.c = (*((char *)s2.v2)) + 1;

    s3.f = (*s1.fp) + (*((float *)s2.v3)) + 1;

    printf("Q3: The values are: i = %d f = %f c = %c \n", *s1.ip, *s1.fp, *s1.cp);
}

void Question4(void)
{

    static char cArr[16];
    /*  char cArr[16]; */
    int i = 0;

    while (i < 5)
    {
        cArr[i] = i + 'A';
        i++;
    }

    printf("Q4: The string is %s\n", cArr);
}

void Question5(void)
{

    static char cArr[10];
    float *fp;
    char *cp;
    int i = 0;

    while (i < 9)
    {
        cArr[i] = i + 'a';
        i++;
    }

    fp = (float *)cArr;

    fp++;

    cp = (char *)fp;
    *cp = *(char *)(fp + 1);

    printf("Q5: The string is %s\n", cArr);
}
