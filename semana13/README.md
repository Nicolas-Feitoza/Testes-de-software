# 🧪 Semana 13 – Integração Contínua

Nesta atividade, foi implementado um workflow de **Integração Contínua** utilizando **GitHub Actions** para executar automaticamente os testes a cada push ou pull request. O projeto mantém as classes `Aluno` e `Turma` com validação de notas, agora com testes automatizados contínuos.

## 📌 Conteúdo

- Classe `Aluno`: representa um aluno com nome, sobrenome e nota.
- Classe `Turma`: agrupa alunos e identifica maior e menor nota.
- Testes automatizados com `unittest`.
- **Workflow GitHub Actions** para CI/CD.

## 🧪 Testes

- `testMaior`: verifica se a maior nota é identificada corretamente.
- `testMenor`: verifica se a menor nota é identificada corretamente.
- `testIntervalo`: valida se as notas estão dentro do intervalo [0, 10].

## 📦 Requisitos

- Python 3.7 ou superior
- Biblioteca: `unittest` (incluída no Python)

## ▶️ Execução Local

```bash
python3 -m unittest discover -s semana13 -p "testes.py"
```

Para rodar o script principal:

```bash
python3 semana13/main.py
```

## 🚀 Integração Contínua

O workflow GitHub Actions executa automaticamente:
- ✅ Testes unitários a cada push
- ✅ Validação de código em pull requests
- ✅ Relatório de cobertura de testes

Para mais informações, consulte o arquivo `.github/workflows/`.
