def soma(valor_um, valor_dois):
    try:
        return float(valor_um) + float(valor_dois)
    except ValueError:
        return "Valores inválidos, por favor utilize apenas números"
    
def sub(valor_um, valor_dois):
    try:
        return float(valor_um) - float(valor_dois)
    except ValueError:
        return "Valores inválidos, por favor utilize apenas números"

def mult(valor_um, valor_dois):
    try:
        return float(valor_um) * float(valor_dois)
    except ValueError:
        return "Valores inválidos, por favor utilize apenas números"

def div(valor_um, valor_dois):
    try:
        return float(valor_um) / float(valor_dois)
    except ValueError:
        return "Valores inválidos, por favor utilize apenas números"