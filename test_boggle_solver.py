import unittest
import sys

sys.path.append("/home/codio/workspace/") #have to tell the unittest the PATH to find boggle_solver.py and the Boggle Class

from boggle_solver import Boggle

class TestSuite_Alg_Scalability_Cases(unittest.TestCase):
  def test_normal_case_3x3(self):
    grid = [
      ["A", "B", "C"],
      ["D", "E", "F"],
      ["G", "H", "I"]]
    dictionary = ["abc", "cfi", "beh", "adg", "aei"]
    game = Boggle(grid, dictionary)
    solution = [x.upper() for x in game.getSolution()]
    expected = ["ABC", "CFI", "BEH", "ADG", "AEI"]
    self.assertEqual(sorted(solution), sorted(expected))
  def test_4x4_grid(self):
    grid = [
      ["T","W","Y","R"],
      ["E","N","P","H"],
      ["G","Z","Qu","R"],
      ["O","N","T","A"]
    ]
    dictionary = ["art","ego","gent","get","net","new","newt"]
    game = Boggle(grid, dictionary)
    solution = [x.upper() for x in game.getSolution()]
    expected = ["ART","EGO","GENT","GET","NET","NEW","NEWT"]
    self.assertEqual(sorted(solution), sorted(expected))
  def test_5x5_grid_simple_paths(self):
    grid = [
      ["A","B","C","D","E"],
      ["F","G","H","I","J"],
      ["K","L","M","N","O"],
      ["P","Q","R","S","T"],
      ["U","V","W","X","Y"]]
    dictionary = ["abcde", "fghij", "klmno"]
    game = Boggle(grid, dictionary)
    solution = [x.upper() for x in game.getSolution()]
    expected = ["ABCDE", "FGHIJ", "KLMNO"]
    self.assertEqual(sorted(solution), sorted(expected))
    
class TestSuite_Simple_Edge_Cases(unittest.TestCase):
  #ADD MANY SIMPLE TEST CASES
  def test_1x1_grid(self):
    grid = [["A"]]
    dictionary = ["a", "aa"]
    game = Boggle(grid, dictionary)
    solution = [x.upper() for x in game.getSolution()]
    expected = []
    self.assertEqual(sorted(solution), sorted(expected))
  def test_empty_grid(self):
    grid = [[]]
    dictionary = ["HELLO"]
    game = Boggle(grid, dictionary)
    solution = game.getSolution()
    expected = []
    self.assertEqual(solution, expected)
  def test_no_matching_words(self):
    grid = [["X","Y"],["Z","W"]]
    dictionary = ["abc","def"]
    game = Boggle(grid, dictionary)
    solution = game.getSolution()
    expected = []
    self.assertEqual(solution, expected)
  def test_single_row(self):
    grid = [["A","B","C","D"]]
    dictionary = ["abc","bcd"]
    game = Boggle(grid, dictionary)
    solution = [x.upper() for x in game.getSolution()]
    expected = ["ABC","BCD"]
    self.assertEqual(sorted(solution), sorted(expected))
  def test_duplicate_letters(self):
    grid = [
      ["A","A"],
      ["A","A"]]
    dictionary = ["aaa"]
    game = Boggle(grid, dictionary)
    solution = [x.upper() for x in game.getSolution()]
    expected = ["AAA"]
    self.assertEqual(sorted(solution), sorted(expected))
  def test_short_words_ignored(self):
    grid = [
      ["A","T"],
      ["G","O"]]
    dictionary = ["at","go","ago"]
    game = Boggle(grid, dictionary)
    solution = [x.upper() for x in game.getSolution()]
    expected = ["AGO"]
    self.assertEqual(sorted(solution), sorted(expected))

class TestSuite_Complete_Coverage(unittest.TestCase):
  #ADD MANY COMPLEXED TEST CASES
  def test_diagonal_word(self):
    grid = [
      ["C","A","T"],
      ["D","O","G"],
      ["M","O","O"]]
    dictionary = ["cog","dog","cat"]
    game = Boggle(grid, dictionary)
    solution = [x.upper() for x in game.getSolution()]
    expected = ["COG","DOG","CAT"]
    self.assertEqual(sorted(solution), sorted(expected))
  def test_long_snake_path(self):
    grid = [
      ["A","B","C","D"],
      ["L","M","N","E"],
      ["K","P","O","F"],
      ["J","I","H","G"]]
    dictionary = ["abcdefghijklmnop"]
    game = Boggle(grid, dictionary)
    solution = [x.upper() for x in game.getSolution()]
    expected = ["ABCDEFGHIJKLMNOP"]
    self.assertEqual(sorted(solution), sorted(expected))
  def test_overlapping_words(self):
    grid = [
      ["C","A","R"],
      ["A","T","E"],
      ["T","E","S"]]
    dictionary = ["car","care","cart","tea"]
    game = Boggle(grid, dictionary)
    solution = [x.upper() for x in game.getSolution()]
    expected = ["CAR","CARE","CART","TEA"]
    self.assertEqual(sorted(solution), sorted(expected))
  def test_non_adjacent_letters(self):
    grid = [
      ["C","A","T"],
      ["X","X","X"],
      ["X","X","G"]]
    dictionary = ["CATG"]
    game = Boggle(grid, dictionary)
    solution = game.getSolution()
    expected = []
    self.assertEqual(solution, expected)
class TestSuite_Qu_and_St(unittest.TestCase):
  #ADD QU AND ST TEST CASES
  def test_qu_word(self):
    grid = [
      ["Qu","A","R"],
      ["X","T","E"],
      ["N","O","P"]]
    dictionary = ["qua","quart"]
    game = Boggle(grid, dictionary)
    solution = [x.upper() for x in game.getSolution()]
    expected = ["QUA","QUART"]
    self.assertEqual(sorted(solution), sorted(expected))
  def test_st_word(self):
    grid = [
      ["S","T","A"],
      ["X","R","E"],
      ["L","P","N"]]
    dictionary = ["star","stare"]
    game = Boggle(grid, dictionary)
    solution = [x.upper() for x in game.getSolution()]
    expected = ["STAR","STARE"]
    self.assertEqual(sorted(solution), sorted(expected))
  def test_q_without_u(self):
    grid = [
      ["Q","A","T"],
      ["X","X","X"],
      ["X","X","X"]]
    dictionary = ["qat"]
    game = Boggle(grid, dictionary)
    solution = game.getSolution()
    expected = ["QAT"]
    self.assertEqual(solution, expected)
if __name__ == '__main__':
	unittest.main()

