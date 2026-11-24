# Testes e relatório — Issue #7

## 1. Objetivo

Esta etapa tem como objetivo organizar os casos de teste da aplicação de tableaux semânticos e verificar os resultados obtidos pelo programa.

Os testes devem contemplar argumentos válidos e inválidos, considerando as fórmulas de entrada e a conclusão de cada argumento.

## 2. Casos de teste

| Teste | Premissas | Conclusão | Resultado lógico esperado |
|---|---|---|---|
| 01 — Modus ponens | `p`, `(p >> q)` | `q` | Válido |
| 02 — Argumento inválido | `p` | `q` | Inválido |
| 03 — Modus tollens | `(p >> q)`, `~q` | `~p` | Válido |
| 04 — Silogismo disjuntivo | `(p \| q)`, `~p` | `q` | Válido |
| 05 — Afirmação do consequente | `(p >> q)`, `q` | `p` | Inválido |
| 06 — Contradição nas premissas | `p`, `~p` | `q` | Válido |

## 3. Verificação dos resultados

Os resultados produzidos pela aplicação deverão ser comparados com os resultados obtidos pelo método de tabela-verdade disponibilizado no projeto.

Para os argumentos inválidos, também deverá ser verificado se o contraexemplo apresentado satisfaz todas as premissas e torna a conclusão falsa.

**Situação inicial:** os casos de teste foram organizados. A execução e a comparação dos resultados deverão ser registradas após a verificação da implementação integrada.

## 4. Dificuldades encontradas

Uma das dificuldades desta etapa é organizar os testes de modo que seja possível comparar os resultados do tableau com os resultados obtidos pelo método de tabela-verdade.

Outra dificuldade é garantir que os casos de teste estejam de acordo com a sintaxe de fórmulas utilizada pelo programa.

## 5. Considerações finais

A utilização de argumentos válidos e inválidos permite avaliar diferentes comportamentos da aplicação. A conclusão sobre o funcionamento dos testes dependerá da execução dos casos e da comparação dos resultados obtidos.
