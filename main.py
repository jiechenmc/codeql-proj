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


services = [
    "s3",
    "dynamodb",
    "lambda",
    "ssm",
    "sqs",
    "sns",
    "ec2",
    "sts",
    "rekognition",
    "cloudformation",
    "stepfunctions",
]

sink_common_verbs = [
    "batch",
    "put",
    "create",
    "delete",
    "download",
    "copy",
    "upload",
    "cancel",
    "update",
    "execute",
    "query",
    "scan",
    "invoke",
    "add",
    "remove",
    "terminate",
    "send",
    "change",
    "purge",
    "set",
    "confirm",
    "subscribe",
    "publish",
    "opt",
    "check",
    "list",
    "run",
    "associate",
    "accept",
    "allocate",
    "assign",
    "detatch",
    "disable",
    "enable",
    "release",
    "purchase",
    "modify",
    "reset",
    "revoke",
    "restore",
    "unassign",
    "search",
    "assume",  # sts
    "decode",  # sts
    "detect",  # sts
    "recognize",  # sts
    "activate",  # cloudformation
    "import",
    "describe",
    "signal",
]

source_common_verb = ["receive", "get"]
