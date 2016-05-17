import sys
from .Expression import Expression
from compiler.types.BooleanType import BooleanType


class Relation(Expression):

    def __init__(self, ast, equation1, equation2, operator):
        super().__init__(ast)
        self.equation1 = equation1
        self.equation2 = equation2
        self.operator = operator
        self.addChild(self.equation1)
        self.addChild(self.equation2)
        self.operand_type = self.equation1.result_type.getPoorest(
            self.equation2.result_type)
        self.result_type = BooleanType()

    def getDisplayableText(self):
        return self.operator

    def generateCode(self, out):
        # Get p-code datatype for this expression
        p_type = self.operand_type.getPSymbol()

        # First get the operands on top of the stack
        self.equation1.generateCode(out)
        self.cast(self.equation1, out)
        self.equation2.generateCode(out)
        self.cast(self.equation2, out)

        # Execute the relevant operation on the operands
        if self.operator is "<":
            self.writeInstruction("les " + p_type, out)
        elif self.operator is ">":
            self.writeInstruction("grt " + p_type, out)
        else:
            print("Error:", self.operator, " is not implemented.")
            sys.exit(1)
