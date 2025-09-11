#include <stdio.h>
#include <stdarg.h>

// Print an integer val using putchar(), return number of chars printed
int my_print_int(int val)
{
    int count = 0;
    char buffer[12]; // enough for 32-bit int + sign + null terminator
    int i = 0;
    int is_negative = 0;

    if (val == 0)
    {
        putchar('0');
        return 1;
    }

    if (val < 0)
    {
        is_negative = 1;
        val = -val;
    }

    // Convert integer to string in reverse order
    while (val > 0)
    {
        buffer[i++] = (val % 10) + '0';
        val /= 10;
    }

    if (is_negative)
    {
        buffer[i++] = '-';
    }

    // Print the string in correct order
    for (int j = i - 1; j >= 0; j--)
    {
        putchar(buffer[j]);
        count++;
    }

    return count;
}

// my_printf implementation
int my_printf(const char *fmt, ...)
{
    va_list args;
    int cnt, total_chars_printed = 0;

    // Print the format string using printf (allowed)
    printf("%s", fmt);

    va_start(args, fmt);

    // Read count of integers to print
    cnt = va_arg(args, int);

    // Loop through integers and print them using my_print_int
    for (int i = 0; i < cnt; i++)
    {
        int val = va_arg(args, int);

        // Print space before each number except first for readability
        if (i > 0)
        {
            putchar(' ');
            total_chars_printed++;
        }

        total_chars_printed += my_print_int(val);
    }

    va_end(args);

    // Print newline for formatting after all integers
    putchar('\n');

    return total_chars_printed;
}

// Example usage
int main()
{
    int param1 = 0x1111, param2 = 0x2222, param3 = 0x3333, param4 = 0x4444;
    int cnt;

    cnt = 1;
    my_printf("Passing one param\n", cnt, param1);

    cnt = 2;
    my_printf("Passing two params\n", cnt, param1, param2);

    cnt = 3;
    my_printf("Passing three params\n", cnt, param1, param2, param3);

    cnt = 4;
    my_printf("Passing four params\n", cnt, param1, param2, param3, param4);

    return 0;
}
