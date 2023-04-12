import os
from antlr4 import *
from antlr4.TokenStreamRewriter import TokenStreamRewriter
from gen.JavaLabeled.JavaParserLabeledListener import JavaParserLabeledListener
from gen.JavaLabeled.JavaParserLabeled import JavaParserLabeled
from gen.JavaLexer.JavaLexer import JavaLexer


class CleanCode(JavaParserLabeledListener):
    def __init__(
        self, common_token_stream: CommonTokenStream = None, var_has_getset=None
    ):
        self.token_stream = common_token_stream
        self.stack = []
        self.stackMethodName = []
        self.stackArgs = []
        self.stackAllVarOfMethod = []
        self.getter_exist = False
        self.setter_exist = False
        self.object = []
        self.variables_has_getter_setter = var_has_getset
        if common_token_stream is not None:
            self.token_stream_rewriter = TokenStreamRewriter(common_token_stream)
        else:
            raise TypeError("common_token_stream is None")

    def enterMethodDeclaration(self, ctx: JavaParserLabeled.MethodDeclarationContext):
        """

        :param ctx:
        :return:
        """
        self.stackMethodName.append(ctx.IDENTIFIER())

    def exitMethodDeclaration(self, ctx: JavaParserLabeled.MethodDeclarationContext):
        """

        :param ctx:
        :return:
        """
        self.stackMethodName.pop()
        self.stackArgs = []
        self.stackAllVarOfMethod = []

    def enterMethodBody(self, ctx: JavaParserLabeled.MethodBodyContext):
        """
        this method  is check method is small or not
        :param ctx:
        :return:
        """
        if str(ctx.children[0].getText()).count(";") > 24:
            print(f"code is too big in  {self.stackMethodName[0]}  method")

    def enterLocalVariableDeclaration(
        self, ctx: JavaParserLabeled.LocalVariableDeclarationContext
    ):
        """

        :param ctx:
        :return:
        """
        self.stackAllVarOfMethod.append(ctx.children[1].children[0].children[0].getText())

    def enterBlock(self, ctx: JavaParserLabeled.BlockContext):
        """

        :param ctx:
        :return:
        """
        self.stack.append(ctx.children[0])

    def exitBlock(self, ctx: JavaParserLabeled.BlockContext):
        """

        :param ctx:
        :return:
        """
        self.stack.pop()
        if len(self.stack) > 1:
            print(f"method {self.stackMethodName[0]} do more than one thing !!!")

    def enterFormalParameterList0(
        self, ctx: JavaParserLabeled.FormalParameterList0Context
    ):
        """

        :param ctx:
        :return:
        """
        if ctx.getChildCount() > 5:
            print(f"method {self.stackMethodName[0]} has many args")

    def enterExpression21(self, ctx: JavaParserLabeled.Expression21Context):
        """
        method to check side effect
        :param ctx:
        :return:
        """
        # print("*"*100)
        # print("LOCAL VARS : ", self.stackAllVarOfMethod)
        # print("TEST VAR : ", ctx.children[0].getText())
        # print("METHOD : ", self.stackMethodName[0])
        # print("*" * 100)
        if ctx.children[0].getText() not in self.stackAllVarOfMethod:
            print(
                f"{ctx.getText()} has side effect in method {self.stackMethodName[0]}"
            )

    def enterFormalParameter(self, ctx: JavaParserLabeled.FormalParameterContext):
        self.stackArgs.append(ctx.children[1].getText())
        self.stackAllVarOfMethod.append(ctx.children[1].getText())

    def enterExpression14(self, ctx: JavaParserLabeled.Expression14Context):
        if (
            ctx.children[0].getText() in self.stackArgs
            or ctx.children[2].getText() in self.stackArgs
        ):
            try:
                self.stackArgs.remove(ctx.children[0].getText())
                self.stackArgs.remove(ctx.children[2].getText())
            except:
                pass
            print(f"use flag in {ctx.getText()} in method {self.stackMethodName[0]}")
