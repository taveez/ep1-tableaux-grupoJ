# EP1 — Tableaux Semânticos

EP de **MAC0239 – Métodos Formais em Programação** (IME-USP, 2026).

Implementação, em Python, de um provador para o cálculo proposicional usando **tableaux semânticos**. Dado um sequente

```
A1, A2, ..., An ⊢ B
```

o programa decide se ele é **válido**. Se não for, mostra um **contra-exemplo** (valoração dos átomos). Nos dois casos, exibe a sequência de regras aplicadas `[(regra, fórmula), ...]`.

## Linguagem aceita

| Elemento   | Sintaxe                              |
|------------|--------------------------------------|
| Átomos     | uma letra: `p`, `q`, `a`, ...        |
| Negação    | `~`                                  |
| Conjunção  | `&`                                  |
| Disjunção  | `\|`                                 |
| Implicação | `>>`                                 |
| Constantes | `True`, `False`                      |

Exemplos: `(p >> q)`, `(((a | b) >> q) & (~s))`

> ⚠️ As fórmulas são lidas como expressões Python, com a precedência do Python: `p | q >> r` vira `p | (q >> r)`. **Parentize tudo.**

## Requisitos

- Python 3.10+
- Código-base da disciplina (`code_base_EP1.py`, já incluído no repositório; não alterar)

## Como usar

```bash
python script.py
```

Formato do arquivo de entrada: uma premissa por linha e a conclusão ao final

```
(p >> q)
p
q
```

Exemplo de saída:

```
Sequente: P => Q, P ⊢ Q
Resultado: VÁLIDO

Regras aplicadas:
[(β→, T P => Q), ...]
```

Para sequentes inválidos, a saída inclui o contra-exemplo, por exemplo `p = F, q = T`.


## Estrutura do repositório

*(ajustar conforme a implementação)*

```
.
├── code_base_EP1.py       # código-base da disciplina (não alterar)
├── code_base_EP1_demo.py  # exemplos de uso do código-base
├── implementacao.py       # código de implementação das funções (#1-#6)
├── script.py              # script de utilização (entrada/saída) (#7)
└── docs/                  # seções do relatório
```

## Entregáveis

- [ ] Implementação (`.py`)
- [ ] Script de utilização (`.py`)
- [ ] Relatório (`.pdf`): instruções de uso, sequentes de teste, estruturas e estratégias, dificuldades

**Prazo:** 18/11/2026

## Grupo

| Nome | NUSP | Issue |
|------|------|-------|
|      |      | #1    |
|      |      | #2    |
|      |      | #3    |
|      |      | #4    |
|      |      | #5    |
|      |      | #6    |
|      |      | #7    |

Veja [CONTRIBUTING.md](CONTRIBUTING.md) para o fluxo de trabalho do grupo.
