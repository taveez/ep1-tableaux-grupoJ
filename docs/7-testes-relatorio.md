# Issue #7 — Testes e relatório

## 1. Objetivo

Esta etapa tem como objetivo testar o provador de tableaux semânticos para a lógica proposicional e comparar seus resultados com os resultados obtidos pelo método da tabela-verdade.

## 2. Estratégia de testes

Os testes devem contemplar argumentos válidos e inválidos, incluindo casos com premissas contraditórias e fórmulas com constantes lógicas.

Para cada argumento, o resultado produzido pelo provador deve ser comparado com o resultado do método da tabela-verdade. Nos casos de argumentos inválidos, também deve ser verificado se o contraexemplo apresentado satisfaz as premissas e falsifica a conclusão.

## 3. Casos de teste propostos

| Teste | Premissas | Conclusão | Resultado esperado |
|---|---|---|---|
| T1 — Modus ponens | `p`, `(p >> q)` | `q` | Válido |
| T2 — Modus tollens | `(p >> q)`, `~q` | `~p` | Válido |
| T3 — Silogismo disjuntivo | `(p \| q)`, `~p` | `q` | Válido |
| T4 — Tautologia | Nenhuma | `(p \| ~p)` | Válido |
| T5 — Premissa insuficiente | `p` | `q` | Inválido |
| T6 — Afirmação do consequente | `(p >> q)`, `q` | `p` | Inválido |
| T7 — Negação do antecedente | `(p >> q)`, `~p` | `~q` | Inválido |
| T8 — Premissas contraditórias | `p`, `~p` | `q` | Válido |
| T9 — Constantes lógicas | `True` | `False` | Inválido |
| T10 — Constante verdadeira | Nenhuma | `True` | Válido |
| T11 — Constante falsa | Nenhuma | `False` | Inválido |

Os resultados da tabela são expectativas lógicas. Eles ainda precisam ser confirmados pela execução dos testes na implementação do grupo.

## 4. Verificação dos resultados

A execução dos testes deverá permitir identificar divergências entre o provador de tableaux e o método da tabela-verdade.

Também deverá ser verificado se os contraexemplos encontrados para argumentos inválidos são coerentes com as premissas e a conclusão.

## 5. Dificuldades e observações

Uma dificuldade desta etapa é garantir que os testes utilizem a sintaxe aceita pela implementação e que os resultados dos dois métodos possam ser comparados corretamente.

A versão final desta seção deverá registrar as dificuldades efetivamente encontradas durante a execução dos testes e as soluções adotadas.

## 6. Situação dos testes

Os casos de teste foram propostos, mas seus resultados ainda precisam ser executados e registrados. Esta seção deverá ser atualizada após a integração com a implementação final do grupo.
