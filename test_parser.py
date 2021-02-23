from parser import make_parser, run_parser, make_ast
import json

parser = make_parser()

def test_from_file(inputName, outputName, errorMsg="Test failed"):
    inputFile = open(inputName)
    input = inputFile.read()
    inputFile.close()
    ast = make_ast(input, parser)

    #Compare to output file
    with open(outputName) as outputFile:
        expected = json.load(outputFile)
        if ast != expected: print(errorMsg) 



#run tests here
def test_numExpr():
    print("============================")
    print("Testing:9001")
    input = "9001;"
    expected = {
        "type": "program",
        "value": {
            "type": "numExpr",
            "value": 9001
        }
    }
    ast = make_ast(input, parser)
    if ast != expected: print("test:9001 did not pass")  

    print("Testing:1 + 1")
    input = "1+ 1;"
    expected = {
        "type": "program",
        "value": {
            "type": "numExpr",
            "value": 2 #Optimization thing
        }
    }
    ast = make_ast(input, parser)
    if ast != expected: print("test:1 + 1 did not pass")  

    print("Testing:Order of operations")
    input = "2 + 8 / 2;"
    expected = {
        "type": "program",
        "value": {
            "type": "numExpr",
            "value": 6.0 #This type can be either an int or float
        }
    }
    ast = make_ast(input, parser)
    if ast != expected: print("test:Order of operations did not pass")  

    print("Testing:Brackets in numExpr")
    input = "(2 + 8) / 2;"
    expected = {
        "type": "program",
        "value": {
            "type": "numExpr",
            "value": 5.0 #This type can be either an int or float
        }
    }
    ast = make_ast(input, parser)
    if ast != expected: print("test:Brackets in numExpr did not pass")  

    print("Testing:Negative numbers")
    input = "-6 / 2;"
    expected = {
        "type": "program",
        "value": {
            "type": "numExpr",
            "value": -3.0 #This type can be either an int or float
        }
    }
    ast = make_ast(input, parser)
    if ast != expected: print("test:Negative numbers did not pass")  

def test_boolExpr():
    print("============================")
    print("Testing:uwu")
    input = "uwu;"
    expected = {
        "type": "program",
        "value": {
            "type": "boolExpr",
            "value": True
        }
    }
    ast = make_ast(input, parser)
    if ast != expected: print("test:uwu did not pass")  

    print("Testing:brackets in boolExpr")
    input = "(owo);"
    expected = {
        "type": "program",
        "value": {
            "type": "boolExpr",
            "value": [
                "(",
                {
                    "type": "boolExpr",
                    "value": False
                },
                ")"
            ]
        }
    }
    ast = make_ast(input, parser)
    if ast != expected: print("test:brackets in boolExpr did not pass")  

    print("Testing:! boolExpr")
    input = "!owo;"
    expected = {
        "type": "program",
        "value": {
            "type": "boolExpr",
            "value": True
        }
    }
    ast = make_ast(input, parser)
    if ast != expected: print("test:! boolExpr did not pass")  

    print("Testing:1 < 2")
    input = "1 <2;"
    expected = {
        "type": "program",
        "value": {
            "type": "boolExpr",
            "value": True
        }
    }
    ast = make_ast(input, parser)
    if ast != expected: print("test:1 < 2 did not pass")  

    print("Testing:1 == uwu") 
    #This may need to be modified in the future due to how Python works
    input = "1 == uwu;"
    expected = {
        "type": "program",
        "value": {
            "type": "boolExpr",
            "value": True
        }
    }
    ast = make_ast(input, parser)
    if ast != expected: print("test:1 == uwu did not pass")  

    print("Testing:1 != uwu")
    #This may need to be modified in the future due to how Python works
    input = "1 != uwu;"
    expected = {
        "type": "program",
        "value": {
            "type": "boolExpr",
            "value": False
        }
    }
    ast = make_ast(input, parser)
    if ast != expected: print("test:1 != uwu did not pass")  

    print("Testing:uwu || owo")
    input = "uwu || owo;"
    expected = {
        "type": "program",
        "value": {
            "type": "boolExpr",
            "value": True
        }
    }
    ast = make_ast(input, parser)
    if ast != expected: print("test:uwu || owo did not pass")  

    # print("Testing:Chaining boolExpr")
    # input = "uwu && (1 < 5 || uwu);"
    # expected = {
    #     "type": "program",
    #     "value": {
    #         "type": "boolExpr",
    #         "value": True
    #     }
    # }
    # ast = make_ast(input, parser)
    # if ast != expected: print("test:Chaining boolExpr did not pass")  

def test_arrays():
    print("============================")
    print("Testing:Arrays")
    inputName = "array_example.owo"
    outputName = "array_output.json"
    test_from_file(inputName, outputName, "Array tests did not pass")






if __name__ == "__main__":
    test_numExpr()
    test_boolExpr()
    test_arrays()

