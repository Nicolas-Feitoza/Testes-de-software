# 🧪 Semana 11 – Integração: Testes de Integração

Nesta atividade, foi simulada a persistência de dados em um banco MongoDB utilizando a biblioteca `mongomock` como stub. Foram desenvolvidos testes de integração para verificar o funcionamento dos métodos de salvamento das classes `Aluno` e `Turma`.

## 📌 Conteúdo

- Classe `Aluno`: representa um aluno com nome, sobrenome e nota.
- Classe `Turma`: agrupa alunos e identifica maior e menor nota.
- Classe `Conexao`: simula conexão com MongoDB.
- Testes automatizados com `unittest` e `mongomock`.

## 🧪 Testes

- `test_salvarAluno`: verifica se os dados do aluno são corretamente persistidos.
- `test_salvarTurma`: testa o salvamento da turma com todos os alunos.

## 📦 Requisitos

- Python 3.7 ou superior
- Bibliotecas:
  - `pymongo`
  - `mongomock`

## ▶️ Execução

```bash
pip install pymongo mongomock
python3 -m unittest discover -s semana11 -p "testes.py"