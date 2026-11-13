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

## Requisitos

- Python 3.10+
- Código-base fornecido no Moodle (já incluído no repositório)

## Como usar

```bash
python tableaux.py entrada.txt
```

Formato do arquivo de entrada: *(a definir na issue #6)*

```
premissas: (p >> q), p
conclusao: q
```

Exemplo de saída:

```
Sequente: (p >> q), p ⊢ q
Resultado: VÁLIDO

Regras aplicadas:
[(β→, T (p >> q)), ...]
```

Para sequentes inválidos, a saída inclui o contra-exemplo, por exemplo `p = F, q = T`.

## Testes

```bash
python testes.py
```

O script roda a bateria de sequentes de `testes/` e compara o resultado do tableau com a tabela-verdade.

## Estrutura do repositório

*(ajustar conforme a implementação)*

```
.
├── tableaux.py        # script de utilização (entrada/saída)
├── estruturas.py      # SignedFormula, Branch            (#1)
├── regras.py          # regras de expansão α/β          (#2)
├── fechamento.py      # fechamento de ramo, contra-exemplo (#3)
├── estrategia.py      # escolha da próxima regra        (#4)
├── motor.py           # algoritmo principal / busca     (#5)
├── testes.py          # bateria de testes               (#7)
├── testes/            # arquivos de sequentes de teste
├── moodle/            # código fornecido pela disciplina
└── docs/              # seções do relatório
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
