## MAIN
def booths_algorithm():
    # Gets Multiplicand
    multiplicand_dec = getInput("Multiplicand")

    # Gets Multiplier
    multiplier_dec = getInput("Multiplier")

    # Converts Multiplicand
    multiplicand_bin = convertDec(multiplicand_dec)

    # Converts Multiplier
    multiplier_bin = convertDec(multiplier_dec)

    # Perform Booth's algorithm
    boothsTriumph(multiplicand_bin, multiplier_bin)

    print("Decimal Result:", int(multiplier_dec) * int(multiplicand_dec))


## Parent function for logical process
def boothsTriumph(mcand, plier):
    print("Multiplicand:", mcand, "Multiplier:", plier)

    product = "00000000" + plier + "0"
    print("Product:", product)

    print(buildLine(0, mcand, product))

    for i in range(1, 9):
        operation = product[-2:]
        product = perform_operation(product, mcand, operation)
        print(buildLine(i, mcand, product))

    product = shift(product)
    product = product[9:17]

    print("Product:", product)


## Perform the necessary algorithmic operation
def perform_operation(product, mcand, operation):
    if operation == "00":
        product = shift(product)
        print("No Op")
        return product

    elif operation == "01":
        temp = binAdd(product[0:8], mcand)
        product = temp + product[8:]
        product = shift(product)
        print("Add")
        return product

    elif operation == "10":
        product = subtraction(product, mcand)
        product = shift(product)
        print("Sub")
        return product

    elif operation == "11":
        product = shift(product)
        print("No Op")
        return product


## Performs Subtraction operation
def subtraction(product, mcand):
    carry = 0
    prime_product = product[:8]
    final_product = ""

    for i in range(len(prime_product) - 1, -1, -1):

        if mcand[i] == "0" and prime_product[i] == "0":
            if carry == 1:
                final_product = "1" + final_product
            else:
                final_product = "0" + final_product

        elif mcand[i] == "1" and prime_product[i] == "0":
            if carry == 1:
                final_product = "0" + final_product
            else:
                final_product = "1" + final_product
            carry = 1

        elif mcand[i] == "0" and prime_product[i] == "1":
            if carry == 1:
                final_product = "0" + final_product
                carry = 0
            else:
                final_product = "1" + final_product

        elif mcand[i] == "1" and prime_product[i] == "1":
            if carry == 1:
                final_product = "1" + final_product
            else:
                final_product = "0" + final_product

    return final_product + product[8:]


## Shifts right
def shift(product):
    return "0" + product[:-1]


## Adds the two binary strings
def binAdd(num, num2):
    product = ""
    carry = "0"

    for i in range(len(num) - 1, -1, -1):

        if carry == "0":
            if num[i] == "0" and num2[i] == "0":
                product = "0" + product

            elif num[i] == "1" and num2[i] == "1":
                product = "0" + product
                carry = "1"

            else:
                product = "1" + product

        else:
            if num[i] == "0" and num2[i] == "0":
                product = "1" + product
                carry = "0"

            elif num[i] == "1" and num2[i] == "1":
                product = "1" + product
                carry = "1"

            else:
                product = "0" + product
                carry = "1"

    return product


## Shows step-by-step process
def buildLine(iteration, mcand, product):
    return (
        "Step: "
        + str(iteration)
        + " | Multiplicand: "
        + mcand
        + " | Product: "
        + product[0:8]
        + " | "
        + product[8:16]
        + " | "
        + product[16]
    )


## Formats numbers from decimal to binary
def convertDec(dec):

    if int(dec) < 0:
        binary = twos_complement(int(dec))
    else:
        binary = format(int(dec), "b")

    binary = binary.zfill(8)

    return binary


## Gets input for algorithm
def getInput(varName):
    boothIn = input("Please enter your " + varName + ": ")

    while int(boothIn) > 127 or int(boothIn) < -128:
        print("Absolute value too big, please try again.")
        boothIn = input("Please enter your " + varName + ": ")

    return boothIn


## Converts negative numbers
def twos_complement(dec):
    adjusted = abs(int(dec) + 1)
    binint = format(adjusted, "b")
    flipped = flip(binint)
    flipped = flipped.rjust(8, "1")
    return flipped


## Flips the bits
def flip(string):
    flipped_string = ""

    for bit in string:
        if bit == "1":
            flipped_string += "0"
        else:
            flipped_string += "1"

    return flipped_string


## CALL MAIN
if __name__ == "__main__":
    booths_algorithm()