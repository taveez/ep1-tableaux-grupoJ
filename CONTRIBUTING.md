# Como contribuir

Guia do fluxo de trabalho do grupo. **Se você nunca usou git, comece pela seção 0** e siga na ordem. Se já usa, pule para a seção 1.

---

## 0. Primeira vez com git

### 0.1 O que é isso tudo, em 30 segundos

- **git** é um programa que guarda o histórico do código. Cada "foto" salva do código é um **commit**.
- **GitHub** é o site onde fica a cópia compartilhada do repositório (o **remote**, chamado `origin`).
- Cada pessoa trabalha numa **branch** (uma linha paralela de trabalho), para não atrapalhar ninguém. A versão oficial fica na branch `main`.
- Quando sua parte está pronta, você abre um **Pull Request (PR)** no GitHub pedindo para juntar sua branch na `main`. Alguém revisa e aprova.

O ciclo é sempre: **editar → `add` → `commit` → `push` → PR**.

### 0.2 Instalar o git

- **Linux:** `sudo apt install git`
- **macOS:** rode `git --version` no terminal. Se não estiver instalado, o sistema oferece instalar.
- **Windows:** baixe em <https://git-scm.com/download/win> e instale com as opções padrão. Use o **Git Bash** como terminal para os comandos deste guia.

Confira se instalou:

```bash
git --version
```

### 0.3 Configurar seu nome e e-mail (uma vez só)

Use o **mesmo e-mail da sua conta do GitHub**:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@exemplo.com"
git config --global init.defaultBranch main
```

### 0.4 Fazer login no GitHub pelo terminal

O GitHub **não aceita sua senha** no terminal. O jeito mais fácil é usar a ferramenta oficial `gh`:

1. Instale: <https://cli.github.com/> (no Linux: `sudo apt install gh`; no macOS: `brew install gh`).
2. Rode e siga as instruções (escolha **GitHub.com**, **HTTPS** e **Login with a web browser**):

```bash
gh auth login
```

### 0.5 Aceitar o convite e baixar o repositório

1. Aceite o convite para o repositório. Ele chega por e-mail ou aparece em <https://github.com/notifications>.
2. No terminal, vá até a pasta onde quer guardar o projeto e **clone** (baixe) o repositório:

```bash
cd ~/Documentos          # ou qualquer pasta sua
git clone https://github.com/<dono>/<nome-do-repo>.git
cd <nome-do-repo>
```

Pronto: agora você tem uma cópia local ligada ao GitHub.

### 0.6 Comandos que você vai usar todo dia

| Comando | O que faz |
|---|---|
| `git status` | Mostra em que branch você está e o que mudou. **Rode sempre que estiver em dúvida.** |
| `git pull` | Baixa as novidades do GitHub. |
| `git checkout -b nome` | Cria uma branch nova e muda para ela. |
| `git checkout nome` | Muda para uma branch que já existe. |
| `git add arquivo.py` | Marca o arquivo para entrar no próximo commit. |
| `git commit -m "mensagem"` | Salva uma "foto" das mudanças marcadas. |
| `git push` | Envia seus commits para o GitHub. |
| `git log --oneline` | Mostra o histórico de commits. |

---

## 1. Pegue uma issue

- Cada pessoa é responsável por uma issue (veja a tabela no README).
- Na página da issue, clique em **Assignees → assign yourself** antes de começar.
- Dúvidas sobre a issue vão nos comentários dela, para ficarem registradas.

## 2. Crie sua branch

**Nunca trabalhe direto na `main`.** Antes de começar:

```bash
git checkout main      # vai para a main
git pull               # atualiza com o que os outros já juntaram
git checkout -b 2-regras-expansao   # cria sua branch: <numero-da-issue>-<descricao>
```

Confira com `git status`: a primeira linha deve mostrar `On branch 2-regras-expansao`.

## 3. Trabalhe e faça commits

Edite os arquivos normalmente no seu editor. De tempos em tempos (a cada pedacinho que funciona), salve um commit:

```bash
git status                       # vê o que mudou
git add regras.py                # marca o(s) arquivo(s)
git commit -m "Adiciona regra α∧ (#2)"
```

Boas práticas:

- Commits **pequenos e frequentes** são melhores que um commit gigante no final.
- Mensagem em português, no imperativo, dizendo o que o commit faz: `Adiciona regra β→`, `Corrige fechamento com constante False`.
- Mencione a issue com `(#numero)`.
- Evite `git add .` sem olhar o `git status` antes, para não commitar arquivo que não devia (ex.: `__pycache__/`).

## 4. Envie para o GitHub

Na **primeira vez** que der push na branch:

```bash
git push -u origin 2-regras-expansao
```

Nas próximas vezes, só:

```bash
git push
```

Dê push pelo menos uma vez por dia, mesmo sem terminar: assim seu trabalho fica salvo e o grupo vê o progresso.

## 5. Abra o Pull Request

1. Entre no repositório no GitHub. Vai aparecer um botão amarelo **Compare & pull request**; clique nele. Se não aparecer, vá em **Pull requests → New pull request** e escolha sua branch.
2. Confira que está **base: `main`** ← **compare: sua-branch**.
3. Título: o que foi feito, ex.: `Regras de expansão α/β`.
4. Na descrição, escreva `Closes #2` (com o número da sua issue). Assim a issue fecha sozinha quando o PR for aceito.
5. Em **Reviewers**, escolha pelo menos uma pessoa do grupo.
6. Clique em **Create pull request**.

Se o revisor pedir mudanças: edite os arquivos, faça `add`, `commit` e `push` de novo **na mesma branch**. O PR atualiza sozinho.

**Só faça merge depois de alguém aprovar.**

## 6. Padrão de código

- Python 3.10+, seguindo a [PEP 8](https://peps.python.org/pep-0008/).
- Funções e variáveis em `snake_case`; classes em `PascalCase`.
- Toda função pública tem docstring dizendo o que recebe e o que devolve.
- **Respeite as interfaces definidas na issue #1** (`docs/interfaces.md`). Se precisar mudar uma assinatura, avise na issue #1 antes de mudar, pois outras pessoas dependem dela.
- Não altere o código do Moodle (`moodle/`). Se precisar de algo diferente, crie uma função nova no nosso código.

## 7. Testes

- Cada módulo vem com testes do que implementa.
- Antes de abrir o PR, rode tudo e confira que passa:

```bash
python testes.py
```

- Não abra PR com teste quebrando.

## 8. Revisando o PR de alguém

```bash
git fetch
git checkout <branch-da-pessoa>
python testes.py
```

- Verifique se segue as interfaces e se os testes passam.
- Comente na aba **Files changed** do PR, clicando na linha.
- Quando estiver ok: **Review changes → Approve**.
- Depois volte para sua branch: `git checkout <sua-branch>`.

## 9. Relatório

- Cada um escreve a parte do relatório sobre o seu módulo em `docs/<numero-da-issue>-<tema>.md` (ex.: `docs/4-estrategia.md`) e commita junto com o código.
- Inclua também uma ou duas linhas sobre as **dificuldades encontradas**.
- Quem estiver na issue #7 junta tudo no PDF final.

---

## Socorro! (problemas comuns)

**"Commitei na `main` sem querer"** (ainda sem push):

```bash
git checkout -b minha-branch-nova   # leva os commits para uma branch nova
git checkout main
git reset --hard origin/main        # volta a main ao estado do GitHub
git checkout minha-branch-nova
```

**`git push` recusado com "rejected" / "fetch first"**: alguém mandou coisa nova para a mesma branch. Rode `git pull` e depois `git push`.

**Minha branch ficou desatualizada em relação à `main`**:

```bash
git checkout main
git pull
git checkout <sua-branch>
git merge main
```

**Conflito ("CONFLICT ... Merge conflict in arquivo.py")**: o git não soube juntar duas mudanças na mesma linha. Abra o arquivo e procure por:

```
<<<<<<< HEAD
sua versão
=======
a outra versão
>>>>>>> main
```

Deixe o trecho do jeito certo, apague as linhas com `<<<<<<<`, `=======` e `>>>>>>>` e depois rode:

```bash
git add arquivo.py
git commit
```

Se ficar confuso, **pare e chame alguém no grupo** antes de tentar comandos aleatórios. Quase tudo no git tem conserto, mas é mais fácil consertar cedo.

**Quero descartar as mudanças de um arquivo** e voltar ao último commit:

```bash
git restore arquivo.py
```

---

## Cronograma

| Data     | Meta                                       |
|----------|--------------------------------------------|
| 13–14/11 | Interfaces da #1 publicadas (stubs)        |
| 15–16/11 | Módulos prontos, com testes                |
| 17/11    | Integração, bateria de testes, relatório   |
| 18/11    | Revisão final e **entrega**                |
