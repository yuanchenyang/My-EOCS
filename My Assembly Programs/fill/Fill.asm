(RESET)
	@16384
	D=A
	@i
	M=D
(LOOP)
	@24576
	D=A
	@i
	D=M-D
	@RESET
	D;JGE
	@24576
	D=M
	@FILL
	D;JNE
// No Fill
	@i
	A=M
	M=0
	@i
	M=M+1
	@LOOP
	0;JMP
(FILL)
	@i
	A=M
	M=-1
	@i
	M=M+1
	@LOOP
	0;JMP