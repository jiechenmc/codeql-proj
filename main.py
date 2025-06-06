import ast

# Path to your Python source file
filename = "/home/admin/codeql-proj/lambda/handler.py"
handler_file = ""
handler_name = "hello"


class HelloArgVisitor(ast.NodeVisitor):
    def visit_FunctionDef(self, node):
        if node.name == handler_name:
            args = node.args.args
            if args:
                print(args[0].arg)
            # else:
            #     print("'hello' has no arguments.")
        self.generic_visit(node)


with open(filename, "r") as f:
    tree = ast.parse(f.read())

HelloArgVisitor().visit(tree)
