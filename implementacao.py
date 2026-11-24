import re
from code_base_EP1 import Variable, Constant, Not, And, Or, Implies, ArgumentForm, vars

# Issue #1 — Estruturas de Dados

class SignedFormula:
    # Permite a criação de objetos que guardam um sinal e uma fórmula

    def __init__(self, sinal, formula):
        if sinal not in ("T", "F"):
            raise ValueError("O sinal deve ser T ou F em string")

        self.sinal = sinal
        self.formula = formula

    # Permite printar a fórmula e seu sinal diretamente
    def __str__(self):
        return f"{self.sinal} {self.formula}"

class Branch:
    # Cria objetos Branch que guardam as formulas do ramo atual, os indices nos quais alguma regra já foi aplicada, a sequência de expansões aplicadas, os sinais das fórmulas, e se o ramo está fechado
    def __init__(self):
        self.formulas = []
        self.expandidas = set()
        self.regras_aplicadas = []
        self.sinais = {}
        self.fechado = False

    def adicionar(self, sf):
        if self.fechado:
            return

        # Adiciona uma fórmula(e sua valoração) no ramo atual
        self.formulas.append(sf)

        # Fecha os ramos quando aplicável
        if isinstance(sf.formula, Variable):
            nome = sf.formula.name # Fórmula em formato de string

            if nome in self.sinais:
                # Se chegar em contradição, fecha o ramo
                if self.sinais[nome] != sf.sinal:
                    self.fechado = True
            else:
                self.sinais[nome] = sf.sinal
        elif isinstance(sf.formula, Constant):
            if sf.formula.value != (sf.sinal == "T"):
                self.fechado = True


    # Cria uma cópia do ramo
    def copy(self):
        copia = Branch()

        copia.formulas = self.formulas.copy()
        copia.expandidas = self.expandidas.copy()
        copia.sinais = self.sinais.copy()
        copia.regras_aplicadas = self.regras_aplicadas.copy()
        copia.fechado = self.fechado

        return copia



# Issue #2 — Regras α

# Recebe uma SignedFormula e devolve uma lista com as fórmulas expandidas
def alfa(sf) -> list[SignedFormula]:
    formulas_expandidas = []
    if isinstance(sf.formula, And) and sf.sinal == 'T':
        formulas_expandidas.extend(SignedFormula('T', filho) for filho in sf.formula.children)
    elif isinstance(sf.formula, Or) and sf.sinal == 'F':
        formulas_expandidas.extend(SignedFormula('F', filho) for filho in sf.formula.children)
    elif isinstance(sf.formula, Implies) and sf.sinal == 'F':
        formulas_expandidas.append(SignedFormula('T', sf.formula.children[0]))
        formulas_expandidas.append(SignedFormula('F', sf.formula.children[1]))
    elif isinstance(sf.formula, Not) and sf.sinal == 'T':
        formulas_expandidas.append(SignedFormula('F', sf.formula.children[0]))

    if formulas_expandidas:
        return formulas_expandidas
    else:
        raise RuntimeError("Não caracteriza uma expansão alfa")


# Issue #3 — Regras β

"""Recebe uma SignedFormula β e devolve uma lista com uma fórmula por ramo novo"""
def beta(sf: SignedFormula) -> list[SignedFormula]:
    ramos = []
    if isinstance(sf.formula, And) and sf.sinal == 'F':
        ramos.extend(SignedFormula('F', filho) for filho in sf.formula.children)
    elif isinstance(sf.formula, Or) and sf.sinal == 'T':
        ramos.extend(SignedFormula('T', filho) for filho in sf.formula.children)
    elif isinstance(sf.formula, Implies) and sf.sinal == 'T':
        ramos.append(SignedFormula('F', sf.formula.children[0]))
        ramos.append(SignedFormula('T', sf.formula.children[1]))
    elif isinstance(sf.formula, Not) and sf.sinal == 'F':
        ramos.append(SignedFormula('T', sf.formula.children[0]))

    if ramos:
        return ramos
    else:
        raise RuntimeError("Não caracteriza uma expansão beta")


# Issue #4 — Motor e estratégia

# resolve o tableaux
def solve(sequente : ArgumentForm) -> bool:
    raiz = Branch()

    for f in sequente.premises:
        raiz.adicionar(SignedFormula("T", f))
    raiz.adicionar(SignedFormula("F", sequente.conclusion))

    return expand(raiz)

# expande as fórmulas do ramo
def expand(ramo: Branch) -> bool:
    fila = [ # fila de fórmulas ainda não expandidas do ramo
        i for i in range(len(ramo.formulas))
        if i not in ramo.expandidas and
        not isinstance(ramo.formulas[i].formula , (Variable, Constant))
    ]

    # expande as fórmulas de regra alfa
    for i in fila:
        sf = ramo.formulas[i]

        if eh_alfa(sf):
            # adiciona cada novo termo ao ramo
            for newsf in alfa(sf):
                ramo.adicionar(newsf)

                # checa se o ramo fechou à cada adição de novo termo
                if ramo.fechado:
                    return True

                # adiciona à fila novas fórmulas ainda não expandidas
                if not isinstance(newsf.formula, (Variable, Constant)):
                    fila.append(len(ramo.formulas) - 1);

            ramo.expandidas.add(i)

    # fila de fórmulas de regra beta ainda não expandidas do ramo
    betas = [i for i in fila if i not in ramo.expandidas]

    # expande as fórmulas de regra beta
    if betas:
        sf = ramo.formulas[betas[0]]

        ramo.expandidas.add(betas[0])
        folhas = []

        for newsf in beta(sf):
            aux = ramo.copy()
            folhas.append(aux)
            aux.adicionar(newsf)

        return all(expand(folha) for folha in folhas) # true se todos ramos tão fechados

    return ramo.fechado

def eh_alfa(sf: SignedFormula) -> bool:
    f = sf.formula

    if sf.sinal == "T":
        return isinstance(f, (And, Not))
    else:
        return isinstance(f, (Or, Implies))

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
