def validate_real(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
input_str = "Hola"
if validate_real(input_str):
    print("Numero valido.")
else:
    print("Numero invalido.")

def validate_alpha(s):
    return s.isalpha()
input_str = "0"
if validate_alpha(input_str):
    print("Cadena valida.")
else:
    print("Cadena invalida.")

def validate_if_else(s):
    return "if" in s and "else" in s
input_str = "if x > 0: pass"
if validate_if_else(input_str):
    print("Sentencia valida.")
else:
    print("Sentencia invalida.")
