import unittest
import aluno as a
import turma as t

class turmaTest(unittest.TestCase):

    def setUp(self):
        self.alunos = [
            a.Aluno('Fabio', 'Teixeira', 10),
            a.Aluno('Angela', 'Teixeira', 7),
            a.Aluno('Fabiano', 'Teixeira', 8),
            a.Aluno('Melissa', 'Teixeira', 6)
        ]
        self.turmaObject = t.Turma()
        self.turmaObject.cadastrarAlunos(self.alunos)

    def tearDown(self):
        pass

    def testMaior(self):
        self.assertEqual(10, self.turmaObject.maiorNota.nota)

    def testMenor(self):
        self.assertEqual(6, self.turmaObject.menorNota.nota)

    def testIntervalo(self):
        for aluno in self.turmaObject.turma:
            self.assertTrue(0 <= aluno.nota <= 10, f'Nota fora do intervalo: {aluno.nota}')

if __name__ == "__main__":
    unittest.main()