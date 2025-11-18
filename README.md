# 📘 Testes de Software – Atividades Semanais

Este repositório reúne as atividades desenvolvidas nas semanas 09, 10, 11 e 13 da disciplina de Introdução a Testes de Software. Cada pasta contém os arquivos de código, testes automatizados e instruções específicas.

## 📚 Atividades

- [Semana 09 – Testes com turma de alunos](semana09/README.md)  
  Implementação de classes `Aluno` e `Turma`, com testes para identificar maior e menor nota, além de validação de intervalo.

- [Semana 10 – Conversão de números romanos](semana10/README.md)  
  Função `converte()` para transformar números romanos em inteiros, com testes unitários e correção de erro lógico.

- [Semana 11 - Integração: Testes de Integração](semana11/README.md)
  Simulação de persistência de dados e MongoDB utilizando mongomock como stub. Testes de integração para as classes Aluno e Turma.

- [Semana 13 – Integração Contínua](semana13/README.md)
  Implementação de workflow **GitHub Actions** para CI/CD, com execução automática de testes unitários a cada push e pull request.

## 🛠️ Requisitos

- Python 3.7 ou superior
- Bibliotecas externas:
  * pymongo
  * mongomock
- Pode ser executado diretamente no GitHub Codespaces

## 🚀 Como usar no GitHub Codespaces

1. Clique em **Code** → **Open with Codespaces** → **New codespace**
2. Navegue até a pasta da semana desejada
3. Execute `main.py` para ver o funcionamento
4. Execute `testes.py` para rodar os testes automatizados

## 🔄 Integração Contínua (Semana 13)

Os testes são executados automaticamente via GitHub Actions a cada push ou pull request. O workflow valida toda a suite de testes do projeto.

---