from parser import make_parser, run_parser, reset_parser, make_ast
import json

parser = make_parser()

def output_to_file(inputName, outputName):
    inputFile = open(inputName)
    input = inputFile.read()
    inputFile.close()
    run_parser(input, outputName, parser)

    parser.restart() 



#run tests here
def test_vars():
    print("============================")
    print("Testing:Declare waifu")
    input = "waifu varName;"
    expected = {
        "type": "program",
        "value": [{
            "type": "declaration",
            "returnType": "waifu",
            "array": False,
            "value": {
                "value": "varName",
                "referenced": 0
            }
        }]
    }
    ast = make_ast(input, parser)
    if ast != expected: print("test:Declare waifu did not pass") 

    print("Testing:Waifu initialization")
    input = "waifu y = 2.5;"
    expected = {
        "type": "program",
        "value": [{
            "type": "initialize",
            "value": [
              {
                "type": "waifu",
                "value": {
                  "value": "y",
                  "referenced": 0
                }
              },
              "=",
              {
                "type": "numExpr",
                "returnType": "waifu",
                "value": 2.5
              }
            ]
        }]
    }
    ast = make_ast(input, parser)
    if ast != expected: print("test:Waifu initialization did not pass") 

    print("Testing:Waifu reassignment")
    input = "y = 500;" # y has already been initialized previously
    expected = {
        "type": "program",
        "value": [{
            "type": "reassign",
            "value": [
                "y",
                "=",
                {
                  "type": "numExpr",
                  "returnType": "waifu",
                  "value": 500
                }
            ]
        }]
    }
    ast = make_ast(input, parser)
    if ast != expected: print("test:Waifu reassignment did not pass")
    
    print("Testing:Waifu reference")
    input = "waifu z = 42; z;"
    expected = {
      "type": "program",
      "value": [
        {
          "type": "initialize",
          "value": [
            {
              "type": "waifu",
              "value": {
                "value": "z",
                "referenced": 1
              }
            },
            "=",
            {
              "type": "numExpr",
              "returnType": "waifu",
              "value": 42
            }
          ]
        },
        {
          "type": "letReference",
          "returnType": "waifu",
          "value": {
            "type": "waifu",
            "value": "z"
          }
        }
      ]
    }
    ast = make_ast(input, parser)
    if ast != expected: print("test:Waifu reference did not pass")

    print("Testing:Catgirl const")
    input = "real catgirl a = uwu;"
    expected = {
        "type": "program",
        "value": [{
            "type": "constInitialize",
            "value": [
              {
                "type": "catgirl",
                "value": {
                "value": "a",
                "referenced": 0
              }
              },
              "=",
              {
                "type": "boolExpr",
                "returnType": "catgirl",
                "value": True
              }
            ]
        }]
    }
    ast = make_ast(input, parser)
    if ast != expected: print("test:Catgirl const did not pass")

    print("Testing:Catgirl assign const")
    input = "real catgirl b = a;"
    expected = {
        "type": "program",
        "value": [{
            "type": "constInitialize",
            "value": [
              {
                "type": "catgirl",
                "value": {
                  "value": "b",
                  "referenced": 0
                }
              },
              "=",
              {
                "type": "letReference", 
                "returnType": "catgirl",
                "value": {
                  "type": "catgirl",
                  "value": "a"
                }
              }
            ]
        }]
    }
    ast = make_ast(input, parser)
    if ast != expected: print("test:Catgirl assign const did not pass")

    print("Testing:Catgirl 1D array declaration")
    input = "catgirl harem A;"
    expected = {
        "type": "program",
        "value": [{
            "type": "declaration",
            "returnType": "catgirl harem",
            "array": True,
            "value": {
              "type": "catgirl harem",
              "value": {
                "value": "A",
                "referenced": 0
              }
            }
        }]
    }
    ast = make_ast(input, parser)
    if ast != expected: print("test:Catgirl 1D array declaration did not pass")

    print("Testing:Catgirl 1D array reassignment")
    input = "A = [uwu];"
    expected = {
        "type": "program",
        "value": [{
            "type": "reassign",
            "value": [
              "A",
              "=",
              {
                "type": "arrayLiteral",
                "returnType": "catgirl harem",
                "value": [
                  "[",
                  {
                    "type": "boolExpr",
                    "returnType": "catgirl",
                    "value": True
                  },
                  "]"
                ]}]
        }]
    }
    ast = make_ast(input, parser)
    if ast != expected: print("test:Catgirl array reassignment did not pass")

    print("Testing:Catgirl 1D array reference")
    input = "A[0];"
    expected = {
        "type": "program",
        "value": [{
          "type": "arrayReference",
          "returnType": "catgirl",
          "value": [
             {
              "type": "letReference",
              "returnType": "catgirl harem",
              "value": {
                "type": "catgirl harem",
                "value": "A"
              }
        },
            "[",
            {
              "type": "numExpr",
              "returnType": "waifu",
              "value": 0
            },
            "]"
          ]
        }]
    }
    ast = make_ast(input, parser)
    if ast != expected: print("test:Catgirl 1D array reference did not pass")

    reset_parser()  

def test_numExpr():
    print("============================")
    print("Testing:9001")
    input = "9001;"
    expected = {
        "type": "program",
        "value": [{
            "type": "numExpr",
            "returnType": "waifu",
            "value": 9001
        }]
    }
    ast = make_ast(input, parser)
    if ast != expected: print("test:9001 did not pass")  

    print("Testing:1 + 1")
    input = "1+ 1;"
    expected = {
        "type": "program",
        "value": [{
            "type": "numExpr",
            "returnType": "waifu",
            "value": 2 #Optimization thing
        }]
    }
    ast = make_ast(input, parser)
    if ast != expected: print("test:1 + 1 did not pass")  

    print("Testing:Order of operations")
    input = "2 + 8 / 2;"
    expected = {
        "type": "program",
        "value": [{
            "type": "numExpr",
            "returnType": "waifu",
            "value": 6.0 #This type can be either an int or float
        }]
    }
    ast = make_ast(input, parser)
    if ast != expected: print("test:Order of operations did not pass")  

    print("Testing:Brackets in numExpr")
    input = "(2 + 8) / 2;"
    expected = {
        "type": "program",
        "value": [{
            "type": "numExpr",
            "returnType": "waifu",
            "value": 5.0 #This type can be either an int or float
        }]
    }
    ast = make_ast(input, parser)
    if ast != expected: print("test:Brackets in numExpr did not pass")  

    print("Testing:Negative numbers")
    input = "-6 / 2;"
    expected = {
        "type": "program",
        "value": [{
            "type": "numExpr",
            "returnType": "waifu",
            "value": -3.0 #This type can be either an int or float
        }]
    }
    ast = make_ast(input, parser)
    if ast != expected: print("test:Negative numbers did not pass")  
    
    #TODO: Add 2 binops, pow, mod
    parser.restart() 


def test_boolExpr():
    print("============================")
    print("Testing:uwu")
    input = "uwu;"
    expected = {
        "type": "program",
        "value": [{
            "type": "boolExpr",
            "returnType": "catgirl",
            "value": True
        }]
    }
    ast = make_ast(input, parser)
    if ast != expected: print("test:uwu did not pass")  

    print("Testing:brackets in boolExpr")
    input = "(owo);"
    expected = {
        "type": "program",
        "value": [{
            "type": "boolExpr",
            "returnType": "catgirl",
            "value": False
        }]
    }
    ast = make_ast(input, parser)
    if ast != expected: print("test:brackets in boolExpr did not pass")  

    print("Testing:! boolExpr")
    input = "!owo;"
    expected = {
        "type": "program",
        "value": [{
            "type": "boolExpr",
            "returnType": "catgirl",
            "value": True
        }]
    }
    ast = make_ast(input, parser)
    if ast != expected: print("test:! boolExpr did not pass")  

    print("Testing:1 < 2")
    input = "1 <2;"
    expected = {
        "type": "program",
        "value": [{
            "type": "boolExpr",
            "returnType": "catgirl",
            "value": True
        }]
    }
    ast = make_ast(input, parser)
    if ast != expected: print("test:1 < 2 did not pass")  

    # print("Testing:1 != uwu")
    # #This may need to be modified in the future due to how Python works
    # input = "1 != uwu;"
    # expected = {
    #     "type": "program",
    #     "value": [{
    #         "type": "boolExpr",
    #         "value": False
    #     }]
    # }
    # ast = make_ast(input, parser)
    # if ast != expected: print("test:1 != uwu did not pass")  

    print("Testing:uwu || owo")
    input = "uwu || owo;"
    expected = {
        "type": "program",
        "value": [{
            "type": "boolExpr",
            "returnType": "catgirl",
            "value": True
        }]
    }
    ast = make_ast(input, parser)
    if ast != expected: print("test:uwu || owo did not pass")  

    print("Testing:Chaining boolExpr")
    input = "uwu && (1 < 5 || uwu);"
    expected = {
        "type": "program",
        "value": [{
            "type": "boolExpr",
            "returnType": "catgirl",
            "value": True
        }]
    }
    ast = make_ast(input, parser)
    if ast != expected: print("test:Chaining boolExpr did not pass") 

    parser.restart() 


def read_test_file(filename):
  counter = 1
  with open(filename) as f:
    for line in f:
      try:
        make_ast(line, parser)
      except Exception as e:
        errStr = " ".join(str(e).split()[:-1]) #remove line counter
        print(errStr, str(counter)) #Have our own line counter
        reset_parser()
      counter += 1

if __name__ == "__main__":
    test_vars()
    test_numExpr()
    test_boolExpr()
    print("==================================")
    print("Testing type errors on expressions")
    read_test_file("./Example/Errors/typeErrors.owo")
    print("==================================")
    print("Testing errors on functions")
    read_test_file("./Example/Errors/functionErrors.owo")
    print("==================================")
    print("Testing errors on variables")
    read_test_file("./Example/Errors/varErrors.owo")
    print("==================================")
    print("Testing complete.")

