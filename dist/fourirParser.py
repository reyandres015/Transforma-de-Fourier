# Generated from fourir.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,11,34,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,1,
        1,1,1,1,1,1,3,1,16,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,3,2,32,8,2,1,2,0,0,3,0,2,4,0,0,37,0,7,1,0,0,0,2,15,
        1,0,0,0,4,31,1,0,0,0,6,8,3,2,1,0,7,6,1,0,0,0,8,9,1,0,0,0,9,7,1,0,
        0,0,9,10,1,0,0,0,10,1,1,0,0,0,11,12,3,4,2,0,12,13,5,10,0,0,13,16,
        1,0,0,0,14,16,5,10,0,0,15,11,1,0,0,0,15,14,1,0,0,0,16,3,1,0,0,0,
        17,32,5,9,0,0,18,32,5,8,0,0,19,20,5,3,0,0,20,21,5,2,0,0,21,32,3,
        4,2,0,22,23,5,4,0,0,23,24,5,2,0,0,24,32,3,4,2,0,25,26,5,5,0,0,26,
        27,5,2,0,0,27,28,3,4,2,0,28,29,5,6,0,0,29,32,1,0,0,0,30,32,5,1,0,
        0,31,17,1,0,0,0,31,18,1,0,0,0,31,19,1,0,0,0,31,22,1,0,0,0,31,25,
        1,0,0,0,31,30,1,0,0,0,32,5,1,0,0,0,3,9,15,31
    ]

class fourirParser ( Parser ):

    grammarFileName = "fourir.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'FIN'", "'='", "'dt'", "'n'", "'freq'", 
                     "'hz'" ]

    symbolicNames = [ "<INVALID>", "FIN", "EQ", "DT", "N", "FREQ", "HZ", 
                      "ID", "INT", "FLOAT", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2

    ruleNames =  [ "prog", "stat", "expr" ]

    EOF = Token.EOF
    FIN=1
    EQ=2
    DT=3
    N=4
    FREQ=5
    HZ=6
    ID=7
    INT=8
    FLOAT=9
    NEWLINE=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fourirParser.StatContext)
            else:
                return self.getTypedRuleContext(fourirParser.StatContext,i)


        def getRuleIndex(self):
            return fourirParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = fourirParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.stat()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1850) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fourirParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlankContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fourirParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(fourirParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlank" ):
                listener.enterBlank(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlank" ):
                listener.exitBlank(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlank" ):
                return visitor.visitBlank(self)
            else:
                return visitor.visitChildren(self)


    class PrintExprContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fourirParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(fourirParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(fourirParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintExpr" ):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = fourirParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 15
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 4, 5, 8, 9]:
                localctx = fourirParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self.expr()
                self.state = 12
                self.match(fourirParser.NEWLINE)
                pass
            elif token in [10]:
                localctx = fourirParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.match(fourirParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fourirParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DtContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fourirParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DT(self):
            return self.getToken(fourirParser.DT, 0)
        def EQ(self):
            return self.getToken(fourirParser.EQ, 0)
        def expr(self):
            return self.getTypedRuleContext(fourirParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDt" ):
                listener.enterDt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDt" ):
                listener.exitDt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDt" ):
                return visitor.visitDt(self)
            else:
                return visitor.visitChildren(self)


    class FREQContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fourirParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FREQ(self):
            return self.getToken(fourirParser.FREQ, 0)
        def EQ(self):
            return self.getToken(fourirParser.EQ, 0)
        def expr(self):
            return self.getTypedRuleContext(fourirParser.ExprContext,0)

        def HZ(self):
            return self.getToken(fourirParser.HZ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFREQ" ):
                listener.enterFREQ(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFREQ" ):
                listener.exitFREQ(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFREQ" ):
                return visitor.visitFREQ(self)
            else:
                return visitor.visitChildren(self)


    class FinContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fourirParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FIN(self):
            return self.getToken(fourirParser.FIN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFin" ):
                listener.enterFin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFin" ):
                listener.exitFin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFin" ):
                return visitor.visitFin(self)
            else:
                return visitor.visitChildren(self)


    class FloatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fourirParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(fourirParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat" ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fourirParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(fourirParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)


    class NContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fourirParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def N(self):
            return self.getToken(fourirParser.N, 0)
        def EQ(self):
            return self.getToken(fourirParser.EQ, 0)
        def expr(self):
            return self.getTypedRuleContext(fourirParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterN" ):
                listener.enterN(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitN" ):
                listener.exitN(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitN" ):
                return visitor.visitN(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = fourirParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr)
        try:
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                localctx = fourirParser.FloatContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.match(fourirParser.FLOAT)
                pass
            elif token in [8]:
                localctx = fourirParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.match(fourirParser.INT)
                pass
            elif token in [3]:
                localctx = fourirParser.DtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 19
                self.match(fourirParser.DT)
                self.state = 20
                self.match(fourirParser.EQ)
                self.state = 21
                self.expr()
                pass
            elif token in [4]:
                localctx = fourirParser.NContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 22
                self.match(fourirParser.N)
                self.state = 23
                self.match(fourirParser.EQ)
                self.state = 24
                self.expr()
                pass
            elif token in [5]:
                localctx = fourirParser.FREQContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 25
                self.match(fourirParser.FREQ)
                self.state = 26
                self.match(fourirParser.EQ)
                self.state = 27
                self.expr()
                self.state = 28
                self.match(fourirParser.HZ)
                pass
            elif token in [1]:
                localctx = fourirParser.FinContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 30
                self.match(fourirParser.FIN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





