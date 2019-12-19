#  File: ExpressionTree.py

#  Description: This file will input an expression into a tree and implement various functions
#  to modify it such as converting the expression into post-fix or in-fix

#  Student's Name: Victor Li

#  Student's UT EID: vql83

#  Partner's Name: Derek Wu

#  Partner's UT EID: dw29924

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 15 November, 2019

#  Date Last Modified: 15 November, 2019

class Stack (object):
    def __init__ (self):
        self.stack = []

    # add an item to the top of the stack
    def push (self, item):
        self.stack.append (item)

    # remove an item from the top of the stack
    def pop (self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek (self):
        return self.stack[-1]

    # check if the stack is empty
    def is_empty (self):
        return (len(self.stack) == 0)

    # return the number of elements in the stack
    def size (self):
        return (len (self.stack))

    def operate(oper1, oper2, token):
        if (token == '+'):
            return oper1 + oper2
        elif (token == '-'):
            return oper1 - oper2
        elif (token == '*'):
            return oper1 * oper2
        elif (token == '/'):
            return oper1 / oper2
        elif (token == '//'):
            return oper1 // oper2
        elif (token == '%'):
            return oper1 % oper2
        elif (token == '**'):
            return oper1 ** oper2

    def rpn (s):
        theStack = Stack ()
        operators = ['+', '-', '*', '/', '//', '%', '**']
        tokens = s.split()
        for item in tokens:
            if (item in operators):
              oper2 = theStack.pop()
              oper1 = theStack.pop()
              theStack.push (operate (oper1, oper2, item))
            else:
                theStack.push (float(item))
        return theStack.pop()

class Node(object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
    # self.parent = None
    # self.visited = False

class Tree (object):
    def __init__ (self):
        self.root = None

    def create_tree (self, expr):
        print("hi")

    def evaluate (self, aNode):
        print("hi")

    def pre_order (self, aNode):
        if (aNode != None):
            print(aNode.data)
            self.pre_order(aNode.lchild)
            self.pre_order(aNode.rchild)

    def post_order (self, aNode):
        if (aNode != None):
            self.post_order(aNode.lchild)
            self.post_order(aNode.rchild)
            print(aNode.data)

    def operate(oper1, oper2, token):
        if (token == '+'):
            return oper1 + oper2
        elif (token == '-'):
            return oper1 - oper2
        elif (token == '*'):
            return oper1 * oper2
        elif (token == '/'):
            return oper1 / oper2
        elif (token == '//'):
            return oper1 // oper2
        elif (token == '%'):
            return oper1 % oper2
        elif (token == '**'):
            return oper1 ** oper2
def main():
    f = "expression.txt"
    with open(f, 'r') as file:
        # read words from words.txt and append to word_list
        expression = file.read().splitlines()

    # close file words.txt
    file.close()

    print(expression)

main()
