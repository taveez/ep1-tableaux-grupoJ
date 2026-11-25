# Relatório — EP1: Tableaux Semânticos


## 1. Instruções de utilização

### 1.1 Requisitos

- **Python 3.10+**
- Arquivo [`code_base_EP1.py`](../code_base_EP1.py) (código-base da disciplina, mantido sem alterações no mesmo diretório).

### 1.2 Linguagem aceita nas fórmulas

As fórmulas são escritas utilizando a sintaxe Python aceita pelo código-base:

| Elemento   | Sintaxe         | Exemplo           |
|------------|-----------------|-------------------|
| Átomos     | uma letra       | `p`, `q`, `a`     |
| Negação    | `~`             | `~p`              |
| Conjunção  | `&`             | `(p & q)`         |
| Disjunção  | `\|`            | `(p \| q)`        |
| Implicação | `>>`            | `(p >> q)`        |
| Constantes | `True`, `False` |                   |

> **Atenção à parentização:** como o parsing usa `eval()` do Python, os operadores seguem a precedência do Python (por exemplo, `>>` tem precedência maior que `&` e `|`, de modo que `p | q >> r` é interpretado como `p | (q >> r)`). Por isso, **parentize todas as subfórmulas compostas**, como em `(((a | b) >> q) & (~s))`.

### 1.3 Executando a bateria de testes (`script.py`)

Na raiz do repositório, execute:

```bash
python script.py
```

O script carrega os 11 sequentes definidos em `SEQUENTES`, constrói os objetos `ArgumentForm` usando `ler_formula`, executa o provador por tableaux (`solve`) e compara o resultado obtido com a tabela-verdade (`is_valid_truth_table()` de `code_base_EP1.py`) e com o valor esperado, exibindo `OK` ou `FALHOU` para cada caso e o total de acertos ao final.

### 1.4 Utilizando com arquivos de entrada (funções de E/S)

As funções de entrada e saída em `implementacao.py` também permitem ler um sequente diretamente de um arquivo `.txt` (como os arquivos em `testes/`):

- **Formato do arquivo de entrada:** uma premissa por linha, com a conclusão na última linha (caso exista apenas uma linha, o sequente não possui premissas).
Exemplo (`testes/01-modus-ponens.txt`):

```text
(p >> q)
p
q
```

- **Uso em Python:**

```python
from implementacao import ler_sequente, solve, imprimir_resultado

arg = ler_sequente("testes/01-modus-ponens.txt")
resultado = solve(arg)
imprimir_resultado(arg, resultado)
```

- **Formato esperado da saída** (para `solve` retornando `(valido, contra_ex, regras)`):

```text
Sequente: P => Q, P ⊢ Q
Resultado: VÁLIDO

Regras aplicadas:
[(β→, T P => Q)]
```

Quando o sequente é inválido e um contra-exemplo é fornecido (dicionário `{átomo: bool}`), a saída também exibe uma linha no formato `Contra-exemplo: p = F, q = T`.

---

## 2. Conjunto de sequentes utilizados como teste

### 2.1 Bateria de testes em `script.py`

A tabela abaixo apresenta os 11 sequentes testados em `script.py`, escolhidos para cobrir regras clássicas de inferência válidas, tautologias, falácias formais conhecidas, premissas contraditórias e casos extremos com constantes booleanas:

| ID  | Caso avaliado                  | Premissas         | Conclusão   | Sequente | Esperado |
|-----|--------------------------------|-------------------|-------------|----------|----------|
| T1  | Modus ponens                   | `p`, `(p >> q)`   | `q`         | `p, p => q ⊢ q` | Válido |
| T2  | Modus tollens                  | `(p >> q)`, `~q`  | `~p`        | `p => q, ¬q ⊢ ¬p` | Válido |
| T3  | Silogismo disjuntivo           | `(p \| q)`, `~p`  | `q`         | `p v q, ¬p ⊢ q` | Válido |
| T4  | Tautologia (terceiro excluído) | *(nenhuma)*       | `(p \| ~p)` | `⊢ p v ¬p` | Válido |
| T5  | Argumento inválido             | `p`               | `q`         | `p ⊢ q` | Inválido |
| T6  | Afirmação do consequente       | `(p >> q)`, `q`   | `p`         | `p => q, q ⊢ p` | Inválido |
| T7  | Negação do antecedente         | `(p >> q)`, `~p`  | `~q`        | `p => q, ¬p ⊢ ¬q` | Inválido |
| T8  | Premissas contraditórias       | `p`, `~p`         | `q`         | `p, ¬p ⊢ q` | Válido |
| T9  | Constantes lógicas             | `True`            | `False`     | `True ⊢ False` | Inválido |
| T10 | Constante verdadeira           | *(nenhuma)*       | `True`      | `⊢ True` | Válido |
| T11 | Constante falsa                | *(nenhuma)*       | `False`     | `⊢ False` | Inválido |

### 2.2 Arquivos de teste em `testes/`

Além da lista `SEQUENTES` em `script.py`, o diretório `testes/` contém sequentes em arquivo texto para validação da leitura via `ler_sequente`:

- `testes/01-modus-ponens.txt`: `(p >> q)`, `p` $\vdash$ `q` (válido)
- `testes/02-argumento-invalido.txt`: `p` $\vdash$ `q` (inválido)

### 2.3 Critério de validação

Para cada caso em `script.py`, a função `verificar` realiza uma checagem tripla:
1. compara o resultado do tableau (`solve(argumento)`) com o valor esperado;
2. compara o resultado da tabela-verdade (`argumento.is_valid_truth_table()`) com o valor esperado;
3. garante que o tableau e a tabela-verdade concordam entre si.

---

## 3. Estruturas de dados utilizadas na implementação

### 3.1 Representação de fórmulas e sequentes (`code_base_EP1.py`)

As fórmulas são representadas pela hierarquia `Proposition` (`Variable`, `Constant`, `Not`, `And`, `Or`, `Implies`), estruturadas como árvores sintáticas acessadas via `.children`. Um sequente $A_1, \dots, A_n \vdash B$ é encapsulado pela classe `ArgumentForm(*premises, conclusion=...)`, que também provê o método `is_valid_truth_table()` utilizado como oráculo nos testes.

### 3.2 Fórmulas marcadas (`SignedFormula`)

Cada fórmula dentro de um ramo do tableau é representada por um objeto `SignedFormula(sinal, formula)` em `implementacao.py`, armazenando:
- `sinal`: string `"T"` (verdadeiro) ou `"F"` (falso), validada no construtor;
- `formula`: instância de `Proposition`.

### 3.3 Ramos do tableau (`Branch`)

Cada ramo da árvore de prova é representado pela classe `Branch` em `implementacao.py`, com os seguintes atributos:
- `formulas`: lista sequencial das `SignedFormula` presentes no ramo;
- `expandidas`: conjunto (`set`) com os índices das fórmulas já expandidas, garantindo que nenhuma regra seja aplicada repetidamente sobre a mesma fórmula;
- `sinais`: dicionário `{nome_atomo: sinal}` que indexa os átomos já atribuídos no ramo;
- `fechado`: booleano que indica se o ramo foi fechado por contradição.

O método `Branch.adicionar(sf)` insere `sf` em `formulas` e faz a verificação imediata de fechamento em tempo constante:
- se `sf.formula` for um átomo (`Variable`) já presente em `sinais` com sinal oposto, marca `fechado = True`;
- se `sf.formula` for uma constante (`Constant`), fecha o ramo quando o valor booleano não corresponde ao sinal (`T False` ou `F True`).

O método `Branch.copy()` cria uma cópia independente das estruturas internas (`formulas`, `expandidas`, `sinais` e `fechado`), permitindo que expansões $\beta$ bifurquem o ramo sem interferência mútua.

---

## 4. Estratégias utilizadas na implementação

### 4.1 Estratégia de parsing e entrada/saída

- **`ler_formula(formula)`:** substitui palavras isoladas `True` e `False` por `Constant(True)` e `Constant(False)` via expressão regular (`re.sub`) antes da avaliação com `eval()`. Isso evita que constantes booleanas sejam tratadas como `bool` nativo do Python (onde `~True` resultaria em `-2`) ou gerem átomos fictícios. Em seguida, extrai os átomos de 1 letra com `re.findall(r"\b[a-zA-Z]\b", expr)` e os instancia com `vars(...)`.
- **`ler_sequente(caminho)`:** lê as linhas não vazias do arquivo, interpreta todas até a penúltima como premissas e a última como conclusão, devolvendo um `ArgumentForm`.
- **`imprimir_resultado(arg, resultado)`:** formata o sequente com `⊢`, imprime `VÁLIDO` ou `INVÁLIDO`, lista o contra-exemplo (quando inválido) e exibe a sequência de regras aplicadas.

### 4.2 Estratégia de refutação e regras de expansão ($\alpha$ e $\beta$)

- **Inicialização por refutação (`solve`):** para testar $A_1, \dots, A_n \vdash B$, o ramo raiz é inicializado com `SignedFormula("T", Ai)` para cada premissa e `SignedFormula("F", B)` para a conclusão. O sequente é válido se e somente se todos os ramos resultantes fecharem.
- **Regras $\alpha$ (`alfa`):** tratam os casos que não bifurcam (`T (C & B)`, `F (C | B)`, `F (C >> B)`, `T (~C)`), gerando todas as subfórmulas marcadas derivadas de `children` no mesmo ramo.
- **Regras $\beta$ (`beta`):** tratam os casos que exigem ramificação (`F (C & B)`, `T (C | B)`, `T (C >> B)`, `F (~C)`), produzindo um ramo filho para cada componente.

### 4.3 Estratégia de escolha de regras e busca nos ramos (`expand`)

- **Prioridade para regras $\alpha$ antes de regras $\beta$:** ao expandir um ramo, `expand` coleta os índices de fórmulas compostas não expandidas e aplica primeiro todas as regras $\alpha$ disponíveis (incluindo novas fórmulas $\alpha$ adicionadas durante o próprio laço), verificando após a expansão se o ramo fechou. Somente quando não restam regras $\alpha$ pendentes no ramo é escolhida uma fórmula $\beta$ (a primeira disponível na fila). Essa prioridade evita duplicar ramos prematuramente e reduz o tamanho da árvore de busca.
- **Busca em profundidade (DFS):** ao aplicar uma regra $\beta$, o algoritmo cria uma cópia do ramo via `ramo.copy()` para cada subfórmula gerada e chama `expand` recursivamente. Se todos os ramos filhos fecharem, o ramo atual é considerado fechado (sequente válido); caso um ramo termine saturado sem fechar (sem novas regras $\alpha$ ou $\beta$ a aplicar), ele permanece aberto (sequente inválido).
- **Extração de contra-exemplo (`contra_exemplo`):** ao atingir um ramo aberto saturado, coleta-se o conjunto de todos os átomos presentes nas fórmulas do ramo (`sf.formula.variables()`), atribui-se `True`/`False` conforme os literais registrados em `ramo.sinais` (definindo `False` para eventuais átomos livres) e valida-se com `evaluate()` que a valoração encontrada satisfaz todos os sinais esperados do ramo.

---

## 5. Dificuldades encontradas

1. **Tratamento de constantes (`True`/`False`) e precedência no parsing:** como as fórmulas são avaliadas diretamente com `eval()` em Python, foi necessário orientar a parentização explícita (devido à precedência entre `|`, `&` e `>>`) e substituir `True`/`False` por `Constant(...)` via regex para evitar que negações como `~True` fossem avaliadas como complemento bit a bit (`-2`).
2. **Suporte a conectivos $n$-ários:** no código-base `code_base_EP1.py`, operações encadeadas com `&` ou `|` armazenam mais de dois filhos em `.children`, o que exigiu adaptar as regras $\alpha$, $\beta$ e o motor de expansão para iterar sobre todos os elementos de `children` em vez de assumir apenas operadores binários.
3. **Alinhamento de interfaces entre branches paralelas:** Separação e coordenação do trabalho entre sete pessoas, como muitas partes do projeto dependiam uma das outras, houve várias iterações de correções e padronizações entre os trabalhos de cada membro do grupo.
