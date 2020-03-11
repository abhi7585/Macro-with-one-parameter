# Macro-with-one-parameter

Aim: Defining a macro with one argument, expansion of macro & generating expanded source code.

Instructions :
1) Write a ALP using few instructions & Macro calls with only one argument.
2) Define domain/body of the Macro (3-5 instructions)
3) Write a program which will replace each Macro call with its domain & performs expansion of the
Macro.
4) Show the input source code with Macro call & output the expanded source code
5) Also output the following statistics:
- Number of instructions in input source code (excluding Macro calls)
- Number of Macro calls
- Number of instructions defined in the Macro call
- Actual argument during each Macro call
- Total number of instructions in the expanded source code.

Input 1: Input Source code with Macro calls
```
MOV R
ABHISHEK 30
DCR R
AND R
ABHISHEK 55
MUL 88
HALT
```
Input 2: Macro definition
```
MACRO
ABHISHEK &ARG
ADD & ARG
SUB &ARG
OR &ARG
MEND
```
Output source code after Macro expansion:
```
MOV R
ADD 30
SUB 30
OR 30
DCR R
AND R
ADD 55
SUB 55
OR 55
MUL 88
HALT
```
Statistical output:
```
Number of instructions in input source code (excluding Macro calls) = 5
Number of Macro calls = 2
Number of instructions defined in the Macro call = 3
Actual argument during first Macro call “RAHUL” = 30
Actual argument during second Macro call “RAHUL” = 55
Total number of instructions in the expanded source code = 11
```
