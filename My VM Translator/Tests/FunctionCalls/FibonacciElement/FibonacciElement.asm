@255
D=A
@SP
M=D
@Sys.init
0;JMP
(Main.fibonacci)
@0
D=A
@SP
M=D+M
@0
D=A
@ARG
A=D+M
D=M
@SP
AM=M+1
M=D
@2
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
@$COMPARE.LABEL.1
D;JLT
@SP
A=M
M=!M
($COMPARE.LABEL.1)
@SP
D=M
M=M-1
A=D
D=M
@Main.fibonacci$IF_TRUE
D;JNE
@Main.fibonacci$IF_FALSE
0;JMP
(Main.fibonacci$IF_TRUE)
@0
D=A
@ARG
A=D+M
D=M
@SP
AM=M+1
M=D
@LCL
D=M
@13
M=D
@5
A=D-A
D=M
@14
M=D
@SP
A=M
D=M
@ARG
A=M
M=D
@ARG
D=M
@SP
M=D
@4
D=A
@13
A=M-D
D=M
@LCL
M=D
@3
D=A
@13
A=M-D
D=M
@ARG
M=D
@2
D=A
@13
A=M-D
D=M
@THIS
M=D
@1
D=A
@13
A=M-D
D=M
@THAT
M=D
@14
A=M
0;JMP
(Main.fibonacci$IF_FALSE)
@0
D=A
@ARG
A=D+M
D=M
@SP
AM=M+1
M=D
@2
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
@$RETURN.ADDRESS.1
D=A
@SP
AM=M+1
M=D
@LCL
D=M
@SP
AM=M+1
M=D
@ARG
D=M
@SP
AM=M+1
M=D
@THIS
D=M
@SP
AM=M+1
M=D
@THAT
D=M
@SP
AM=M+1
M=D
@5
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M+1
@LCL
M=D
@Main.fibonacci
0;JMP
($RETURN.ADDRESS.1)
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
@$RETURN.ADDRESS.2
D=A
@SP
AM=M+1
M=D
@LCL
D=M
@SP
AM=M+1
M=D
@ARG
D=M
@SP
AM=M+1
M=D
@THIS
D=M
@SP
AM=M+1
M=D
@THAT
D=M
@SP
AM=M+1
M=D
@5
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M+1
@LCL
M=D
@Main.fibonacci
0;JMP
($RETURN.ADDRESS.2)
@SP
A=M
D=M
@SP
AM=M-1
M=M+D
@LCL
D=M
@13
M=D
@5
A=D-A
D=M
@14
M=D
@SP
A=M
D=M
@ARG
A=M
M=D
@ARG
D=M
@SP
M=D
@4
D=A
@13
A=M-D
D=M
@LCL
M=D
@3
D=A
@13
A=M-D
D=M
@ARG
M=D
@2
D=A
@13
A=M-D
D=M
@THIS
M=D
@1
D=A
@13
A=M-D
D=M
@THAT
M=D
@14
A=M
0;JMP
(Sys.init)
@0
D=A
@SP
M=D+M
@23
D=A
@SP
AM=M+1
M=D
@$RETURN.ADDRESS.3
D=A
@SP
AM=M+1
M=D
@LCL
D=M
@SP
AM=M+1
M=D
@ARG
D=M
@SP
AM=M+1
M=D
@THIS
D=M
@SP
AM=M+1
M=D
@THAT
D=M
@SP
AM=M+1
M=D
@5
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M+1
@LCL
M=D
@Main.fibonacci
0;JMP
($RETURN.ADDRESS.3)
(Sys.init$WHILE)
@Sys.init$WHILE
0;JMP
