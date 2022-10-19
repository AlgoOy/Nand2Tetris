def init_syntax():
    """
    this function will init the C_instruction syntax.
    :return: comp_syntax, dest_syntax, jump_syntax
    """
    dest_syntax = {
        "null": "000",
        "M": "001",
        "D": "010",
        "MD": "011",
        "A": "100",
        "AM": "101",
        "AD": "110",
        "AMD": "111",
    }
    comp_syntax = {
        "0": "0101010",
        "1": "0111111",
        "-1": "0111010",
        "D": "0001100",
        "A": "0110000",
        "M": "1110000",
        "!D": "0001101",
        "!A": "0110001",
        "!M": "1110001",
        "-D": "0001111",
        "-A": "0110011",
        "-M": "1110011",
        "D+1": "0011111",
        "A+1": "0110111",
        "M+1": "1110111",
        "D-1": "0001110",
        "A-1": "0110010",
        "M-1": "1110010",
        "D+A": "0000010",
        "D+M": "1000010",
        "D-A": "0010011",
        "D-M": "1010011",
        "A-D": "0000111",
        "M-D": "1000111",
        "D&A": "0000000",
        "D&M": "1000000",
        "D|A": "0010101",
        "D|M": "1010101",
    }
    jump_syntax = {
        "null": "000",
        "JGT": "001",
        "JEQ": "010",
        "JGE": "011",
        "JLT": "100",
        "JNE": "101",
        "JLE": "110",
        "JMP": "111",
    }
    return dest_syntax, comp_syntax, jump_syntax


def instruction_type(lines, symbol):
    """
    process the corresponding command type.
    :param lines: input a list contain the assembly code
    :param symbol: input symbol table
    :return:
    """
    codes = []
    reg_addr = 16
    for line in lines:
        if line.startswith("@"):
            line = line.strip("@")
            if line.isdigit():
                code = a_type(int(line))
            elif line in symbol:
                code = a_type(symbol[line])
            else:
                symbol[line] = reg_addr
                code = a_type(reg_addr)
                reg_addr += 1
        else:
            code = c_type(line)
        codes.append(code)
    return codes


def base_conversion(decimal):
    """
    convert decimal to binary.
    :param decimal: input decimal
    :return: return a string about binary with leading zeros.
    """
    binary = "{:016b}".format(decimal)
    # binary = bin(decimal)[2:].zfill(16) # The second method
    return binary


def a_type(a_content):
    """
    process A instruction
    :param a_content: input A instruction
    :return: return binary code about A instruction
    """
    return base_conversion(a_content)


def c_type(c_content):
    """
    process C instruction
    :param c_content: input C instruction
    :return: return binary code about C instruction
    """
    dest_syntax, comp_syntax, jump_syntax = init_syntax()
    is_exist_comp = "=" in c_content
    is_exist_jump = ";" in c_content
    if is_exist_comp and is_exist_jump:
        dest, other = c_content.split("=")
        comp, jump = other.split(";")
    elif is_exist_comp:
        dest, comp = c_content.split("=")
        jump = "null"
    elif is_exist_jump:
        comp, jump = c_content.split(";")
        dest = "null"
    else:
        dest = "null"
        comp = c_content
        jump = "null"
    return "111" + comp_syntax[comp] + dest_syntax[dest] + jump_syntax[jump]


def to_binary_codes(filename, symbol):
    """
    convert assembly language to machine language.
    :param filename: input file path
    :param symbol: input symbol table
    :return: None
    """
    with open(filename[:-3] + "out", "r") as fr:
        lines = [line.strip() for line in fr.readlines()]
        codes = instruction_type(lines, symbol)
        with open(filename[:-3] + "hack", "w") as fw:
            fw.writelines("\n".join(codes))
