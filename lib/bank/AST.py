# ABSTRACT SYNTAX TREE (AST) CLASS
# Taite Krogfus
# 04/28/2026
# Final Project
# DESCRIPTION: Defines the ASTNode class used to build the Abstract Syntax Tree (AST)
# for the Banking DSL. Each node represents a part of a command and may contain child
# nodes to form a hierarchical structure. The AST is used by the Parser and Interpreter
# to understand and execute commands.

class ASTNode:
    # allows for no value to be passed (e.g., PROGRAM node requires no value)
    def __init__(self, node_type, value=None):
        self.__node_type = node_type
        self.__value = value
        self.__children = []

    def get_node_type(self):
        return self.__node_type

    def get_value(self):
        return self.__value

    def get_children(self):
        return self.__children

    def set_node_type(self, node_type):
        self.__node_type = node_type

    def set_value(self, value):
        self.__value = value

    #will be used in Parser.py
    def add_child(self, child_node):
        self.__children.append(child_node) # private list of child nodes

    #formatting for printing AST output in a clear and efficient way
    def __str__(self):
        return f"ASTNode({self.__node_type}, {self.__value}, children={self.__children})"

    def __repr__(self):
        return self.__str__()
