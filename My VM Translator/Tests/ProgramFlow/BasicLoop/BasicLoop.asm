@SP
M=M-1
@0
D=A
@SP
AM=M+1
M=D
@0
D=A
@LCL
D=D+M
@13
M=D
@SP
A=M
D=M
@13
A=M
M=D
@SP
M=M-1
(LOOP_START)
@0
D=A
@ARG
A=D+M
D=M
@SP
AM=M+1
M=D
@0
D=A
@LCL
A=D+M
D=M
@SP
AM=M+1
M=D
@SP
A=M
D=M
@SP
AM=M-1
M=M+D
@0
D=A
@LCL
D=D+M
@13
M=D
@SP
A=M
D=M
@13
A=M
M=D
@SP
M=M-1
@0
D=A
@ARG
A=D+M
D=M
@SP
AM=M+1
M=D
@1
D=A
@SP
AM=M+1
M=D
@SP
A=M
D=M
@SP
AM=M-1
M=M-D
@0
D=A
@ARG
D=D+M
@13
M=D
@SP
A=M
D=M
@13
A=M
M=D
@SP
M=M-1
@0
D=A
@ARG
A=D+M
D=M
@SP
AM=M+1
M=D
@SP
D=M
M=M-1
A=D
D=M
@LOOP_START
D;JNE
@0
D=A
@LCL
A=D+M
D=M
@SP
AM=M+1
M=D
@SP
M=M+1
(END)
@END
0;JMP