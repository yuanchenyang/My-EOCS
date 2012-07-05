#!/usr/bin/env python3 
import sys
import os
import glob

#Example input:
#python3 VM.py3 <filename>.vm
#OR
#python3 VM.py3 <foldername>
#
#<foldername> must be a folder containing at least 1 .vm file


##	GLOBAL Variables
comparisonLabelIndex = 0
returnAddress = 0
funcName = ""

binaryCommands = {"add":"+", "sub":"-", "and":"&", "or":"|"}
unaryCommands = {"neg":"-", "not":"!"}
comparisonCommands = {"eq":"JEQ", "gt":"JGT", "lt":"JLT"}
flowCommands = ["label", "goto", "if-goto"]

pointedSegments = {"this":"THIS", "that":"THAT", "local":"LCL", "argument":"ARG"}

#Static push and pop
def staticPush(value,constant):
	if constant:
		return "@" + value + "\nD=A\n@SP\nAM=M+1\nM=D\n"
	else:
		return "@" + value + "\nD=M\n@SP\nAM=M+1\nM=D\n"
def staticPop(value):
	return "@SP\nA=M\nD=M\n@" + value + "\nM=D\n@SP\nM=M-1\n"

#Push and pop functions with pointed memory locations
def pointedPush(arg1, arg2):
	return "@" + arg2 + "\nD=A\n@" + pointedSegments[arg1] + "\nA=D+M\nD=M\n@SP\nAM=M+1\nM=D\n"
def pointedPop(arg1, arg2):
	#Uses register 13 as temp storage
	return "@" + arg2 + "\nD=A\n@" + pointedSegments[arg1] + "\nD=D+M\n@13\nM=D\n@SP\nA=M\nD=M\n@13\nA=M\nM=D\n@SP\nM=M-1\n"
	
#Argument takes in command(string) and does it on stack
def binaryStackCommand(command):
	return "@SP\nA=M\nD=M\n@SP\nAM=M-1\nM=M" + binaryCommands[command] + "D\n"
def unaryStackCommand(command):
	return "@SP\nA=M\nM=" + unaryCommands[command] + "M\n"
def comparisonStackCommand(command):
	global comparisonLabelIndex
	comparisonLabelIndex += 1
	compLabel = "$COMPARE.LABEL."+str(comparisonLabelIndex)
	return "@SP\nA=M\nD=M\n@SP\nAM=M-1\nD=M-D\nM=-1\n@" + compLabel + "\nD;" + comparisonCommands[command] +"\n@SP\nA=M\nM=!M\n(" + compLabel + ")\n"

#Controls flow
def controlFlowCommand(command, label):
	global funcName
	if command == "label":
		return "(" + funcName + "$" + label + ")\n"
	elif command == "goto":
		return "@" + funcName + "$" + label + "\n0;JMP\n"
	elif command == "if-goto":
		return "@SP\nD=M\nM=M-1\nA=D\nD=M\n@" + funcName + "$"+ label + "\nD;JNE\n"

#Returns static RAM address in string format
def assignStaticRAM(arg1,arg2,name):
	if arg1 == "static":
		return name + "." + str(arg2)
	elif arg1 == "pointer":
		return str(3 + int(arg2))
	elif arg1 == "temp":
		return str(5 + int(arg2))

#Translates code and assigns static variable names based on fileName
def translate(fileName,code):
	global funcName, returnAddress
	asm = ""
	for line in code:
		if line[0] == "push":
			if line[1] == "constant":
				asmLine = staticPush(line[2],True)
			elif line[1] in pointedSegments:
				asmLine = pointedPush(line[1], line[2])
			else:
				asmLine = staticPush(assignStaticRAM(line[1], line[2], fileName),False)
		elif line[0] == "pop":
			if line[1] in pointedSegments:
				asmLine = pointedPop(line[1], line[2])
			else:
				asmLine = staticPop(assignStaticRAM(line[1], line[2], fileName))
		elif line[0] in binaryCommands:
			asmLine = binaryStackCommand(line[0])
		elif line[0] in unaryCommands:
			asmLine = unaryStackCommand(line[0])		
		elif line[0] in comparisonCommands:
			asmLine = comparisonStackCommand(line[0])
		elif line[0] in flowCommands:
			asmLine = controlFlowCommand(line[0], line[1])
		elif line[0] == "function":
			#NOTE: in this implementation, local variables are not init-ed to 0
			funcName = line[1]
			asmLine = "(" + line[1] + ")\n@" + line[2] + "\nD=A\n@SP\nM=D+M\n"
		elif line[0] == "call":
			#Sets and stores return address
			returnAddress += 1
			asmLine = staticPush("$RETURN.ADDRESS." + str(returnAddress),True)
			#Stores LCL, ARG, THIS and THAT
			for i in ["LCL","ARG","THIS","THAT"]:
				asmLine += staticPush(i,False)
			#Assigns ARG
			asmLine += "@" + str(int(line[2]) + 4) + "\nD=A\n@SP\nD=M-D\n@ARG\nM=D\n"
			#Assigns LCL
			asmLine += "@SP\nD=M+1\n@LCL\nM=D\n"
			#Runs Function
			asmLine += "@" + line[1] + "\n0;JMP\n"
			#Add label
			asmLine += "($RETURN.ADDRESS." + str(returnAddress) + ")\n"
		elif line[0] == "return":
			#Sets register 13 to LCL value
			asmLine = "@LCL\nD=M\n@13\nM=D\n"
			#Sets register 14 to return address
			asmLine += "@5\nA=D-A\nD=M\n@14\nM=D\n"
			#Put return value to ARG's pointed address
			asmLine += "@SP\nA=M\nD=M\n@ARG\nA=M\nM=D\n"
			#Restores SP
			asmLine += "@ARG\nD=M\n@SP\nM=D\n"
			#Restores LCL, ARG, THIS, THAT
			j = 4
			for i in ["LCL","ARG","THIS","THAT"]:
				asmLine += "@" + str(j) + "\nD=A\n@13\nA=M-D\nD=M\n@" + i + "\nM=D\n"
				j -= 1
			#Goto return address
			asmLine += "@14\nA=M\n0;JMP\n"
		asm += asmLine
	return asm

#Parsing code to translate VM code into a list of lists
#For each line: [command,(arg1,arg2)] (command, arg1, arg2 are strings)
def readFile(fileName):
	vmFile = open(fileName + ".vm")
	lines = vmFile.readlines()
	vmFile.close()
	#Remove comments and splits each line
	lines=[s.partition("//")[0].split() for s in lines]
	#Remove blank lines
	lines=[s for s in lines if s!=[]]
	return lines 

#Opening and reading file(s)
name = sys.argv[1]
asm = ""

if name[-3:] == ".vm":
	#Single File
	name = name[:-3]
	#NOTE: SP in this implementation points to the topmost element on the stack,
	#      thus the following code involving SP is added to correct this for testing
	asm += "@SP\nM=M-1\n"
	asm += translate(name, readFile(name))
	asm += "@SP\nM=M+1\n"
	#End loop
	asm += "(END)\n@END\n0;JMP\n"
	name = name.rsplit(".vm",1)[0]
else:
	#Bootstrap code
	asm += "@255\nD=A\n@SP\nM=D\n@Sys.init\n0;JMP\n"
	#Code for all the .vm files
	for n in glob.glob(os.path.join(name,'*.vm')):
		n = n[:-3]
		asm += translate(n.split(name+'/',1)[-1], readFile(n))	

#Write to <filename>.asm file
writeFileName = name + ".asm"
writeFile = open(writeFileName, 'w')
writeFile.write(asm)
writeFile.close()