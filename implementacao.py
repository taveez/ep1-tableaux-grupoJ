from moodle.code_base_EP1 import Variable, Constant, Not, And, Or, Implies, ArgumentForm

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

def ler_formula(texto):
    pass

def ler_sequente(caminho):
    pass

def imprimir_resultado(arg, resultado):
    pass
