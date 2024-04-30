# Generated from fourir.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .fourirParser import fourirParser
else:
    from fourirParser import fourirParser

# This class defines a complete generic visitor for a parse tree produced by fourirParser.

class fourirVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by fourirParser#prog.
    def visitProg(self, ctx:fourirParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fourirParser#printExpr.
    def visitPrintExpr(self, ctx:fourirParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fourirParser#blank.
    def visitBlank(self, ctx:fourirParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fourirParser#float.
    def visitFloat(self, ctx:fourirParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fourirParser#int.
    def visitInt(self, ctx:fourirParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fourirParser#dt.
    def visitDt(self, ctx:fourirParser.DtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fourirParser#N.
    def visitN(self, ctx:fourirParser.NContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fourirParser#FREQ.
    def visitFREQ(self, ctx:fourirParser.FREQContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fourirParser#Fin.
    def visitFin(self, ctx:fourirParser.FinContext):
        return self.visitChildren(ctx)



del fourirParser