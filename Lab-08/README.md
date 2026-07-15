## Objective

- To design and simulate a 4-bit synchronous up counter in VHDL.
- To design and simulate a 4-bit synchronous up/down counter in VHDL.

## Theory

A counter is a sequential circuit that cycles through a predefined sequence of states on each clock edge. Counters are built using flip-flops and are fundamental to timing, sequencing, and frequency division.

- **Synchronous Counter:** All flip-flops are triggered by the same clock signal, making it faster and more reliable than an asynchronous (ripple) counter.
- **Up Counter:** Increments the count by 1 on each rising edge of the clock.
- **Up/Down Counter:** Increments or decrements the count depending on the direction control signal.
- **Reset:** An active-high reset initializes the counter to `0000`.

## Output
![alt text](<Screenshot (51).png>)

## Discussion and conclusion
In this laboratory exercise, 4-bit synchronous up and up/down counters were successfully designed, modeled, and analyzed using VHDL behavioral 
descriptions. Additionally, the lab successfully contrasted asynchronous and synchronous reset patterns, highlighting their distinct impacts on 
circuit behavior and synchronization.
