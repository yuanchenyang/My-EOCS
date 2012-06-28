//Sorts entries in ascending order from memory address 101 onwards (inclusive), size of data set specified by R0
// R1 and R2 used for temp storage

@1
D=A
@count //Counts number of times a switch has been made each run,
M=D    //starts at 1 first
(RESET)
	@count
	D=M
	@END
	D;JEQ //Ends if no swaps have been made in a full run
	@100
	D=A
	@i //counter i=100
	M=D
	@101
	D=A
	@j //counter j=101
	M=D
	@0
	D=A
	@count //Reset count
	M=D
(LOOP)
	@i
	M=M+1 //i++
	@j
	M=M+1 //j++
	D=M 
	@100
	D=D-A
	@R0
	D=D-M //Computes j-100-R0
	@RESET
	D;JGT //Reset if j-100-R0>0
	@i
	A=M
	D=M
	@R1
	M=D //Load register specified by i’s value into R1
	@j
	A=M
	D=M
	@R2 //Load register specified by j’s value into R2
	M=D
	@R1
	D=M
	@R2
	D=D-M
	@SWITCH //if R1-R2>0 then switch their positions
	D;JGT
	@LOOP
	0;JMP
(SWITCH)
	@R1
	D=M
	@j
	A=M
	M=D //Move value of R1 into register specified by j’s value
	@R2
	D=M
	@i
	A=M
	M=D //Move value of R2 into register specified by i’s value
	@count
	M=M+1 //count++
	@LOOP
	0;JMP
(END)
	@END
	0;JMP