# Skeleton Program for the AQA AS Summer 2023 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in a Python 3 environment

# Version number: 0.0.0

"""
ERROR CODES

Error code 1:The file doesnt exist

Error code 2:The loaded file cannot be read correctly 

Error code 3:The Opcode is not in SymbolTable

Error code 4:There is no colon after the opcode.

Error code 5:The opcode is an empty string

Error code 6:The operand isnt an integer

Error code 7:The number of lines stored in SourceCode[0] is empty.

Error code 8:The number of lines stored in SourceCode[0] is empty.

Error code 9:The number of lines stored in SourceCode[0] is empty.

Error code 10:The operand value is 0, meaning the code hasnt been Assembled properly

Error code 11:The opcode is "ERR", meaning there is an error.
"""

"""
Register Array

Registers[0]=PC
Registers[1]=ACC
Registers[2]= The value of the status register in denary
Registers[3]=TOS
Registers[4]=ERR
"""

EMPTY_STRING = ""
HI_MEM = 20
MAX_INT = 127  # 8 bits available for operand (two's complement integer)
PC = 0
ACC = 1
STATUS = 2
TOS = 3
ERR = 4

#SourceCode


class AssemblerInstruction:
    def __init__(self):
        self.OpCode = EMPTY_STRING
        self.OperandString = EMPTY_STRING
        self.OperandValue = 0


def DisplayMenu():
    print()
    print("Main Menu")
    print("=========")
    print("L - Load a program file")
    print("D - Display source code")
    print("E - Edit source code")
    print("A - Assemble program")
    print("R - Run the program")
    print("X - Exit simulator")
    print()


def GetMenuOption():
    """
       Parameters:
       Return type:string
       Description:It makes sure that the users inputs are only 1 character.
    """
    Choice = EMPTY_STRING
    while len(Choice) != 1:
        Choice = input("Enter your choice: ")
    
    return Choice[0]


def ResetSourceCode(SourceCode):
    """
       Parameters: Array
       Return type: Array
       Description: Resets the array SourceCode so it is filled with spaces.
    """
    for LineNumber in range(HI_MEM):
        SourceCode[LineNumber] = EMPTY_STRING
    return SourceCode


def ResetMemory(Memory):
    """
       Parameters:
       Return type: Array
       Description: Resets the Memory array
    """
    for LineNumber in range(HI_MEM):
        Memory[LineNumber].OpCode = EMPTY_STRING
        Memory[LineNumber].OperandString = EMPTY_STRING
        Memory[LineNumber].OperandValue = 0
    return Memory


def DisplaySourceCode(SourceCode):
    """
       Parameters: Array
       Return type:
       Description: first value of SourceCode represents the number of lines. It then formats each line of the SourceCode
    """
    print()
    NumberOfLines = int(SourceCode[0])
    for LineNumber in range(0, NumberOfLines + 1):
        print("{:>2d} {:<40s}".format(LineNumber, SourceCode[LineNumber]))
    print()


def LoadFile(SourceCode):
    """
       Parameters: Array
       Return type: Array
       Description: Resets SourceCode. Asks user to input a file. Then uses exception handling to check if file exists. Then it checks how many lines SourceCode has and it
       transfers the contents of each line of the file into each index position of SourceCode. Error code 1 is if the file doesnt exist. Error code 2 is . If there are no errors
       DisplaySourceCode is called.
    """
    FileExists = False
    SourceCode = ResetSourceCode(SourceCode)
    LineNumber = 0
    FileName = input("Enter filename to load: ")
    try:
        FileIn = open(FileName + ".txt", 'r')
        FileExists = True
        Instruction = FileIn.readline()
        while Instruction != EMPTY_STRING:
            LineNumber += 1
            SourceCode[LineNumber] = Instruction[:-1]
            Instruction = FileIn.readline()
        FileIn.close()
        SourceCode[0] = str(LineNumber)
    except:
        if not FileExists:
            print("Error code 1:The file doesnt exist")
        else:
            print("Error code 2:The loaded file cannot be read correctly ")
            SourceCode[0] = str(LineNumber - 1)
    if LineNumber > 0:
        DisplaySourceCode(SourceCode)
    return SourceCode


def EditSourceCode(SourceCode):
    """
       Parameters: Array
       Return type: Array
       Description: Asks user the line number they want to edit and prints that line number. C=Cancel edit.  Ensures user enters a valid input. If user wants to edit they will
       be asked to enter a new line.
    """
    LineNumber = int(input("Enter line number of code to edit: "))
    print(SourceCode[LineNumber])
    Choice = EMPTY_STRING
    while Choice != "C":
        Choice = EMPTY_STRING
        while Choice != "E" and Choice != "C":
            print("E - Edit this line")
            print("C - Cancel edit")
            Choice = input("Enter your choice: ")
        if Choice == "E":
            SourceCode[LineNumber] = input("Enter the new line: ")
        DisplaySourceCode(SourceCode)
    return SourceCode


def UpdateSymbolTable(SymbolTable, ThisLabel, LineNumber):
    """
       Parameters: Dictionary, string, integer
       Return type: Dictionary
       Description: updates the symbol table by adding the label to it(key) followed by the line number it appears in(value).
    """
    if ThisLabel in SymbolTable:
        print("Error code 3:The Opcode is not in SymbolTable")
    else:
        SymbolTable[ThisLabel] = LineNumber
    return SymbolTable


def ExtractLabel(Instruction, LineNumber, Memory, SymbolTable):
    """
       Parameters: String, integer, Array, dictionary
       Return type: Dictionary, Array
       Description: This label is the name of the label e.g. NUM1, NUM2 START etc. .strip() removes any spaces from the string. Error code 4 is if the 5th character/ the
       character after the label isnt a colon. 
    """
    if len(Instruction) > 0:
        ThisLabel = Instruction[0:5]
        ThisLabel = ThisLabel.strip()
        if ThisLabel != EMPTY_STRING:
            if Instruction[5] != ':':
                print("Error code 4:There is no colon after the opcode.")
                Memory[0].OpCode = "ERR"
            else:
                SymbolTable = UpdateSymbolTable(SymbolTable, ThisLabel, LineNumber)
    return SymbolTable, Memory


def ExtractOpCode(Instruction, LineNumber, Memory):
    """
       Parameters: String, integer
       Return type: Array
       Description: This extracts the opcode which is index position 7-9 of each line that has an opcode.  then if tehre is an adsress mode it adds it to the opcode.
       Error code 5 is when the opcode is an empty string.
    """
    if len(Instruction) > 9:
        OpCodeValues = ["LDA", "STA", "LDA#", "HLT", "ADD", "JMP", "SUB", "CMP#", "BEQ", "SKP", "JSR", "RTN", "   "]
        Operation = Instruction[7:10]
        if len(Instruction) > 10:
            AddressMode = Instruction[10:11]
            if AddressMode == '#':
                Operation += AddressMode
        if Operation in OpCodeValues:
            Memory[LineNumber].OpCode = Operation
        else:
            if Operation != EMPTY_STRING:
                print("Error code 5:The opcode is an empty string")
                Memory[0].OpCode = "ERR"
    return Memory


def ExtractOperand(Instruction, LineNumber, Memory):
    """
       Parameters: String, Integer
       Return type: Array
       Description: Extracts the operand by extracting from index 12 onwards. the for loop to loop through the operand and if it sees an * ThisPosition=-1. Therefore [:ThisPosition]
       will retrun everything apart from the asterix. If there is no asterix then it will just return the operand. Then the spaces are removed from the operand using .strip()
    """
    if len(Instruction) >= 13:
        Operand = Instruction[12:]
        ThisPosition = -1
        for Position in range(len(Operand)):
            if Operand[Position] == '*':
                ThisPosition = Position
        if ThisPosition >= 0:
            Operand = Operand[:ThisPosition]
        Operand = Operand.strip()
        Memory[LineNumber].OperandString = Operand
    return Memory


def PassOne(SourceCode, Memory, SymbolTable):
    """
       Parameters: Array, , Dictionary
       Return type: Array, Dictionary
       Description: Transfers SoruceCode into Instruction. It then extracts label, Opcode and operand
    """
    NumberOfLines = int(SourceCode[0])
    for LineNumber in range(1, NumberOfLines + 1):
        Instruction = SourceCode[LineNumber]
        SymbolTable, Memory = ExtractLabel(Instruction, LineNumber, Memory, SymbolTable)
        Memory = ExtractOpCode(Instruction, LineNumber, Memory)
        Memory = ExtractOperand(Instruction, LineNumber, Memory)
    return Memory, SymbolTable


def PassTwo(Memory, SymbolTable, NumberOfLines):
    """
       Parameters:Array, Dictionary, Integer
       Return type:Array
       Description: Goes through each line and checks if operand is in symbol table and intitialises operand value to its value in the symbol table.
       It then chcecks if the operand is an inetegr if it isnt an error code is produced.
    """
    for LineNumber in range(1, NumberOfLines + 1):
        Operand = Memory[LineNumber].OperandString
        if Operand != EMPTY_STRING:
            if Operand in SymbolTable:
                OperandValue = SymbolTable[Operand]
                Memory[LineNumber].OperandValue = OperandValue
            else:
                try:
                    OperandValue = int(Operand)
                    Memory[LineNumber].OperandValue = OperandValue
                except:
                    print("Error code 6:The operand isnt an integer")
                    Memory[0].OpCode = "ERR"
    return Memory


def DisplayMemoryLocation(Memory, Location):
    """
       Parameters:Array,Integer
       Return type:
       Description: Displays the opcode and operand value.
    """
    print("*  {:<5s}{:<5d} |".format(Memory[Location].OpCode, Memory[Location].OperandValue), end='')


def DisplaySourceCodeLine(SourceCode, Location):
    """
       Parameters:Array, Integer
       Return type:
       Description:Displays the location and the line of the SourceCode which corresponds
       to that location. It does this for each location.
    """
    print(" {:>3d}  |  {:<40s}".format(Location, SourceCode[Location]))


def DisplayCode(SourceCode, Memory):
    """
       Parameters: Array, Array
       Return type:
       Description: This prints out the code in each frame
    """
    print("*  Memory     Location  Label  Op   Operand Comment")
    print("*  Contents                    Code")
    NumberOfLines = int(SourceCode[0])
    DisplayMemoryLocation(Memory, 0)
    print("   0  |")
    for Location in range(1, NumberOfLines + 1):
        DisplayMemoryLocation(Memory, Location)
        DisplaySourceCodeLine(SourceCode, Location)


def Assemble(SourceCode, Memory):
    """
       Parameters:Array, Array
       Return type:Array
       Description:Resets Memory array. Initialises symbol table. SourceCode[0] is the number of lines in the code.If there is no Error in the code it sets the opcode in Memory[0] to
       JMP. It then also sets the operand in Memory[0] to the value of START in the dictionary SymbolTable. If there is no start then the operand value is set to 1. It assembles the code
       by passing Memory and Symbol table through the subroutines PassOne and PassTwo.
    """
    Memory = ResetMemory(Memory)
    NumberOfLines = int(SourceCode[0])
    SymbolTable = {}
    Memory, SymbolTable = PassOne(SourceCode, Memory, SymbolTable)
    if Memory[0].OpCode != "ERR":
        Memory[0].OpCode = "JMP"
        if "START" in SymbolTable:
            Memory[0].OperandValue = SymbolTable["START"]
        else:
            Memory[0].OperandValue = 1
        Memory = PassTwo(Memory, SymbolTable, NumberOfLines)
    return Memory


def ConvertToBinary(DecimalNumber):
    """
       Parameters: Integer
       Return type: String
       Description: Converts a denary number to binary.
    """
    BinaryString = EMPTY_STRING
    while DecimalNumber > 0:
        Remainder = DecimalNumber % 2
        Bit = str(Remainder)
        BinaryString = Bit + BinaryString
        DecimalNumber = DecimalNumber // 2
    while len(BinaryString) < 4:
        BinaryString = '0' + BinaryString
    return BinaryString


def ConvertToDecimal(BinaryString):
    """
       Parameters: String
       Return type: Integer
       Description: Returns the decimal equivalent of the binary string
    """
    DecimalNumber = 0
    for Bit in BinaryString:
        BitValue = int(Bit)
        DecimalNumber = DecimalNumber * 2 + BitValue
    return DecimalNumber


def DisplayFrameDelimiter(FrameNumber):
    """
       Parameters:Integer
       Return type:
       Description: This displays the background of each frame if frame number == -1. This means
       that the previous frame has been displayed correctly.
    """
    if FrameNumber == -1:
        print("***************************************************************")
    else:
        print("****** Frame", FrameNumber, "************************************************")


def DisplayCurrentState(SourceCode, Memory, Registers):
    """
       Parameters:Array, Array, Array
       Return type:
       Description: This displays the code in each frame and the current state of the PC, ACC AND TOS.
    """
    print("*")
    DisplayCode(SourceCode, Memory)
    print("*")
    print("*  PC: ", Registers[PC], " ACC: ", Registers[ACC], " TOS: ", Registers[TOS])
    print("*  Status Register: ZNVC")
    print("*                  ", ConvertToBinary(Registers[STATUS]))                   
    DisplayFrameDelimiter(-1)


def SetFlags(Value, Registers):
    """
       Parameters: Integer, Array
       Return type: Array
       Description: if value is 0 then z flag is set to 0. if value is negative then n flag is set to 1. if there is an overflow then the V flag is set.
    """
    Carry=0
    if Value == 0:
        Registers[STATUS] = ConvertToDecimal("1000")
    elif Value < 0:
        Registers[STATUS] = ConvertToDecimal("0100")
    elif Value > MAX_INT or Value < -(MAX_INT + 1):
        Registers[STATUS] = ConvertToDecimal("0011")
        if Value>MAX_INT:
            Carry=Value-MAX_INT
        else:
            Carry=-(MAX_INT+1)-Value
        Registers[ACC]=MAX_INT
        print(f"ACC: {MAX_INT}")
        print(f"Carry: {Carry}")
        print(f"Final Value: {MAX_INT}+{Carry}={MAX_INT+Carry}")
        print("")
    else:
        Registers[STATUS] = ConvertToDecimal("0000")
    return Registers


def ReportRunTimeError(ErrorMessage, Registers):
    """
       Parameters: String, Array
       Return type: Array
       Description: If the program runs for too long it produces an error message.
    """
    print("Run time error:", ErrorMessage)
    Registers[ERR] = 1
    return Registers


def ExecuteLDA(Memory, Registers, Address):
    """
       Parameters:Array, Array, Integer
       Return type:Array
       Description:Stores the operand value which corresponds to the memory address number
       in the ACC.
    """
    Registers[ACC] = Memory[Address].OperandValue
    Registers = SetFlags(Registers[ACC], Registers)
    return Registers


def ExecuteSTA(Memory, Registers, Address):
    """
       Parameters:Array, Array, Integer
       Return type:Array
       Description: Stores the operand value in the accumulator.
    """
    Memory[Address].OperandValue = Registers[ACC]
    return Memory


def ExecuteLDAimm(Registers, Operand):
    """
       Parameters:Array, Integer
       Return type:Array
       Description:Loads the operand value into the accumulator. Changes the flag according
       to what the operand value is.
    """
    Registers[ACC] = Operand
    Registers = SetFlags(Registers[ACC], Registers)
    return Registers


def ExecuteADD(Memory, Registers, Address):
    """
       Parameters:Array, Array, Integer
       Return type:Array
       Description: Adds what is in the accumulator to the operand value. Sets a flag according
       to the result in the ACC. If the V flag is set to 1, then thre is an overflow.
    """
    Registers[ACC] = Registers[ACC] + Memory[Address].OperandValue
    Registers = SetFlags(Registers[ACC], Registers)
    return Registers


def ExecuteSUB(Memory, Registers, Address):
    """
       Parameters:Array, Array, Integer
       Return type:Array
       Description:Subtracts the operand value from the accumulator. Sets a flag according to
       the result in the ACC. If the V flag is set to 1, then there is an overflow
    """
    Registers[ACC] = Registers[ACC] - Memory[Address].OperandValue
    Registers = SetFlags(Registers[ACC], Registers)
    if Registers[STATUS] == ConvertToDecimal("0011"):
        ReportRunTimeError("Overflow", Registers)
    return Registers


def ExecuteCMPimm(Registers, Operand):
    """
       Parameters:Array, Integer
       Return type:Array
       Description: Compares by finding the differemce between the acc value and the operand
    """
    Value = Registers[ACC] - Operand
    Registers = SetFlags(Value, Registers)
    return Registers


def ExecuteBEQ(Registers, Address):
    """
       Parameters:Array,Integer
       Return type:Array
       Description: If the ACC and operand value are equal it assigns the value in the PC
       the address number it should branch to.
    """
    StatusRegister = ConvertToBinary(Registers[STATUS])
    FlagZ = StatusRegister[0]
    if FlagZ == "1":
        Registers[PC] = Address
    return Registers


def ExecuteJMP(Registers, Address):
    """
       Parameters:Array, Integer
       Return type:Array
       Description:It assigns the value in the PC to the correct address number
    """
    Registers[PC] = Address
    return Registers


def ExecuteSKP():
    return


def DisplayStack(Memory, Registers):
    """
       Parameters:Array, Array
       Return type:
       Description: prints out the contents of the stack
    """
    print("Stack contents:")
    print(" ----")
    for Index in range(Registers[TOS], HI_MEM):
        print("|{:>3d} |".format(Memory[Index].OperandValue))
    print(" ----")


def ExecuteJSR(Memory, Registers, Address):
    """
       Parameters:Array, Array, Array
       Return type:Array, Array
       Description: Assigns a value to the PC(Top of stack minus 1)which is the address number
       of the subroutine that is going to jump to. JSR- jumps to the subroutine.
    """
    StackPointer = Registers[TOS] - 1
    Memory[StackPointer].OperandValue = Registers[PC]
    Registers[PC] = Address
    Registers[TOS] = StackPointer
    DisplayStack(Memory, Registers)
    return Memory, Registers


def ExecuteRTN(Memory, Registers):
    """
       Parameters:Array,Array
       Return type:Array
       Description: Returns from the current subroutine and assigns the correct value to the PC
    """
    StackPointer = Registers[TOS]
    Registers[TOS] += 1
    Registers[PC] = Memory[StackPointer].OperandValue
    return Registers


def Execute(SourceCode, Memory):
    """
       Parameters: Array, Array
       Return type:
       Description: Initialises the array Registers. Displays the frame, the code, the contents of the CIR
       for each line of code.It executes the opcode which is in that line of code. If Registers[ERR]=0
       (there is no error), it will display the current state of each frame. This is repeated until HLT is
       seen in the code.
       
    """
    Registers = [0, 0, 0, 0, 0]
    Registers = SetFlags(Registers[ACC], Registers)
    Registers[PC] = 0
    Registers[TOS] = HI_MEM
    FrameNumber = 0
    DisplayFrameDelimiter(FrameNumber)
    DisplayCurrentState(SourceCode, Memory, Registers)
    OpCode = Memory[Registers[PC]].OpCode
    while OpCode != "HLT":
        FrameNumber += 1
        print()
        DisplayFrameDelimiter(FrameNumber)
        Operand = Memory[Registers[PC]].OperandValue
        print("*  Current Instruction Register: ", OpCode, Operand)
        Registers[PC] = Registers[PC] + 1
        if OpCode == "LDA":
            Registers = ExecuteLDA(Memory, Registers, Operand)
        elif OpCode == "STA":
            Memory = ExecuteSTA(Memory, Registers, Operand)
        elif OpCode == "LDA#":
            Registers = ExecuteLDAimm(Registers, Operand)
        elif OpCode == "ADD":
            Registers = ExecuteADD(Memory, Registers, Operand)
        elif OpCode == "JMP":
            Registers = ExecuteJMP(Registers, Operand)
        elif OpCode == "JSR":
            Memory, Registers = ExecuteJSR(Memory, Registers, Operand)
        elif OpCode == "CMP#":
            Registers = ExecuteCMPimm(Registers, Operand)
        elif OpCode == "BEQ":
            Registers = ExecuteBEQ(Registers, Operand)
        elif OpCode == "SUB":
            Registers = ExecuteSUB(Memory, Registers, Operand)
        elif OpCode == "SKP":
            ExecuteSKP()
        elif OpCode == "RTN":
            Registers = ExecuteRTN(Memory, Registers)
        if Registers[ERR] == 0:
            OpCode = Memory[Registers[PC]].OpCode
            DisplayCurrentState(SourceCode, Memory, Registers)
        else:
            OpCode = "HLT"
    print("Execution terminated")


def AssemblerSimulator():
    """
       Parameters:
       Return type:
       Description: intialises SourceCode and Memory and resets both of them. Calls the following subroutines based upton the user inputs. 
    """
    SourceCode = [EMPTY_STRING for Lines in range(HI_MEM)]
    Memory = [AssemblerInstruction() for Lines in range(HI_MEM)]
    SourceCode = ResetSourceCode(SourceCode)
    Memory = ResetMemory(Memory)
    Finished = False
    while not Finished:
        DisplayMenu()
        MenuOption = GetMenuOption()
        if MenuOption == 'L':
            SourceCode = LoadFile(SourceCode)
            Memory = ResetMemory(Memory)
        elif MenuOption == 'D':
            if SourceCode[0] == EMPTY_STRING:
                print("Error code 7:The number of lines stored in SourceCode[0] is empty.")
            else:
                DisplaySourceCode(SourceCode)
        elif MenuOption == 'E':
            if SourceCode[0] == EMPTY_STRING:
                print("Error code 8:The number of lines stored in SourceCode[0] is empty.")
            else:
                SourceCode = EditSourceCode(SourceCode)
                Memory = ResetMemory(Memory)
        elif MenuOption == 'A':
            if SourceCode[0] == EMPTY_STRING:
                print("Error code 9:The number of lines stored in SourceCode[0] is empty.")
            else:
                Memory = Assemble(SourceCode, Memory)
        elif MenuOption == 'R':
            if Memory[0].OperandValue == 0:
                print("Error code 10:The operand value is 0, meaning the code hasnt been Assembled properly")
            elif Memory[0].OpCode == "ERR":
                print("Error code 11:The opcode is ERR, meaning there is an error.")
            else:
                Execute(SourceCode, Memory)
        elif MenuOption == 'X':
            Finished = True
        else:
            print("You did not choose a valid menu option. Try again")
    print("You have chosen to exit the program")


if __name__ == "__main__":
    AssemblerSimulator()
