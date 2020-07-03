def fixed_to_float(bin_num, mantissa_bit_amount=10, exponent_bit_amount=6):
    assert bin_num.find("1") != -1, "No 1's"
    assert len(bin_num[bin_num.find("1"):bin_num.rfind("1")]) < mantissa_bit_amount, f"mantissa would be larger than {mantissa_bit_amount} bits"
    # Save original to compare later
    original = bin_num

    # Determine numbers to pad with and left most 1
    ex_negative = False

    # Remove old decimal point
    bin_num = list(bin_num)
    bin_num.remove(".")

    # Find left most 1 to find new decimal point position
    dec_point = "".join(bin_num).find("1")
    if dec_point == 0:
        dec_point += 1
    bin_num.insert(dec_point, ".")

    # Cast list back to str
    bin_num = "".join(bin_num)

    # Find exponent by getting difference between the original decimal position and the new one
    exponent = format((original.find(".") if original.find(".") > -1 else len(original)) - bin_num.find("."), f"0{exponent_bit_amount}b")
    if int(exponent, 2) < 0:
        num = int(exponent, 2)
        exponent = str(bin(num & (2**(int(num).bit_length() + 1)) - 1))[2:]
        ex_negative = True

    # Slice str to make the binary start with 0.1
    bin_num = bin_num[dec_point - 1:]

    # Pad mantissa with 0
    bin_num = bin_num + ("0" * (mantissa_bit_amount - (len(bin_num) - 1)))

    # Pad exponent with 0 if positive and 1 if negative
    exponent = (("0" if not ex_negative else "1") * (exponent_bit_amount - len(exponent))) + exponent
    return bin_num, exponent


print(fixed_to_float("010101010.1"))
