
from domain import Board
from computerAlgorithms import AlgorithmSimple
import unittest

class BoardTests(unittest.TestCase):
    def test_board_create(self):
        board = Board()
        self.assertEqual(board.win(),None)
        self.assertEqual(board.tie(),False)
        for row in range(15):
            for col in range(15):
                self.assertEqual(board.get_square(row,col),0)

    def test_board_move(self):
        board = Board()
        board.move(1,1,'b')
        self.assertEqual(board.get_square(1,1),1)

    def test_board_win(self):
        board = Board()
        board.move(1,1,'b')
        board.move(1,5,'b')
        board.move(1,4,'b')
        board.move(1,3,'b')
        board.move(1,2,'b')
        self.assertEqual(board.win(),5)

class AlgorithmSimpleTest(unittest.TestCase):
    def test_algorithm(self):
        board = Board()
        algortihm = AlgorithmSimple()
        self.assertEqual(algortihm.next_move(board),(0,0))
        board.move(0,0,'b')
        self.assertEqual(algortihm.next_move(board),(0,1))
        board.move(0,1,'b')
        self.assertEqual(algortihm.next_move(board),(0,2))
        
if __name__ == '__main__':
    unittest.main()