%{
#include <stdio.h>
#include <stdlib.h>

extern int yylex(void);
int yyerror(const char *s);

%}

%union {
    int num;
}

%token <num> NUMBER
%token <num> BOOL
%token AND OR NOT

%left OR
%left AND
%left '+' '-'
%left '*' '/'
%right NOT

%type <num> expr

%%

input:
      /* vacío */               { printf("Ingrese Expresión\n"); }
    | input expr '\n'           { printf("Expresión Válida\n\n"); }
    | input error '\n'          {
                                    yyerror("Expresión Inválida");
                                    yyerrok;
                                    printf("\n\n");
                                }
    ;

expr:
      expr '+' expr
    | expr '-' expr
    | expr '*' expr
    | expr '/' expr
    | expr AND expr
    | expr OR expr
    | NOT expr
    | '(' expr ')'
    | NUMBER
    | BOOL
    ;

%%

int yyerror(const char *s) {
    fprintf(stderr, "%s\n", s);
    return 0;
}

int main(void) {
    return yyparse();
}

