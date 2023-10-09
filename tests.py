import unittest
import main_program

class TestCases(unittest.TestCase):

    def test_bacon_num(self):
        input = 'Kate Winslet'
        expected = 2
        actual = main_program.bacon_degree(input)
        self.assertEqual(expected, actual)

    def test_bacon_num2(self):
        input = 'Keanu Reeves'
        expected = None
        actual = main_program.bacon_degree(input)
        self.assertEqual(expected, actual)

    def test_bacon_num3(self):
        input = 'Tinh-Phong Nguyen'
        expected = "Vertex exists but there are no connections to Kevin Bacon"
        actual = main_program.bacon_degree(input)
        self.assertEqual(expected, actual)

    def test_highest_bacon(self):
        expected = [['Glenn Close', 'Grace Kelly', 'John Gielgud'],['Glenn Close', 'John Gielgud', 'Grace Kelly'] \
                   ,['John Gielgud', 'Glenn Close', 'Grace Kelly'],['John Gielgud', 'Grace Kelly', 'Glenn Close'] \
                    ,['Grace Kelly', 'Glenn Close', 'John Gielgud'],['Grace Kelly', 'John Gielgud', 'Glenn Close']]
        actual = main_program.highest_bacon_num()
        function_works = False

        if actual in expected:
            function_works = True
        self.assertEqual(True, function_works)

    def test_actor_links1(self):
        actor1 = 'Kate Winslet'
        actor2 = 'Grace Kelly'
        expected = 3
        actual = main_program.actor_link(actor1, actor2)
        self.assertEqual(expected, actual)

    def test_actor_links2(self):
        actor1 = 'Kate Winslet'
        actor2 = 'Keanu Reeves'
        expected = None
        actual = main_program.actor_link(actor1, actor2)
        self.assertEqual(expected, actual)

    def test_actor_links3(self):
        actor1 = 'Kate Winslet'
        actor2 = 'Tinh-Phong Nguyen'
        expected = "Vertecies exists but there are no connections between them"
        actual = main_program.actor_link(actor1, actor2)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
