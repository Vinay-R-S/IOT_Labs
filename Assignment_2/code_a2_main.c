#include <stdio.h>
#include <stdlib.h>
#include "code_a2_datatypes.h"
#include "code_a2_my_globals.h"
#include "code_a2_init_functions.h"

// Define global message pointer array
void *g_message_array[10];

int main()
{
    // Allocate 5 Msg_A and 5 Msg_B dynamically
    for (int i = 0; i < 5; i++)
    {
        Msg_A *pMsgA = (Msg_A *)malloc(sizeof(Msg_A));
        if (pMsgA == NULL)
        {
            printf("Memory allocation failed for Msg_A\n");
            return 1;
        }
        init_msgA(pMsgA);
        g_message_array[i] = (void *)pMsgA;
    }

    for (int i = 5; i < 10; i++)
    {
        Msg_B *pMsgB = (Msg_B *)malloc(sizeof(Msg_B));
        if (pMsgB == NULL)
        {
            printf("Memory allocation failed for Msg_B\n");
            return 1;
        }
        init_msgB(pMsgB);
        g_message_array[i] = (void *)pMsgB;
    }

    // Print all messages using generic print function
    for (int i = 0; i < 10; i++)
    {
        print_msg(g_message_array[i]);
        printf("\n");
    }

    // Free allocated memory
    for (int i = 0; i < 10; i++)
    {
        free(g_message_array[i]);
        g_message_array[i] = NULL;
    }

    return 0;
}
