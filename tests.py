import unittest
import s_path


class TestMethodsReading(unittest.TestCase):

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
        edges = s_path.file_read("tester.dat")
        # Tests that each value in the table is the expected value for the test file
        for i in range(len(tester_read)):
            self.assertEqual(edges[i][0], tester_read[i][0])
            self.assertEqual(edges[i][1], tester_read[i][1])
            self.assertEqual(edges[i][2], tester_read[i][2])

    def test_read_act(self):

        edges = s_path.file_read("exmouth-links.dat")
        # A table with some values of the links file and which line they occur on
        test_values = [["J1001", "J1002", 72, 0],
                       ["J1020", "J1017", 430, 55],
                       ["X1058", "J1040", 2049, 176],
                       ["J1057", "J1055", 1245, 153],
                       ["J1009", "J1030", 118, 25],
                       ["J1016", "J1014", 2146, 44],
                       ["J1034", "J1033", 159, 88],
                       ["J1047", "J1049", 431, 125],
                       ["J1054", "J1051", 684, 142],
                       ["J1060", "J1010", 142, 158],
                       ["J1041", "J1040", 1229, 105]]

        # Tests that each value in the table is the expected value for the exmouth-links file
        for i in range(len(test_values)):
            self.assertEqual(edges[test_values[i][3]][0], test_values[i][0])
            self.assertEqual(edges[test_values[i][3]][1], test_values[i][1])
            self.assertEqual(edges[test_values[i][3]][2], test_values[i][2])


if __name__ == '__main__':
    unittest.main()
