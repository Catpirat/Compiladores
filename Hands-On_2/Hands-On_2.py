import ply.lex as lex

# Contadores para cada tipo de token
keywords = 0
identifiers = 0
numbers = 0
operators = 0
delimiters = 0

# Definimos los tokens
tokens = (
    'KEYWORD',
    'IDENTIFIER',
    'NUMBER',
    'OPERATOR',
    'DELIMITER',
)

# Palabras clave reconocidas
keywords_list = {'int', 'return', 'if', 'else', 'while', 'for'}

# Reglas de los tokens
def t_KEYWORD(t):
    r'\b(int|return|if|else|while|for)\b'
    global keywords
    keywords += 1
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in keywords_list:
        t.type = 'KEYWORD'
        global keywords
        keywords += 1
    else:
        global identifiers
        identifiers += 1
    return t

def t_NUMBER(t):
    r'\d+'
    global numbers
    numbers += 1
    return t

def t_OPERATOR(t):
    r'[+\-*/=]'
    global operators
    operators += 1
    return t

def t_DELIMITER(t):
    r'[;(){}]'
    global delimiters
    delimiters += 1
    return t

# Ignorar espacios, tabs y saltos de línea
t_ignore = ' \t\n'

# Manejo de errores
def t_error(t):
    print(f"Carácter desconocido: {t.value[0]}")
    t.lexer.skip(1)

# Creamos el lexer
lexer = lex.lex()

# Entrada de prueba
data = '''
int x = 10;
if (x > 5) { return x; }
'''

# Alimentamos el lexer
lexer.input(data)

# Procesamos todos los tokens
for tok in lexer:
    pass

# Mostramos los resultados
print(f"Palabras clave: {keywords}")
print(f"Identificadores: {identifiers}")
print(f"Números: {numbers}")
print(f"Operadores: {operators}")
print(f"Delimitadores: {delimiters}")