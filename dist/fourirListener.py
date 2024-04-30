# Generated from fourir.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .fourirParser import fourirParser
else:
    from fourirParser import fourirParser

# This class defines a complete listener for a parse tree produced by fourirParser.
class fourirListener(ParseTreeListener):

    # Enter a parse tree produced by fourirParser#prog.
    def enterProg(self, ctx:fourirParser.ProgContext):
        pass

    # Exit a parse tree produced by fourirParser#prog.
    def exitProg(self, ctx:fourirParser.ProgContext):
        pass


    # Enter a parse tree produced by fourirParser#printExpr.
    def enterPrintExpr(self, ctx:fourirParser.PrintExprContext):
        pass

    # Exit a parse tree produced by fourirParser#printExpr.
    def exitPrintExpr(self, ctx:fourirParser.PrintExprContext):
        pass


    # Enter a parse tree produced by fourirParser#blank.
    def enterBlank(self, ctx:fourirParser.BlankContext):
        pass

    # Exit a parse tree produced by fourirParser#blank.
    def exitBlank(self, ctx:fourirParser.BlankContext):
        pass


    # Enter a parse tree produced by fourirParser#float.
    def enterFloat(self, ctx:fourirParser.FloatContext):
        pass

    # Exit a parse tree produced by fourirParser#float.
    def exitFloat(self, ctx:fourirParser.FloatContext):
        pass


    # Enter a parse tree produced by fourirParser#int.
    def enterInt(self, ctx:fourirParser.IntContext):
        pass

    # Exit a parse tree produced by fourirParser#int.
    def exitInt(self, ctx:fourirParser.IntContext):
        pass


    # Enter a parse tree produced by fourirParser#dt.
    def enterDt(self, ctx:fourirParser.DtContext):
        pass

    # Exit a parse tree produced by fourirParser#dt.
    def exitDt(self, ctx:fourirParser.DtContext):
        pass


    # Enter a parse tree produced by fourirParser#N.
    def enterN(self, ctx:fourirParser.NContext):
        pass

    # Exit a parse tree produced by fourirParser#N.
    def exitN(self, ctx:fourirParser.NContext):
        pass


    # Enter a parse tree produced by fourirParser#FREQ.
    def enterFREQ(self, ctx:fourirParser.FREQContext):
        pass

    # Exit a parse tree produced by fourirParser#FREQ.
    def exitFREQ(self, ctx:fourirParser.FREQContext):
        pass


    # Enter a parse tree produced by fourirParser#Fin.
    def enterFin(self, ctx:fourirParser.FinContext):
        pass

    # Exit a parse tree produced by fourirParser#Fin.
    def exitFin(self, ctx:fourirParser.FinContext):
        pass



del fourirParser