import re
from code_base_EP1 import Variable, Constant, Not, And, Or, Implies, ArgumentForm, vars

# Issue #1 — Estruturas de Dados

class SignedFormula:
    def __init__(self, sinal, formula):
        pass

class Branch:
    def __init__(self):
        pass

    def adicionar(self, sf):
        pass

    def copy(self):
        pass


# Issue #2 — Regras α

def alfa(sf):
    pass


# Issue #3 — Regras β

def beta(sf):
    pass


# Issue #4 — Motor e estratégia

def escolher(ramo):
    pass

def provar(arg):
    pass


# Issue #5 — Contra-exemplo

def contra_exemplo(ramo, arg):
    pass


# Issue #6 — Entrada e saída

def ler_formula(formula):
    #Trata possíveis constantes na fórmula
    expr = re.sub(r"\b(True|False)\b", r"Constant(\1)", formula.strip())
    #Recolhe as letras que representam os átomos
    letras = re.findall(r"\b[a-zA-Z]\b", expr)
    #Define as variáveis a partir das constantes e das letras encontradas
    variaveis = {str(x): x for x in vars(*letras)}
    variaveis["Constant"] = Constant
    #Retorna a fórmula obtida
    return eval(expr, variaveis)


def ler_sequente(caminho):
    #Lê um sequente de um arquivo de texto e devolve um `ArgumentForm`.
    with open(caminho, "r", encoding="utf-8") as arquivo:
        linhas = [linha.strip() for linha in arquivo if linha.strip()]

    if not linhas:
        raise ValueError(f"Arquivo de sequente vazio: {caminho}")

    premissas = [ler_formula(linha) for linha in linhas[:-1]]
    conclusao = ler_formula(linhas[-1])
    return ArgumentForm(*premissas, conclusion=conclusao)


# Espera:
#   arg: ArgumentForm
#   resultado: (valido, contra_ex, regras)
#     - valido: bool (True se o sequente é válido, False caso contrário)
#     - contra_ex: dict {atomo: bool} (ou None se válido), ex.: {'p': False, 'q': True}
#     - regras: lista de tuplas [(regra, formula), ...]
def imprimir_resultado(arg, resultado):
    valido, contra_ex, regras = resultado
    premissas = ", ".join(str(p) for p in arg.premises)
    sequente = f"{premissas} ⊢ {arg.conclusion}" if premissas else f"⊢ {arg.conclusion}"

    print(f"Sequente: {sequente}")
    print(f"Resultado: {'VÁLIDO' if valido else 'INVÁLIDO'}")
    if not valido and contra_ex:
        ce = ", ".join(f"{k} = {'T' if v else 'F'}" for k, v in contra_ex.items())
        print(f"Contra-exemplo: {ce}")
    print("\nRegras aplicadas:")
    print("[" + ", ".join(f"({r}, {f})" for r, f in regras) + "]")
