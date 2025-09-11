#include<stdio.h>
#include<stdlib.h>

/* 1. Write a program in C to store n elements in an array and print the elements using a pointer.

Test Data:
Input the number of elements to store in the array :5
Input 5 number of elements in the array:
element 0:5
element 1:7
element 2:2
element 3:9
element 4:8

Expected Output:
The elements you entered are:
element 0:5
element 1:7
element 2:2
element 3:9
element 4:8 

*/

void printElements()
{
    int n = 0;
    printf("Input the number of elements to store in the array : ");
    scanf("%d", &n);

    int *arr = (int*)(malloc(sizeof(int) * n));

    for(int i=0; i<n; i++)
    {
        printf("element %d:", i);
        scanf("%d", &arr[i]);
    }

    printf("\nThe elements you entered are:\n");

    for(int i=0; i<n; i++)
    {
        printf("element %d: %d", i, arr[i]);
        printf("\n");
    }
}

void printElementsReverse()
{
    int n = 0;
    printf("Input the number of elements to store in the array : ");
    scanf("%d", &n);

    int *arr = (int*)(malloc(sizeof(int) * n));

    for(int i=0; i<n; i++)
    {
        printf("element %d:", i);
        scanf("%d", &arr[i]);
    }

    printf("\nThe elements you entered are:\n");

    for(int i=n-1; i>=0; i--)
    {
        printf("element %d: %d", i, arr[i]);
        printf("\n");
    }
}

/* 2. Write a program in C to print all permutations of a given string using pointers.

Expected Output:
The permutations of the string 'abcd' are:
abcd abdc acbd acdb adcb adbc bacd badc bcad bcda boca bdac cbad cbda cabd cadb cdab cdba dbca dbac dcba dcab dacb dabc

*/

void swap(char *x, char *y)
{
    char temp = *x;
    *x = *y;
    *y = temp;
}

void permutation(char *arr, int idx, int n)
{
    if(idx == n) { printf("%s ", arr); return; }
    for(int i=idx; i<n; i++)
    {
        swap(&arr[i], &arr[idx]);
        permutation(arr, idx+1, n);
        swap(&arr[i], &arr[idx]);
    }
}

/* 3. Print Factorial of a number.

Input: 5
Output: 120

*/

void factorial(int n)
{
    int fact = 1;
    for(int i=1; i<=n; i++) { fact = fact * i; }
    printf("%d ",fact);
}

/* 4. Sum of array elements 

Input: 1 2 3 4 5 6 7 8 9 10
Output: 55

*/

void sumOfElements(int *arr)
{
    int n = sizeof(arr)/sizeof(arr[0]), sum = 0;

    for(int i=0; i<n; i++) { sum = sum + arr[i]; }
    printf("Sum of elements of the array: %d",sum);
}

/* 5. Reverse the array elements 

Input: 1 2 3 4 5
Output: 5 4 3 2 1

*/

void reverseArray(int *arr)
{
    int n = sizeof(arr)/sizeof(arr[0]);
    for(int i=0; i<n/2; i++)
    {
        arr[i] = arr[i] ^ arr[n-i];
        arr[n-i] = arr[i] ^ arr[n-i];
        arr[i] = arr[i] ^ arr[n-i];
    }
}

/* 6. Bubble sort

Input: 3 1 5 2 4
Output: 1 2 3 4 5 

*/

void bubbleSort(int *arr)
{
    int n = sizeof(arr)/sizeof(arr[0]);

    for(int i=0; i<n; i++)
    {
        for(int j=0; j<n-i-1; j++)
        {
            if(arr[i] > arr[j])
            {
                arr[i] = arr[i] ^ arr[j];
                arr[j] = arr[i] ^ arr[j];
                arr[i] = arr[i] ^ arr[j];
            }
        }
    }
}

int main()
{
    // Program 1
    printElements();

    // Reverse printing
    printElementsReverse();

    // Program 2
    char arr[] = {'a','b','c','d'};
    int n = sizeof(arr)/sizeof(arr[0]);
    permutation(arr, 0, n);

    // Program 3
    factorial(5);

    // Program 4
    int nums[] = {1,2,3,4,5,6,7,8,9,10};
    sumOfElements(nums);

    // Program 5
    reverseArray(nums);

    // Program 6
    bubbleSort(nums);

    return 0;
}