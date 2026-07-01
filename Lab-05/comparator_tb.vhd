library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity COMPARATOR_TB is
end entity COMPARATOR_TB;

architecture Simulation of COMPARATOR_TB is

    signal A  : STD_LOGIC_VECTOR(1 downto 0) := "00";
    signal B  : STD_LOGIC_VECTOR(1 downto 0) := "00";
    signal EQ : STD_LOGIC;
    signal GT : STD_LOGIC;
    signal LT : STD_LOGIC;

begin

    -- Device Under Test (DUT)
    DUT : entity work.COMPARATOR_2BIT
        port map (
            A  => A,
            B  => B,
            EQ => EQ,
            GT => GT,
            LT => LT
        );

    -- Stimulus Process
    STIMULUS : process
    begin
        -- Test Case 1: A = B
        A <= "00";
        B <= "00";
        wait for 10 ns;

        -- Test Case 2: A > B
        A <= "01";
        B <= "00";
        wait for 10 ns;

        -- Test Case 3: A < B
        A <= "00";
        B <= "01";
        wait for 10 ns;

        -- Test Case 4: A < B
        A <= "10";
        B <= "11";
        wait for 10 ns;

        -- Test Case 5: A > B
        A <= "11";
        B <= "10";
        wait for 10 ns;

        -- Test Case 6: A = B
        A <= "11";
        B <= "11";
        wait for 10 ns;

        wait;
    end process;

end architecture Simulation;