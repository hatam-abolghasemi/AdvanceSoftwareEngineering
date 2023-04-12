cd Grammars
antlr4 -Dlanguage=Python3 -visitor JavaLexer.g4 -o ../gen/JavaLexer
antlr4 -Dlanguage=Python3 -visitor JavaParserLabeled.g4 -lib ../gen/JavaLexer -o ../gen/JavaLabeled