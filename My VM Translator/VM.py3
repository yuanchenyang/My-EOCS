#!/usr/bin/env python3 
import sys

fileName = sys.argv[1]
vmFile = open(fileName)
lines = vmFile.readlines()
vmFile.close()

##	GLOBAL Variables
spValue = 256		#points to one space after end of stack
staticValue = 16
comparisonLabelIndex = 0

binaryCommands = {"add":"+", "sub":"-", "and":"&", "or":"|"}
unaryCommands = {"neg":"-", "not":"!"}
comparisonCommands = {"eq":"JEQ", "gt":"JGT", "lt":"JLT"}

pointedSegments = {"this":"THIS", "that":"THAT", "local":"LCL", "argument":"ARG"}

staticVars = {}

#Argument is absolute memory location (string), returns asm code
def push(loc, ifConstant):
	global spValue
	if ifConstant:
		code = "@" + loc + "\nD=A\n@" + str(spValue) + "\nM=D\n"
	else:
		code = "@" + loc + "\nD=M\n@" + str(spValue) + "\nM=D\n"
	spValue = spValue + 1
	return code
	
def pop(loc):
	global spValue
	code = "@" + str(spValue - 1) + "\nD=M\n@" + loc + "\nM=D\n"
	spValue = spValue - 1
	return code

#Push and pop functions with pointed memory locations
def pointedPush(arg1, arg2):
	global spValue
	code = "@" + arg2 + "\nD=A\n@" + pointedSegments[arg1] + "\nA=D+M\nD=M\n@" + str(spValue) + "\nM=D\n"
	spValue = spValue + 1
	return code
def pointedPop(arg1, arg2):
	global spValue
	#I have a feeling that this can be improved
	code = "@" + arg2 + "\nD=A\n@" + pointedSegments[arg1] + "\nD=D+M\n@" + str(spValue) + "\nM=D\n@" + str(spValue - 1) + "\nD=M\n@" + str(spValue) + "\nA=M\nM=D\n"
	spValue = spValue - 1
	return code
	
#Argument takes in command(string) and does it on stack
def binaryStackCommand(command):
	global spValue
	code = "@" + str(spValue - 1) +  "\nD=M\n@" + str(spValue - 2) + "\nD=M" + binaryCommands[command] + "D\n@" + str(spValue - 2) + "\nM=D\n"
	spValue = spValue - 1
	return code
	
def unaryStackCommand(command):
	code = "@" + str(spValue - 1) + "\nM=" + unaryCommands[command] + "M\n"
	return code
	
def comparisonStackCommand(command):
	global spValue
	global comparisonLabelIndex
	compLabel = "COMPARE.LABEL."+str(comparisonLabelIndex)
	code = "@" + str(spValue - 2) + "\nD=M\nM=-1\n@" + str(spValue - 1) + "\nD=D-M\n@" + compLabel + "\nD;" + comparisonCommands[command] + "\n@" + str(spValue - 2) + "\nM=!M\n(" + compLabel + ")\n"
	comparisonLabelIndex = comparisonLabelIndex + 1
	spValue = spValue - 1
	return code

#Returns static RAM address in string format
def assignStaticRAM(arg1,arg2):
	global staticValue
	if arg1 == "static":
		if arg2 not in staticVars:
			staticVars[arg2] = staticValue
			staticValue = staticValue + 1
		return str(staticVars[arg2])
	elif arg1 == "pointer":
		return str(3 + int(arg2))
	elif arg1 == "temp":
		return str(5 + int(arg2))


#Parsing code to translate VM code into a list of lists
#For each line: [<command>,<arg1>,<arg2>] 
# arg1 and arg2 are optional, whether they exists depends on command

parsedLines = []

for line in lines:
	lineBuffer = []
	wordBuffer = ""
	wordNumber = 0
	inWord = False
	for l in range(len(line)):
		if (line[l] == " ") or (line[l] == "\t") or (line[l] == "\n") or (line[l] == "/"):
			if inWord:
				lineBuffer.append(wordBuffer)
				wordBuffer = ""
				wordNumber = wordNumber + 1
				inWord = False
			pass
			if (line[l] == "/") and (line[l+1] == "/"): break
		else:
			if wordNumber == 3: break
			inWord = True
			wordBuffer = wordBuffer + line[l]
	if len(lineBuffer) > 0:
		parsedLines.append(lineBuffer)
		lineBuffer = []

asm = ""

for line in parsedLines:
	if line[0] == "push":
		if line[1] == "constant":
			asmLine = push(line[2],True)
		elif line[1] in pointedSegments:
			asmLine = pointedPush(line[1], line[2])
		else:
			asmLine = push(assignStaticRAM(line[1], line[2]),False)
	elif line[0] == "pop":
		if line[1] in pointedSegments:
			asmLine = pointedPop(line[1], line[2])
		else:
			asmLine = pop(assignStaticRAM(line[1], line[2]))
	elif line[0] in binaryCommands:
		asmLine = binaryStackCommand(line[0])
	elif line[0] in unaryCommands:
		asmLine = unaryStackCommand(line[0])		
	elif line[0] in comparisonCommands:
		asmLine = comparisonStackCommand(line[0])
	asm = asm + asmLine
	

#End loop
asm = asm + "(END)\n@END\n0;JMP\n"

#Write to <filename>.asm file
writeFileName = ""
for l in range(len(fileName)):
	if fileName[l] == ".":
		break
	writeFileName = writeFileName + fileName[l]
	
writeFileName = writeFileName + ".asm"

writeFile = open(writeFileName, 'w')
writeFile.write(asm)
writeFile.close()