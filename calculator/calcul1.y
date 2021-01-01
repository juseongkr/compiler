%{
#include	<stdio.h>
static double store [26];

%}

%union { 
	double num;
	int id;
}

%token	<num>	NUM
%token	<id>	IDENT
%token	PRINT ASSIGN SEMI NL COM
%token	'+'	'-'	'*'	'/'	'('	')'
%type	<num> expression term term1 factor factor1 exp_list estatements

%%

program
	: statements
	  { printf ("END\n"); }
statements
	: statements SEMI statement
	| statements NL statement
	| statement
statement
	: IDENT ASSIGN expression
	  { store [$<id>1-'a'] = $<num>3; }
	| PRINT '(' exp_list ')'
	| /* empty */
estatements
	: statement
	| estatements SEMI statement
exp_list
	: expression
	  { printf("%f\n", $<num>1); }
	| exp_list COM expression
	  { printf("%f\n", $<num>3); }
	| /* empty */
	  { printf("\n"); }
expression
	: expression '+' term1
	  { $$ = $1 + $3; }
	| expression '-' term1
	  { $$ = $1 - $3; }
	| term
term
	: term '*' factor1
	  { $$ = $1 * $3; }
	| term '/' factor1
	  { $$ = $1 / $3; }
	| '(' estatements COM expression ')'
	  { $$ = $4; }
	| factor
term1
	: term1 '*' factor1
	  { $$ = $1 * $3; }
	| term1 '/' factor1
	  { $$ = $1 / $3; }
	| '(' estatements COM expression ')'
	  { $$ = $4; }
	| factor1
factor
	: factor1
	| '-' factor1
	  { $$ = $2; }
factor1
	: '(' expression ')'
	  { $$ = $2; }
	| IDENT
	  { $$ = store [$<id>1-'a']; }
	| NUM

%%
void yyerror (char* s) {
	printf ("***Error:%s\n", s);
}

int main ()
{
	yyparse ();
}
