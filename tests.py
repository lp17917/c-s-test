import unittest
import s_path


class TestMethods(unittest.TestCase):

    def test_read(self):
        # Test to check that the file is read in correctly
        tester_read = [["A", "C", 1],
                       ["A", "E", 12],
                       ["A", "F", 6],
                       ["B", "E", 2],
                       ["B", "F", 8],
                       ["C", "D", 3],
                       ["C", "E", 12],
                       ["E", "F", 6],
                       ["C", "A", 7],
                       ["E", "A", 8],
                       ["F", "D", 5],
                       ["D", "C", 3],
                       ["C", "B", 9]]
        s, f, w = s_path.file_read("tester.dat")
        for i in range(len(tester_read)):
            self.assertEqual(s[i], tester_read[i][0])
            self.assertEqual(f[i], tester_read[i][1])
            self.assertEqual(w[i], tester_read[i][2])


if __name__ == '__main__':
    unittest.main()
