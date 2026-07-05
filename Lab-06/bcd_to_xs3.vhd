library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity BCD_TO_XS3 is
    port (
        BCD : in  STD_LOGIC_VECTOR(3 downto 0);
        XS3 : out STD_LOGIC_VECTOR(3 downto 0)
    );
end entity BCD_TO_XS3;

architecture Behavioral of BCD_TO_XS3 is
begin
    process(BCD)
    begin
        XS3 <= STD_LOGIC_VECTOR(unsigned(BCD) + 3);
    end process;
end architecture Behavioral;