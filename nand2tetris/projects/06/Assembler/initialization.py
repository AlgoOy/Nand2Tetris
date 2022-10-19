def init_symbol():
    """
    init the symbol table
    :return: a dict about symbol table
    """
    symbol = {f"R{i}": i for i in range(16)}
    symbol["SP"] = 0
    symbol["LCL"] = 1
    symbol["ARG"] = 2
    symbol["THIS"] = 3
    symbol["THAT"] = 4
    symbol["SCREEN"] = 16384
    symbol["KBD"] = 24576
    return symbol
