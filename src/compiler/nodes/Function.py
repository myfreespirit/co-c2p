# following 4 lines were necessary to import Type
import os
import sys
lib_path = os.path.abspath(os.path.join('.', 'types'))
sys.path.append(lib_path)

from AST import AST
from ASTNode import ASTNode
from Type import Type
from ControlStructure import ControlStructure

class Function(ASTNode, ControlStructure):    

    def __init__(self, ast, return_type, identifier, parameters, content, extern):
        ASTNode.__init__(self, ast)
        ControlStructure.__init__(self)
        
        self.return_type = return_type
        self.identifier = identifier
        self.extern = extern
        self.parameters = parameters
        self.addChild(parameters)
        self.content = content
        
        if(content != None):
            self.addChild(content)
        
        self.depth = ast.call_stack.getNestingDepth()
        
    def isForwardDeclaration(self):
        return self.content == None
        
    def getReturnLabel(self):
        return "function_" + self.identifier + "_return"
    
    def getBreakLabel(self):
        return None
        
    def getContinueLabel(self):
        return None
        
    def getDisplayableText(self):
        if(isForwardDeclaration()):
            return "declaration of function '" + self.identifier + "'"
        return "definition of function '" + self.identifier + "'"
        
    def generateCode(self, out):
        # TODO
        pass
