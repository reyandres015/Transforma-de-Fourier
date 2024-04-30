from antlr4 import *
from dist.fourirLexer import fourirLexer
from dist.fourirParser import fourirParser
from dist.fourirVisitor import fourirVisitor
import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
from scipy.fftpack import fft, fftfreq

ES = 0
N = 0
FREQ = 0
class EvalVisitor(fourirVisitor):
    def __init__(self):
        self.memory = {}

    # Métodos visit
    def visitPrintExpr(self, ctx):
        value = self.visit(ctx.expr())
        # fft_value = np.fft(value)
        # print(value)
        return value
    
    def visitDt(self, ctx):
        global ES
        ES = self.visit(ctx.expr())
        print(ES)
        
    def visitN(self, ctx):
        global N
        N = self.visit(ctx.expr())
        print(N)
        
    def visitFREQ(self, ctx):
        global FREQ
        FREQ = self.visit(ctx.expr())
        print(FREQ)

    def visitInt(self, ctx):
        return int(ctx.INT().getText())
    
    def visitFin(self, ctx):
        n = 2 ** N  # Número de intervalos
        f = FREQ  # Hz
        dt = 1 / (f * ES)  # Espaciado, 16 puntos por período

        t = np.linspace(0, (n - 1) * dt, n)  # Intervalo de tiempo en segundos
        y = np.sin(2 * pi * f * t) - 0.5 * np.sin(2 * pi * 2 * f * t)  # Señal

        Y = fft(y) / n  # Normalizada
        frq = fftfreq(n, dt)  # Recuperamos las frecuencias

        plt.plot(t, y)
        plt.plot(t, y, 'ko')
        plt.xlabel('Tiempo (s)')
        plt.ylabel('$y(t)$')
        plt.title("Signal for resolving with Fourier")
        plt.show()
        
        #TRANSFORMADA
        
        plt.vlines(frq, 0, Y.imag)  # Representamos la parte imaginaria
        plt.annotate(text=u'f = 400 Hz', xy=(400.0, -0.5), xytext=(400.0 + 1000.0, -0.5 - 0.35), arrowprops=dict(arrowstyle = "->"))
        plt.annotate(text=u'f = -400 Hz', xy=(-400.0, 0.5), xytext=(-400.0 - 2000.0, 0.5 + 0.15), arrowprops=dict(arrowstyle = "->"))
        plt.annotate(text=u'f = 800 Hz', xy=(800.0, 0.25), xytext=(800.0 + 600.0, 0.25 + 0.35), arrowprops=dict(arrowstyle = "->"))
        plt.annotate(text=u'f = -800 Hz', xy=(-800.0, -0.25), xytext=(-800.0 - 1000.0, -0.25 - 0.35), arrowprops=dict(arrowstyle = "->"))
        plt.ylim(-1, 1)
        plt.xlabel('Frecuencia (Hz)')
        plt.ylabel('Im($Y$)')
        plt.title("Signal resolved with Fourier")
        plt.show()


def main():
    input_stream = FileStream("ejemplo.txt")
    lexer = fourirLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = fourirParser(token_stream)
    tree = parser.prog()

    eval_visitor = EvalVisitor()
    eval_visitor.visit(tree)


if __name__ == '__main__':
    main()
