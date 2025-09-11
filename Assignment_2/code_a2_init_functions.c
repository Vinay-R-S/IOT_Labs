#include <stdio.h>
#include "code_a2_init_functions.h"

// Initialize Msg_A with some example values
void init_msgA(Msg_A *pMsgA)
{
    if (pMsgA == NULL)
        return;
    pMsgA->msg_type = MSG_A;
    pMsgA->iValue = 10;
    pMsgA->fValue = 20.5f;
    pMsgA->dValue = 30.25;
}

// Initialize Msg_B with some example values
void init_msgB(Msg_B *pMsgB)
{
    if (pMsgB == NULL)
        return;
    pMsgB->msg_type = MSG_B;
    pMsgB->iValue1 = 100;
    pMsgB->iValue2 = 200;
    pMsgB->fValue1 = 300.5f;
    pMsgB->dValue1 = 400.75;
    pMsgB->fValue2 = 500.25f;
    pMsgB->dValue2 = 600.125;
}

// Print a generic message based on msg_type
void print_msg(void *pMsg)
{
    if (pMsg == NULL)
        return;

    MSG_TYPE type = *((MSG_TYPE *)pMsg); // first field is msg_type

    if (type == MSG_A)
    {
        print_msgA((Msg_A *)pMsg);
    }
    else if (type == MSG_B)
    {
        print_msgB((Msg_B *)pMsg);
    }
    else
    {
        printf("Unknown message type.\n");
    }
}

// Print Msg_A contents
void print_msgA(Msg_A *pMsgA)
{
    if (pMsgA == NULL)
        return;
    printf("Msg_A:\n");
    printf("  iValue = %u\n", pMsgA->iValue);
    printf("  fValue = %.2f\n", pMsgA->fValue);
    printf("  dValue = %.3lf\n", pMsgA->dValue);
}

// Print Msg_B contents
void print_msgB(Msg_B *pMsgB)
{
    if (pMsgB == NULL)
        return;
    printf("Msg_B:\n");
    printf("  iValue1 = %u\n", pMsgB->iValue1);
    printf("  iValue2 = %u\n", pMsgB->iValue2);
    printf("  fValue1 = %.2f\n", pMsgB->fValue1);
    printf("  dValue1 = %.3lf\n", pMsgB->dValue1);
    printf("  fValue2 = %.2f\n", pMsgB->fValue2);
    printf("  dValue2 = %.3lf\n", pMsgB->dValue2);
}
