from implementacao import ler_formula, solve
from code_base_EP1 import ArgumentForm

SEQUENTES = [
    # Nome, premissas, conclusão, resultado esperado
    ("T1 — Modus ponens",
     ["p", "(p >> q)"], "q", True),

    ("T2 — Modus tollens",
     ["(p >> q)", "~q"], "~p", True),

    ("T3 — Silogismo disjuntivo",
     ["(p | q)", "~p"], "q", True),

    ("T4 — Tautologia",
     [], "(p | ~p)", True),

    ("T5 — Argumento inválido",
     ["p"], "q", False),

    ("T6 — Afirmação do consequente",
     ["(p >> q)", "q"], "p", False),

    ("T7 — Negação do antecedente",
     ["(p >> q)", "~p"], "~q", False),

    ("T8 — Premissas contraditórias",
     ["p", "~p"], "q", True),

    ("T9 — Constantes lógicas",
     ["True"], "False", False),

    ("T10 — Constante verdadeira",
     [], "True", True),

    ("T11 — Constante falsa",
     [], "False", False),
]


def verificar(nome, premissas, conclusao, esperado):
    formulas = [ler_formula(f) for f in premissas]
    formula_conclusao = ler_formula(conclusao)

    argumento = ArgumentForm(
        *formulas,
        conclusion=formula_conclusao
    )

    retorno = solve(argumento)
    resultado_tableau = retorno[0] if isinstance(retorno, tuple) else retorno
    resultado_tabela = argumento.is_valid_truth_table()

    passou = (
        resultado_tableau == esperado
        and resultado_tabela == esperado
        and resultado_tableau == resultado_tabela
    )

    situacao = "OK" if passou else "FALHOU"

    print(f"{nome}: {situacao}")
    print(f"  Tableau: {resultado_tableau}")
    print(f"  Tabela-verdade: {resultado_tabela}")
    print(f"  Esperado: {esperado}")

    return passou


def main():
    aprovados = 0

    for nome, premissas, conclusao, esperado in SEQUENTES:
        try:
            if verificar(nome, premissas, conclusao, esperado):
                aprovados += 1
        except Exception as erro:
            print(f"{nome}: ERRO — {erro}")

        print()

    print(f"Total: {aprovados}/{len(SEQUENTES)} testes aprovados.")


if __name__ == "__main__":
    main()
