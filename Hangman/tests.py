import unittest
from repo import Repository

class Tests (unittest.TestCase):
    def test(self):
        r = Repository('2.txt')
        self.assertEqual(len(r.sentences),1)
        r.write_sentence('dogs are big')
        self.assertEqual(len(r.sentences),2)
    def test2(self):
        r = Repository('2.txt')
        c = 'cats are small'
        c += '\n'
        self.assertEqual(r.sentences[0],c)

if __name__ == '__main__':
    unittest.main()