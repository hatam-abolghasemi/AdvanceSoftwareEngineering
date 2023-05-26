from antlr4 import *
from antlr4.TokenStreamRewriter import TokenStreamRewriter
from gen.JavaLabeled.JavaParserLabeledListener import JavaParserLabeledListener
from gen.JavaLabeled.JavaParserLabeled import JavaParserLabeled


class CleanCode(JavaParserLabeledListener):
    # Initializes the CleanCode object, sets up instance variables, and raises an error if common_token_stream is None.
    def __init__(
            self, common_token_stream: CommonTokenStream = None, var_has_getset=None
    ):
        self.token_stream = common_token_stream
        self.imports = []
        self.used_imports = set()
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

    # Appends the method name to a stack when a method is entered.
    def enterMethodDeclaration(self, ctx: JavaParserLabeled.MethodDeclarationContext):
        self.stackMethodName.append(ctx.IDENTIFIER())

    # Pops the method out of the stack when a method is exited.
    def exitMethodDeclaration(self, ctx: JavaParserLabeled.MethodDeclarationContext):
        self.stackMethodName.pop()
        self.stackArgs = []
        self.stackAllVarOfMethod = []

    # 01. Small -----------------------------------------------------------------------------
    def enterMethodBody(self, ctx: JavaParserLabeled.MethodBodyContext):
        # Triggers when the number of lines in the method body exceeds 24.
        if str(ctx.children[0].getText()).count(";") > 24:
            print(f"Code is too big in  {self.stackMethodName[0]}  method")

    # Appends a context child to the stack of method variables.
    def enterLocalVariableDeclaration(self, ctx: JavaParserLabeled.LocalVariableDeclarationContext):
        self.stackAllVarOfMethod.append(ctx.children[1].children[0].children[0].getText())

    # 02. Use descriptive names -----------------------------------------------------------------------------
    def enterVariableDeclaratorId(self, ctx: JavaParserLabeled.VariableDeclaratorIdContext):
        # Triggers when a variable is declared and checks whether the variable's name is descriptive enough.
        name = ctx.IDENTIFIER().getText()
        if len(name) <= 3:
            print(f"{name} is not descriptive in method {self.stackMethodName[0]}")

    # Appends a child to the stack when a block is entered.
    def enterBlock(self, ctx: JavaParserLabeled.BlockContext):
        self.stack.append(ctx.children[0])

    # 02. Do one thing -----------------------------------------------------------------------------
    def exitBlock(self, ctx: JavaParserLabeled.BlockContext):
        # Pops the block out of the stack when a block is exited and checks whether a method does more than one thing.
        self.stack.pop()
        if len(self.stack) > 1:
            print(f"Method {self.stackMethodName[0]} does more than one thing !!!")

    # 03. Prefer fewer arguments -----------------------------------------------------------------------------
    def enterFormalParameterList0(self, ctx: JavaParserLabeled.FormalParameterList0Context):
        # Triggers when the number of parameters in the method exceeds 5.
        if ctx.getChildCount() > 5:
            print(f"Method {self.stackMethodName[0]} has many args")

    # 04. Have no side effects -----------------------------------------------------------------------------
    def enterExpression21(self, ctx: JavaParserLabeled.Expression21Context):
        # Triggers when the first expression of the method is not in the list of method variables.
        if ctx.children[0].getText() not in self.stackAllVarOfMethod:
            print(f"{ctx.getText()} has side effect in method {self.stackMethodName[0]}")

    # Enter Parameter -----------------------------------------------------------------------------
    def enterFormalParameter(self, ctx: JavaParserLabeled.FormalParameterContext):
        # Appends the parameter to the stack of method arguments.
        self.stackArgs.append(ctx.children[1].getText())
        self.stackAllVarOfMethod.append(ctx.children[1].getText())

    # 05. Don't use flag arguments -----------------------------------------------------------------------------
    def enterExpression14(self, ctx: JavaParserLabeled.Expression14Context):
        # Triggers when a flag argument (a boolean argument used to control the flow of a method) is used in the method.
        if (
                ctx.children[0].getText() in self.stackArgs or
                ctx.children[2].getText() in self.stackArgs
        ):
            try:
                self.stackArgs.remove(ctx.children[0].getText())
                self.stackArgs.remove(ctx.children[2].getText())
            except:
                pass
            print(f"Use flag in {ctx.getText()} in method {self.stackMethodName[0]}")


    # 06. Checks if the class name and method names follow camelCase convention. Also, checks if variable names are descriptive enough.
    def checkNamingConvention(self, ctx: ParserRuleContext):
        # Check if the class name and method names follow camelCase convention.
        if isinstance(ctx, JavaParserLabeled.ClassDeclarationContext):
            class_name = ctx.IDENTIFIER().getText()
            if not class_name[0].isupper():
                print(f"Class name '{class_name}' does not follow camelCase naming convention.")
        elif isinstance(ctx, JavaParserLabeled.MethodDeclarationContext):
            method_name = ctx.IDENTIFIER().getText()
            if not method_name[0].islower():
                print(f"Method name '{method_name}' does not follow camelCase naming convention.")

        # Check if variable names are descriptive enough.
        if isinstance(ctx, JavaParserLabeled.LocalVariableDeclarationStatementContext):
            variable_name = ctx.localVariableDeclaration().variableDeclarators().variableDeclarator()[0] \
                .variableDeclaratorId().IDENTIFIER().getText()
            if len(variable_name) <= 3:
                print(f"Variable name '{variable_name}' is not descriptive enough.")

    # 07. Checks if all imported packages are used in the code.
    def enterImportDeclaration(self, ctx:JavaParserLabeled.ImportDeclarationContext):
        imp = ctx.IMPORT().getText()
        if not imp.startswith("import "): # only add if it's not a keyword
            self.imports.append(imp)

    def enterTypeDeclaration(self, ctx:JavaParserLabeled.TypeDeclarationContext):
        for child in ctx.getChildren():
            if isinstance(child, JavaParserLabeled.TypeTypeContext):
                type_name = child.getText()
                self.used_imports.add(type_name)

    def exitCompilationUnit(self, ctx:JavaParserLabeled.CompilationUnitContext):
        unused_imports = [i for i in self.imports if i not in self.used_imports]
        for i in unused_imports:
            pkg_name = i.split()[-1] # get last part of import statement
            print(f"Unused import '{pkg_name}' found in the code.")


    # 08. Checks for magic numbers in the code.
    def checkMagicNumbers(self, ctx: ParserRuleContext):
        # Check for magic numbers in the code.
        if isinstance(ctx, JavaParserLabeled.LiteralContext):
            literal = ctx.getText()
            if literal.isdigit():
                print(f"Magic number '{literal}' found in the code.")

    # 09. Checks for unused variables in the code.
    def checkUnusedVariables(self, ctx: ParserRuleContext):
        # Check for unused variables in the code.
        if isinstance(ctx, JavaParserLabeled.LocalVariableDeclarationStatementContext):
            variable_name = ctx.localVariableDeclaration().variableDeclarators() \
                .variableDeclarator()[0].variableDeclaratorId().IDENTIFIER().getText()

            # Get all the variable references in the current parsing context.
            variable_references = [x.getText() for x in ctx.descendants() if isinstance(x, JavaParserLabeled.PrimaryContext)]

            if variable_name not in variable_references:
                print(f"Unused variable '{variable_name}' found in the code.")

    # 10. Checks for code duplication in the code.
    def checkCodeDuplication(self, ctx: ParserRuleContext):
        # Check for code duplication in the code.
        if isinstance(ctx, JavaParserLabeled.MethodDeclarationContext):
            method_name = ctx.IDENTIFIER().getText()
            method_body = ctx.methodBody().getText()

            # Search for the current method body in all other method bodies.
            if sum(1 for x in self.stackAllVarOfMethod if method_body in x) > 1:
                print(f"Code duplication found in method '{method_name}'.")
