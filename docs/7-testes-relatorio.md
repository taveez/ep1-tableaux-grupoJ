# Issue #7 — Testes e relatório

## 1. Objetivo

Esta etapa teve como objetivo testar o provador de tableaux semânticos para a lógica proposicional e comparar os resultados obtidos com aqueles fornecidos pelo método da tabela-verdade.

## 2. Estratégia de testes

Foram definidos 11 casos de teste para avaliar argumentos válidos e inválidos. A seleção incluiu argumentos clássicos da lógica proposicional, premissas contraditórias e fórmulas com constantes lógicas.

Para cada caso, foram comparados três elementos: o resultado do provador de tableaux, o resultado do método da tabela-verdade e o resultado esperado para o argumento.

## 3. Casos de teste e resultados

| Teste | Caso avaliado | Resultado esperado | Resultado obtido |
|---|---|---|---|
| T1 | Modus ponens | Válido | Aprovado |
| T2 | Modus tollens | Válido | Aprovado |
| T3 | Silogismo disjuntivo | Válido | Aprovado |
| T4 | Tautologia | Válido | Aprovado |
| T5 | Premissa insuficiente | Inválido | Aprovado |
| T6 | Afirmação do consequente | Inválido | Aprovado |
| T7 | Negação do antecedente | Inválido | Aprovado |
| T8 | Premissas contraditórias | Válido | Aprovado |
| T9 | Premissa verdadeira e conclusão falsa | Inválido | Aprovado |
| T10 | Conclusão verdadeira | Válido | Aprovado |
| T11 | Conclusão falsa | Inválido | Aprovado |

## 4. Resultados obtidos

A execução do arquivo `script.py` resultou na aprovação dos 11 casos de teste, correspondendo a uma taxa de aprovação de 100%.

Em todos os casos, o resultado produzido pelo provador de tableaux coincidiu com o resultado do método da tabela-verdade e com a classificação esperada.

Os testes contemplaram argumentos válidos e inválidos, além de situações com premissas contraditórias e constantes lógicas. Os resultados indicam que a implementação apresentou o comportamento esperado para os casos avaliados.

## 5. Dificuldades e observações

Durante os testes iniciais, alguns casos apresentaram o erro `'NoneType' object is not iterable'`. A investigação identificou que a função responsável pelas regras β precisava estar implementada.

Após a utilização da implementação da regra β fornecida pelo integrante responsável por essa parte do projeto, os testes foram executados novamente. Os 11 casos passaram, sem divergências entre os resultados do tableau e os da tabela-verdade.

## 6. Conclusão

Os testes realizados permitiram comparar o comportamento do provador de tableaux com o método da tabela-verdade em 11 casos selecionados. Todos os casos apresentaram os resultados esperados.

Conclui-se que a implementação passou nos testes executados. Essa conclusão se limita aos casos avaliados e não garante a ausência de erros em todas as fórmulas possíveis.

A verificação automática de contraexemplos para os argumentos inválidos deverá ser registrada separadamente caso seja implementada e executada.

## 7. Dificuldades e soluções

A principal dificuldade foi identificar a causa dos erros apresentados na primeira execução e garantir que os testes fossem realizados com a implementação integrada da regra β.

A solução consistiu em utilizar a implementação da regra β do integrante responsável e executar novamente os 11 testes, comparando os resultados do tableau com os da tabela-verdade.
