
grammar fourir;

prog:   stat+ ;

stat:   expr NEWLINE                # printExpr
    |   NEWLINE                     # blank
    ;

expr:   FLOAT                       # float
    |   INT                         # int
    |   DT EQ expr                  # dt
    |   N EQ expr                   # N
    |   FREQ EQ expr HZ             # FREQ
    |   FIN                         # Fin
    ;

FIN : 'FIN';
EQ  :   '=' ;
DT :   'dt' ;
N :   'n' ;
FREQ :   'freq' ;
HZ :   'hz' ;
ID  :   [a-zA-Z]+ ;      // Coincide con identificadores
INT :   [0-9]+ ;         // Coincide con enteros
FLOAT:  [0-9]+ '.' [0-9]+ ;    // Coincide con flotantes
NEWLINE:'\r'? '\n' ;     // Retorna nuevas líneas al analizador (es una señal de fin de declaración)
WS  :   [ \t]+ -> skip ; // Ignora los espacios en blanco
