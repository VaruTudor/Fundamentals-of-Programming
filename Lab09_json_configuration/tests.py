from Repository import BookRepository, ClientRepository
from domain import Client, Book
import unittest

class RepoTest(unittest.TestCase):
    
    def test_BookRepository(self):
        r = BookRepository()
        r._repo.clear()
        b1 = Book(1,'aa','bb')
        r.add(b1)
        self.assertEqual(len(r._repo),1)
        self.assertEqual(r._repo[0], b1)
        r.update(b1.id,'cc','dd')
        self.assertEqual (b1.title, 'cc')
        self.assertEqual (b1.author, 'dd')
        r.delete(b1.id)
        self.assertEqual(len(r._repo), 0)

    def test_ClientRepository(self):
        r = ClientRepository()
        r._repo.clear()
        c1 = Client(1,'aa')
        r.add(c1)
        self.assertEqual( len(r._repo), 1)
        self.assertEqual( r._repo[0], c1)
        self.assertEqual( len(r._repo), 1)
        r.update(c1.id, 'bb')
        self.assertEqual(c1.name, 'bb')
        r.delete(c1.id)
        self.assertEqual( len(r._repo), 0)

if __name__ == '__main__':
    unittest.main()