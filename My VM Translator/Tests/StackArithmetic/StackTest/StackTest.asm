@SP
M=M-1
@17
D=A
@SP
AM=M+1
M=D
@17
D=A
@SP
AM=M+1
M=D
@SP
A=M
D=M
@SP
AM=M-1
D=M-D
M=-1
@COMPARE.LABEL.1
D;JEQ
@SP
A=M
M=!M
(COMPARE.LABEL.1)
@892
D=A
@SP
AM=M+1
M=D
@891
D=A
@SP
AM=M+1
M=D
@SP
A=M
D=M
@SP
AM=M-1
D=M-D
M=-1
@COMPARE.LABEL.2
D;JLT
@SP
A=M
M=!M
(COMPARE.LABEL.2)
@32767
D=A
@SP
AM=M+1
M=D
@32766
D=A
@SP
AM=M+1
M=D
@SP
A=M
D=M
@SP
AM=M-1
D=M-D
M=-1
@COMPARE.LABEL.3
D;JGT
@SP
A=M
M=!M
(COMPARE.LABEL.3)
@56
D=A
@SP
AM=M+1
M=D
@31
D=A
@SP
AM=M+1
M=D
@53
D=A
@SP
AM=M+1
M=D
@SP
A=M
D=M
@SP
AM=M-1
M=M+D
@112
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
@SP
A=M
M=-M
@SP
A=M
D=M
@SP
AM=M-1
M=M&D
@82
D=A
@SP
AM=M+1
M=D
@SP
A=M
D=M
@SP
AM=M-1
M=M|D
(END)
@END
0;JMP
