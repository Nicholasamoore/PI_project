============================
Processor Assembly Language
============================
As mentioned in the architecture section, the ARMv8-A supports both 32 and 64-bit instruction sets. For the purposes of this lab report, we will focus on the 64-bit architecture (referred to as A64). It is important to note that the assembler will choose the correct encoding of the same instruction based on the values of the operands.

Data Processing Instructions
=============================
* Arithmetic and Logical Operations
    - These include Arithmetic (ADD, SUB), Logical (AND, EOR), Comparison (CMP), and Move (MOV) instructions
    - Denoted by the instruction followed by the register and two operands
    - i.e. ADD X0, X1, #5    //X0 = X1 + 5
* Multiply and Divide Operations
    - Consists of multiply (MUL, MADD, MNEG) and divide (SDIV, UDIV) instructions
    - Denoted by the instruction followed by the register and two operands (or three in the case of MADD and MSUB)
    - i.e. MNEG X0, X1, X2    //X0 = -(X1 * X2)
* Shift Operations
    - Consists of Logical (LSL, LSR) and Arithmetic (ASR) instructions
    - Denoted by the instruction followed by the register
    - i.e. LSL X0    //X0 = X0 * 2
* Bitfield and Byte Maniuplation
    - Consists of Bitfield (SXTB, UXTB) and bit (RBIT, REV) manipulations
    - Denoted by the instruction followed by the destination register and the source register 
    - i.e. UXTB X0, W1    //Extend the register W1 to 64-bits and store in X0)  
* Conditional Instructions
    - Checks condition flags and conditionally performs instruction
    - Denoted by the instruction followed by two registers
    - i.e. CSET W0, EQ    //If the Z condition flag is set (previous comparison was 0) then W0 = 1, otherwise W0 = 0

Memory Access Instructions
===========================
* Consists of Load (LDR) and Store (STR) instructions
* Denoted by the instruction followed by the register and an address
* i.e. LDR X0, [X1, #8]    //Load from address X1 + 8 into X0

Flow Control
=============
* Consists of branch (CBZ, CBNZ) instructions
* Denoted by the instruction followed by the register and branch label
* i.e. CBNZ X0, label    //Branch to label if x0 != 0

Misc
====
* Contains system control and other instructions. Seems to be outside the scope of this class.
