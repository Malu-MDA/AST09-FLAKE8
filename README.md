# AST09 — Qualidade de Código com Flake8

![Python](https://img.shields.io/badge/Python-3.15%2B-blue?logo=python)
![Flake8](https://img.shields.io/badge/Code%20Quality-Flake8-orange)
![Pytest](https://img.shields.io/badge/Testing-Pytest%20Style-green)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-2088FF?logo=githubactions)

## Sobre o projeto

Atividade prática da disciplina de Análise e Solução de Testes (AST), com foco na implementação de ferramentas de linting para melhorar a qualidade, a legibilidade e a padronização de código Python.

O desafio consiste em analisar e refatorar um script legado de teste de login, configurar regras do Flake8 e integrar verificações específicas para testes com Pytest.

## Tecnologias utilizadas

- Python
- Flake8
- flake8-pytest-style
- Git e GitHub
- GitHub Actions

## O que foi desenvolvido

- Configuração do Flake8 com limite de 100 caracteres por linha.
- Limite de complexidade ciclomática igual a 3.
- Exclusão de diretórios de cache e ambientes virtuais.
- Refatoração de comparações booleanas e verificações de `None`.
- Tratamento de variável não utilizada com comentário `noqa` específico.
- Análise de estilo para testes automatizados com o plugin `flake8-pytest-style`.
- Integração contínua para executar as verificações automaticamente.

## Estrutura do projeto

```text
AST09-FLAKE8/
├── .github/
│   └── workflows/
│       └── flake8.yml
├── .flake8
├── test_login.py
├── explicacao.md
└── README.md
```

## Como executar localmente

### 1. Criar e ativar o ambiente virtual

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Instalar as dependências

```powershell
python -m pip install flake8 flake8-pytest-style
```

### 3. Executar a análise estática

```powershell
python -m flake8 .
```

Se nenhuma mensagem for exibida, o Flake8 não encontrou violações nas regras configuradas.

## Integração contínua

O GitHub Actions executa o Flake8 automaticamente a cada envio de código para o repositório e em pull requests direcionados à branch principal.
