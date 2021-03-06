from evaluator import Result
from nodes import Node
from moduals.moduals import Module

maths = Module("maths")


@maths.register
class Add(Node):
    full_name = "addition"
    op_name = "add"
    inputs = ("a", "b")
    input_slots = {"a":"text.line_num",
                   "b":"text.line_num"
                   }
    outputs = ("sum",)
    description = "takes inputs a and b and returns the sum "

    def eval(self, data):
        out = data["a"] + data["b"]
        return Result(sum=out)


@maths.register
class Subtract(Node):
    full_name = "subtraction"
    op_name = "sub"
    inputs = ("a", "b")
    input_slots = {"a": "text.line_num",
                   "b": "text.line_num"
                   }
    outputs = ("difference", )
    description = "takes inputs a and b and returns the difference (a - b) "
    def eval(self, data):
        out = data.a - data.b
        return Result(difference=out)


@maths.register
class Multiply(Node):
    full_name = "multiply"
    op_name = "mul"
    inputs = ("a", "b")
    input_slots = {"a": "text.line_num",
                   "b": "text.line_num"
                   }
    outputs = ("product", )
    description = "takes inputs a and b, returns the product of a and b"
    def eval(self, data):
        out = data["a"] + data["b"]
        return Result(product=out)


@maths.register
class Divide(Node):
    full_name = "divide"
    op_name = "div"
    inputs = ("a", "b")
    input_slots = {"a": "text.line_num",
                   "b": "text.line_num"
                   }
    outputs = ("result",)
    description = "takes inputs a and b and return a divided by b"
    def eval(self, data):
        try:
            out = data["a"] / data["b"]
        except ZeroDivisionError:
            return Result(exeption=True)
        return Result(result=out)


@maths.register
class Exponentiation(Node):
    full_name = "exponentiation"
    op_name = "pow"
    inputs = ("a", "b")
    input_slots = {"a": "text.line_num",
                   "b": "text.line_num"
                   }
    outputs = ("result",)

    def eval(self, data):
        out = data["a"] ** data["b"]
        return Result(result=out)


@maths.register
class Modulus(Node):
    full_name = "modulus"
    op_name = "mod"
    inputs = ("a", "b")
    input_slots = {"a": "text.line_num",
                   "b": "text.line_num"
                   }
    outputs = ("remainder",)
    description = "takes input a and b and returns the modulus ( a % b)"

    def eval(self, data):
        out = data["a"] % data["b"]
        return Result(sum=out)

