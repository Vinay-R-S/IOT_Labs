#ifndef INIT_FUNCTIONS_H
#define INIT_FUNCTIONS_H

#include "code_a2_datatypes.h"

// Initialize message structures with some example data
void init_msgA(Msg_A *pMsgA);
void init_msgB(Msg_B *pMsgB);

// Print functions for generic and specific message types
void print_msg(void *pMsg);
void print_msgA(Msg_A *pMsgA);
void print_msgB(Msg_B *pMsgB);

#endif // INIT_FUNCTIONS_H
