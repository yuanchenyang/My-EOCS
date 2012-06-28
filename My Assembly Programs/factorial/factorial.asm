@j			// Input R0
M=0			// Output R1
@R1			// Factorial of input
M=1
(LOOPF)
	@j
	D=M
	@R0
	D=D-M
	@END
	D;JGE
	@j
	M=M+1
	D=M
	@R11
	M=D
	@R1
	D=M
	@R10
	M=D
//Multiply function Starts
	@i
	M=0
	@prod
	M=0
	(LOOPM)
		@i
		D=M
		@R10
		D=D-M
		@LOOPADD
		D;JGE
		@R11
		D=M
		@prod
		M=M+D
		@i
		M=M+1
		@LOOPM
		0;JMP
//Multiply function Ends
(LOOPADD)
	@prod
	D=M
	@R1
	M=D
	@LOOPF
	0;JMP
(END)
	@END
	0;JMP