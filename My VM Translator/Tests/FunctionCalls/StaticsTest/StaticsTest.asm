@255
D=A
@SP
M=D
@Sys.init
0;JMP
(Class1.set)
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
@SP
A=M
D=M
@Class1.0
M=D
@SP
M=M-1
@1
D=A
@ARG
A=D+M
D=M
@SP
AM=M+1
M=D
@SP
A=M
D=M
@Class1.1
M=D
@SP
M=M-1
@0
D=A
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
(Class1.get)
@0
D=A
@SP
M=D+M
@Class1.0
D=M
@SP
AM=M+1
M=D
@Class1.1
D=M
@SP
AM=M+1
M=D
@SP
A=M
D=M
@SP
AM=M-1
M=M-D
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
(Class2.set)
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
@SP
A=M
D=M
@Class2.0
M=D
@SP
M=M-1
@1
D=A
@ARG
A=D+M
D=M
@SP
AM=M+1
M=D
@SP
A=M
D=M
@Class2.1
M=D
@SP
M=M-1
@0
D=A
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
(Class2.get)
@0
D=A
@SP
M=D+M
@Class2.0
D=M
@SP
AM=M+1
M=D
@Class2.1
D=M
@SP
AM=M+1
M=D
@SP
A=M
D=M
@SP
AM=M-1
M=M-D
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
@6
D=A
@SP
AM=M+1
M=D
@8
D=A
@SP
AM=M+1
M=D
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
@6
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M+1
@LCL
M=D
@Class1.set
0;JMP
($RETURN.ADDRESS.1)
@SP
A=M
D=M
@5
M=D
@SP
M=M-1
@23
D=A
@SP
AM=M+1
M=D
@15
D=A
@SP
AM=M+1
M=D
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
@6
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M+1
@LCL
M=D
@Class2.set
0;JMP
($RETURN.ADDRESS.2)
@SP
A=M
D=M
@5
M=D
@SP
M=M-1
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
@4
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M+1
@LCL
M=D
@Class1.get
0;JMP
($RETURN.ADDRESS.3)
@$RETURN.ADDRESS.4
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
@4
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M+1
@LCL
M=D
@Class2.get
0;JMP
($RETURN.ADDRESS.4)
(Sys.init$WHILE)
@Sys.init$WHILE
0;JMP
