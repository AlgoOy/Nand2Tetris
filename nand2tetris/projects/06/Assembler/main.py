import initialization
import preprocessor
import assembly_parser

filename_list = [
    "../add/Add.asm",
    "../max/Max.asm",
    "../max/MaxL.asm",
    "../pong/Pong.asm",
    "../pong/PongL.asm",
    "../rect/Rect.asm",
    "../rect/RectL.asm",
]
for filename in filename_list:
    symbol = initialization.init_symbol()
    preprocessor.handle_symbol(filename, symbol)
    assembly_parser.to_binary_codes(filename, symbol)
