from lark import Lark
import os

with open(os.path.join(os.path.dirname(__file__), "grammar.lark"), encoding="utf-8") as grammar:
    lark_parser = Lark(grammar.read(), start="start", parser='lalr')
