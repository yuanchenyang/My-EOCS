#!/usr/bin/env python3 
import sys

#Get number into 16 digit binary string
def toBin(n):
	s = bin(n)[2:]
	for j in range(16-len(s)):
		s = "0"+s
	return s

#Numbers
numbers = ["0","1","2","3","4","5","6","7","8","9"]

#Binary code dictionaries

comp = {"0":"0101010", "1":"0111111", "-1":"0111010", "D":"0001100", "A":"0110000", "!D":"0001101", "!A":"0110001", "-D":"0001111", "-A":"0110011", "D+1":"0011111", "1+D":"0011111", "A+1":"0110111", "1+A":"0110111", "D-1":"0001110", "A-1":"0110010", "D+A":"0000010", "A+D":"0000010", "D-A":"0010011", "A-D":"0000111", "D&A":"0000000", "A&D":"0000000", "D|A":"0010101", "A|D":"0010101", "M":"1110000", "!M":"1110001", "-M":"1110011", "M+1":"1110111", "1+M":"1110111", "M-1":"1110010", "D+M":"1000010", "M+D":"1000010", "D-M":"1010011", "M-D":"1000111", "D&M":"1000000", "M&D":"1000000", "D|M":"1010101", "M|D":"1010101"}

dest = {"":"000", "null":"000", "M":"001", "D":"010", "MD":"011", "A":"100", "AM":"101", "AD":"110", "AMD":"111"}

jump = {"":"000", "null":"000", "JGT":"001", "JEQ":"010", "JGE":"011", "JLT":"100", "JNE":"101", "JLE":"110", "JMP":"111"}

symbols = {"SP":"0000000000000000", "LCL":"0000000000000001", "ARG":"0000000000000010", "THIS":"0000000000000011", "THAT":"0000000000000100", "SCREEN":"0100000000000000", "KBD":"0110000000000000"}

#add R0-R15 to symbols
for i in range(16):
	s = toBin(i)
	symbols["R"+str(i)] = s

binary = ""

fileName = sys.argv[1]
asmFile = open(fileName)
lines = asmFile.readlines()
asmFile.close()

# First pass
# Ignores for tabs and spaces before and after commands, blank lines, everything after "//"
lineCount = 0
symbolCount = 16
codeLines = []
variables = []
labels = {}
for line in lines:
	lineBuffer = ""
	started = False
	if (";" in line) or ("=" in line) or ("@" in line):
		for l in range(0, len(line)):
			if line[l] == "\n":
				break
			elif line[l] == "/":
				if line[l+1] == "/":
					break
			elif (line[l] == " ") or (line[l] == "\t"):
				if started:
					break
			else:
				started = True
				lineBuffer = lineBuffer + line[l]
		if started:
			lineCount = lineCount + 1
			codeLines.append(lineBuffer)
			if ("@" in lineBuffer) and (lineBuffer[1] not in numbers) and (lineBuffer[1:] not in symbols) and (lineBuffer[1:] not in variables):
				variables.append(lineBuffer[1:])			
	elif (line[0] == "(") and (")" in line):
		for l in range(1,len(line)):
			if (line[l] == ")"):
				break
			else:
				lineBuffer = lineBuffer + line[l]
		labels[lineBuffer] = toBin(lineCount)

for v in variables:
	if v not in labels:
		symbols[v] = toBin(symbolCount)
		symbolCount = symbolCount + 1

for l in labels:
	symbols[l] = labels[l]

# Second pass
for line in codeLines:
	compBuffer = ""
	destBuffer = ""
	jumpBuffer = ""
	j = False
	if line[0] == "@":
		if line[1] in numbers:
			s = toBin(int(line[1:]))
		else:
			s = symbols[line[1:]]
		binary = binary + s + "\n"
	else:
		for l in range(len(line)):
			if line[l] == "=":
				destBuffer = compBuffer
				compBuffer = ""
			elif line[l] == ";":
				j = True
			else:
				if j:
					jumpBuffer = jumpBuffer + line[l]
				else:
					compBuffer = compBuffer + line[l]

		binary = binary + "111" + comp[compBuffer] + dest[destBuffer] + jump[jumpBuffer] + "\n"


#Write to <filename>.hack file
writeFileName = ""
for l in range(len(fileName)):
	if fileName[l] == ".":
		break
	writeFileName = writeFileName + fileName[l]
	
writeFileName = writeFileName + ".hack"

writeFile = open(writeFileName, 'w')
writeFile.write(binary)
writeFile.close()
			
		
		