@i
M=0
@prod
M=0
(LOOP)
@i
D=M
@R0
D=D-M
@END
D;JGE
@R1
D=M
@prod
M=M+D
@i
M=M+1
@LOOP
0;JMP
(END)
@END
0;JMP