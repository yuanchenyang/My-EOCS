// This file is part of the materials accompanying the book 
// "The Elements of Computing Systems" by Nisan and Schocken, 
// MIT Press. Book site: www.idc.ac.il/tecs
// File name: projects/06/max/Max.asm

// Computes M[2] = max(M[0], M[1])  where M stands for RAM
   @i
   D=M              // D=first number
   @j
   D=D-M            // D=first number - second number
   @OUTPUT_FIRST
   D;JGT            // if D>0 (first is greater) goto output_first
   @j
   D=M              // D=second number
   @OUTPUT_D
   0;JMP            // goto output_d
(OUTPUT_FIRST)
   @i             
   D=M              // D=first number
(OUTPUT_D)
   @k
   M=D              // M[2]=D (greatest number)
(INFINITE_LOOP)
   @INFINITE_LOOP
   0;JMP            // infinite loop
