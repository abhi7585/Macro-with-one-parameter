from sys import exit
motOpCode = ["MOV", "ADD", "SUB", "MUL", "DIV", "AND", "OR",
             "LOAD", "STORE", "DCR", "INC", "JMP", "JNZ", "HALT"]
keywords = ["MACRO", "CONST", "DOUBLE", "INT", "FLOAT", "SHORT", "LONG", "STRUCT", "IF", "ELSE", "FOR", "SWITCH",
            "CASE", "CHAR", "RETURN", "PRINTF", "SCANF", "AX", "BX", "CX", "DX", "AH", "BH", "CH", "DH", "AL", "BL", "CL", "DL"]
sourceCode = []
macroNames = []
macroDefinition = []
outputSourceCode = []
noOfInstructionSC = 0
noOfMacroCall = 0
noOfInstructionMC = 0
expandedCode = 0
values = []
argName = ''

mc = int(input("Enter the number of Macro Definition code line : "))
for i in range(mc):
    instruction = input("Enter Macro code instruction {} :". format(i+1))
    macroDefinition.append(instruction)
macroDefinition = [element.upper() for element in macroDefinition]

if macroDefinition[0] == "MACRO" and macroDefinition[-1] == "MEND": 
    temp = macroDefinition[1]
    macroName, argName = temp.split()
    if macroName not in keywords and macroName not in motOpCode:
        macroNames.append(macroName)
else:
    print("Invalid Macro Definition.")
    exit(0)

sc = int(input("Enter the number of Source code lines : "))
for i in range(sc):
    instruction = input("Enter Source code instruction {} : ". format(i+1))
    sourceCode.append(instruction)   
sourceCode = [element.upper() for element in sourceCode]
for i in range(sc):
    if macroName in sourceCode[i]:
        noOfMacroCall = noOfMacroCall + 1
    else:    
        noOfInstructionSC = noOfInstructionSC + 1

for i in range(sc):
    if macroName in sourceCode[i]: 
        noOfInstructionMC = 0
        temp = str(sourceCode[i])
        macroName, argValue = temp.split()
        if argValue not in values:
            values.append(argValue)  
        for j in range(2, mc-1):
            if argName in macroDefinition[j]:
                temp = macroDefinition[j]
                opCode, value  = temp.split()
                temp =  temp.replace(argName, argValue)
            outputSourceCode.append(temp)
            noOfInstructionMC = noOfInstructionMC + 1
    else:
        temp = sourceCode[i]
        outputSourceCode.append(temp)

print("Expanded Source Code is : ")
for i in outputSourceCode:
        print(i)
        expandedCode = expandedCode + 1

print()
print("No of instructions in input source code : {}".format(noOfInstructionSC))
print("No of macro call : {}".format(noOfMacroCall))
print("No of instructions defined in macro call : {}".format(noOfInstructionMC))
for i in range(len(values)):
    print("Actual arguement during {} Macro call 'ABHISHEK' = {}".format(i+1, values[i]))
print("Total number of isntructions in expanded code : {}".format(expandedCode))
