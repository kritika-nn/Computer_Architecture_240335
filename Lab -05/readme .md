#### Lab Report: 2-bit Magnitude Comparator

 ### Objective

  To design and simulate a 2-bit magnitude comparator in VHDL.
  To understand how comparison operations are implemented in hardware.
## Theory
    A magnitude comparator compares two binary numbers and produces three output signals:

    EQ (Equal): HIGH when A=B
    GT (Greater Than): HIGH when A>B
    LT (Less Than): HIGH when  A<B

    For a 2-bit comparator with inputs A=A1A0 and B=B1B0: 

     EQ = A1⊕'B1⋅A0⊕'B0
    GT = A1B1'+A1⊕'B1⋅A0B0'
    LT= A1'B1 + A1⊕'B1⋅A0'B0

    ## Output 
    ![alt text](<Screenshot (46).png>)
    

    ## Discussion and conclusion

     # Here, by the waveform we verify that a 
    comparator has place for 2 input and 3 output 
    lines, the comparator is a device that compares 
    the two inputs and gives an output as high in 
    one of the 3 output lines. The two inputs A and 
    B determine the output eq, lt and gt, eq = 1 
    when A=B, gt = 1 when A > B and lt = 1 when A < 
    B.
    