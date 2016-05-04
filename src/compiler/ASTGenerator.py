# following 4 lines were necessary to import Program
import os
import sys
lib_path = os.path.abspath(os.path.join('.', 'nodes'))
sys.path.append(lib_path)

from SmallCVisitor import SmallCVisitor
from SmallCParser import SmallCParser
from Program import Program
from IncludeDirective import IncludeDirective

class ASTGenerator(SmallCVisitor):
    def __init__(self, ast, parsetree):
        self.ast = ast
        self.parsetree = parsetree
        
        
    def generate(self):
        return self.visitSmallc_program(self.parsetree)
            
    
    def visitSmallc_program(self, parsetree:SmallCParser.Smallc_programContext):
        include_contexts = parsetree.include()
        function_contexts = parsetree.function_definition()

        include_directives = []
        for inc_ctx in include_contexts:
            print("for loop:", inc_ctx.getText())
            include_directives.append(self.visit(inc_ctx))
        print(include_directives)
        
        functions = []
        '''
        for func_ctx in function_contexts:
            # print(func_ctx.getText())
            # print(self.visit(func_ctx))
            functions.append(self.visit(func_ctx))
        print(functions)
        '''
        
        return Program(self.ast, include_directives, functions)
	
	
    def visitInclude(self, parsetree:SmallCParser.IncludeContext):
        return IncludeDirective(self.ast, parsetree.FILENAME().getText())
    
    
    def visitFunction_definition(self, parsetree:SmallCParser.Function_definitionContext):
        self.ast.symbol_table.incrementScope()
        self.ast.call_stack.incrementDepth()

        type_spec = self.visit(parsetree.type_specifier())
        type_name = type_spec.getType()
        
        identifier = parsetree.id().IDENTIFIER().getText()

        '''        
            TODO
			ParameterDeclarationList parameter_list;
			if (parsetree.param_decl_list() == None)
				parameter_list = new ParameterDeclarationList(ast,
						new ArrayList<ParameterDeclaration>(), false);
			else
				parameter_list = (ParameterDeclarationList) self.visit(parsetree
						.param_decl_list());
        
        '''
                
        if parsetree.compound_stmt() == None:
            statement = None
        else:
            statement = visitCompound_stmt(parsetree.compound_stmt(), True)
        
        self.ast.call_stack.decrementDepth()

        '''
            TODO
			Function func = new Function(self.ast, type, identifier, parameter_list,
					statement, parsetree.EXTERN() != null);
        '''
        
        self.ast.symbol_table.decrementScope()
		
        '''
		    TODO
    		return func
    	'''
