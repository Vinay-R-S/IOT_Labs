#ifndef DATATYPES_H
#define DATATYPES_H

#include <stdint.h>

typedef enum
{
    MSG_A = 1,
    MSG_B = 2,
} MSG_TYPE;

typedef struct
{
    MSG_TYPE msg_type;
    uint32_t iValue;
    float fValue;
    double dValue;
} Msg_A;

typedef struct
{
    MSG_TYPE msg_type;
    uint32_t iValue1;
    uint32_t iValue2;
    float fValue1;
    double dValue1;
    float fValue2;
    double dValue2;
} Msg_B;

#endif // DATATYPES_H
