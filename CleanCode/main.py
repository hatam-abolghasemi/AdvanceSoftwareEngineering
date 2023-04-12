import os
from antlr4 import *
from Resources.CleanCode import CleanCode
from gen.JavaLabeled.JavaParserLabeled import JavaParserLabeled
from gen.JavaLexer.JavaLexer import JavaLexer


def main(directory_path: str = ""):
    obj = []

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".java"):
                stream = FileStream(
                    os.path.join(root, file), encoding="utf8", errors="ignore"
                )
                lexer = JavaLexer(stream)
                token_stream = CommonTokenStream(lexer)
                token_stream.fill()
                parser = JavaParserLabeled(token_stream)
                ef_listener = CleanCode(
                    common_token_stream=token_stream, var_has_getset=obj
                )
                tree = parser.compilationUnit()
                walker = ParseTreeWalker()
                walker.walk(t=tree, listener=ef_listener)
    return True


main(directory_path="JavaProject")
