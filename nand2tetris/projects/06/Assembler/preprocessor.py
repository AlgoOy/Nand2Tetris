def handle_symbol(filename, symbol):
    """
    this function will add label symbol to symbol table, at the same time,
    it will delete the space and comment which in the origin assembly file.
    :param filename: assembly file name
    :param symbol: symbol table
    :return: the modified symbol table and generate an intermediate file
    """
    with open(filename, "r") as fr:
        codes = []
        index = 0
        for line in fr.readlines():
            line = line.strip()
            if not (len(line)) or line.startswith("//"):
                continue
            elif line.startswith("("):
                symbol[line.strip("()")] = index
            else:
                loc = line.find("//")
                if loc != -1:
                    line = line[0:loc].strip()
                codes.append(line)
                index += 1
        with open(filename[:-3] + "out", "w") as fw:
            fw.writelines("\n".join(codes))
