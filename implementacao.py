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

def atualizar_branch(regra, branch, sf, index): 
    branch.regras_aplicadas.append((regra, sf))
    branch.expandidas.add(index)

# PRÉ: recebe branch atual e índice de branch.formulas

# CAUTION: Não verifica se o fechou o ramo ou não, só atualiza seu status
def alfa(branch, index):
    if index in branch.expandidas:
        return
    
    if index >= len(branch.formulas):
        raise ValueError ("Índice maior que o número de fórmulas")

    sf = branch.formulas[index]
    if isinstance(sf.formula, And) and sf.sinal == 'T':
        # Adiciona as subexpressões à branch
        for filho in sf.formula.children:
            sffilho = SignedFormula("T", filho)
            branch.adicionar(sffilho)
        atualizar_branch("α∧", branch, sf, index)
    elif isinstance(sf.formula, Or) and sf.sinal == 'F':
        for filho in sf.formula.children:
            sffilho = SignedFormula('F', filho)
            branch.adicionar(sffilho)
        atualizar_branch("αV", branch, sf, index)
    elif isinstance(sf.formula, Implies) and sf.sinal == 'F':
        branch.adicionar(SignedFormula('T', sf.formula.children[0]))
        branch.adicionar(SignedFormula('F', sf.formula.children[1]))
        atualizar_branch("α→", branch, sf, index)
    elif isinstance(sf.formula, Not) and sf.sinal == 'T':
        sffilho = SignedFormula('F', sf.formula.children[0])
        branch.adicionar(sffilho)
        atualizar_branch("α¬", branch, sf, index)

    else:
        raise RuntimeError("Não caracteriza uma expansão alfa")


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
