import queue
import unittest
import time
import dijkstra
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
        for value in test_values:
            self.assertEqual(edges[value[3]][0], value[0])
            self.assertEqual(edges[value[3]][1], value[1])
            self.assertEqual(edges[value[3]][2], value[2])

    def test_node_exists(self):
        nodes = ["A", "B", "C", "D", "E", "F", "G", "H"]
        self.assertTrue(s_path.node_exists("A", nodes))
        self.assertTrue(s_path.node_exists("C", nodes))
        self.assertTrue(s_path.node_exists("E", nodes))
        self.assertTrue(s_path.node_exists("G", nodes))
        self.assertTrue(s_path.node_exists("B", nodes))
        self.assertFalse(s_path.node_exists("T", nodes))
        self.assertFalse(s_path.node_exists("B ", nodes))
        self.assertFalse(s_path.node_exists(5, nodes))

    def test_add_nodes(self):
        expectedoutput = ["J0001", "J0101", "J0052", "X0010", "J0123", "J1010"]
        nodes = []
        s_path.add_node("J0001", nodes)
        self.assertEqual(expectedoutput[:1], nodes)
        s_path.add_node("J0101", nodes)
        self.assertEqual(expectedoutput[:2], nodes)
        s_path.add_node("J0001", nodes)
        self.assertEqual(expectedoutput[:2], nodes)
        s_path.add_node("J0052", nodes)
        self.assertEqual(expectedoutput[:3], nodes)
        s_path.add_node("J0052", nodes)
        self.assertEqual(expectedoutput[:3], nodes)
        s_path.add_node("X0010", nodes)
        s_path.add_node("J0123", nodes)
        s_path.add_node("J1010", nodes)
        self.assertEqual(expectedoutput, nodes)


class TestMethodsQueue(unittest.TestCase):

    def test_push(self):
        pqueue = dijkstra.PriorityQueue()
        element = ["A", "A", 0]
        pqueue.push(element)
        expected = [["A", "A", 0]]
        self.assertEqual(expected, pqueue.queue)
        element = ["C", "B", 4]
        pqueue.push(element)
        expected = [["A", "A", 0], ["C", "B", 4]]
        self.assertEqual(expected, pqueue.queue)
        element = ["J0001", "J0123", 9]
        pqueue.push(element)
        expected = [["A", "A", 0], ["C", "B", 4], ["J0001", "J0123", 9]]
        self.assertEqual(expected, pqueue.queue)
        element = ["", "X10", 0]
        pqueue.push(element)
        expected = [["A", "A", 0], ["C", "B", 4], ["J0001", "J0123", 9], ["", "X10", 0]]
        self.assertEqual(expected, pqueue.queue)
        element = [""]
        pqueue.push(element)
        expected = [["A", "A", 0], ["C", "B", 4], ["J0001", "J0123", 9], ["", "X10", 0], [""]]
        self.assertEqual(expected, pqueue.queue)
        dijkstra.PriorityQueue.queue = []

    def test_pop(self):
        pqueue = dijkstra.PriorityQueue()
        addingeles = [["A", "A", 0], ["C", "B", 4], ["J0001", "J0123", 9], ["", "X10", 1], ["B", "C", 5]]
        for ele in addingeles:
            pqueue.push(ele)
        expected = sorted(addingeles, key=lambda x: x[2])
        for ele in expected:
            self.assertEqual(ele, dijkstra.PriorityQueue.pop(pqueue))
        pqueue = None

    def test_pop_bug(self):
        pqueue = dijkstra.PriorityQueue()
        addingeles = [["A", "A", 8], ["C", "B", 4], ["J0001", "J0123", 9], ["", "X10", 1], ["B", "C", 5]]
        for ele in addingeles:
            pqueue.push(ele)
        expected = sorted(addingeles, key=lambda x: x[2])
        for ele in expected:
            self.assertEqual(ele, dijkstra.PriorityQueue.pop(pqueue))
        dijkstra.PriorityQueue.queue = []

    def test_update(self):
        pqueue = dijkstra.PriorityQueue()
        addingeles = [["A", "A", 0], ["C", "B", 4], ["J0001", "J0123", 9], ["", "X10", 1], ["B", "C", 5]]
        for ele in addingeles:
            pqueue.push(ele)
        pqueue.update_priority(0, ["A", "B", 5])
        self.assertEqual(addingeles, pqueue.queue)
        expected = [["A", "A", 0], ["C", "B", 4], ["J0001", "J0100", 3], ["", "X10", 1], ["B", "C", 5]]
        pqueue.update_priority(2, ["J0001", "J0100", 3])
        self.assertEqual(expected, pqueue.queue)
        expected = [["A", "A", 0], ["C", "B", 4], ["J0001", "J0100", 3], ["", "X10", 1], ["A", "C", 2]]
        pqueue.update_priority(4, ["A", "C", 2])
        self.assertEqual(expected, pqueue.queue)
        pqueue = None

    def test_isempty(self):
        pqueue = dijkstra.PriorityQueue()
        print(pqueue.queue)
        self.assertTrue(pqueue.isempty())
        pqueue.push(["A", "A", 0])
        self.assertFalse(pqueue.isempty())
        dijkstra.PriorityQueue.queue = []

    def test_find(self):
        pqueue = dijkstra.PriorityQueue()
        addingeles = [["A", "A", 0], ["C", "B", 4], ["J0001", "J0123", 9], ["", "X10", 1], ["B", "C", 5]]
        for ele in addingeles:
            pqueue.push(ele)
        self.assertEqual(pqueue.find(["A", "A", 0]), 0)
        self.assertEqual(pqueue.find(["B", "C", 5]), 4)
        self.assertEqual(pqueue.find(["J0001", "J0123", 9]), 2)
        self.assertEqual(pqueue.find(["", "X10", 1]), 3)
        self.assertEqual(pqueue.find(["C", "B", 4]), 1)
        dijkstra.PriorityQueue.queue = []


class TestMethodsDijkstra(unittest.TestCase):

    def test_dijkstra_length(self):
        # Use the test file to generate all the lengths and check them
        nodes = ["A", "B", "C", "D", "E", "F"]

        lengths = [[0, 10, 1, 4, 12, 6],
                   [10, 0, 11, 13, 2, 8],
                   [7, 9, 0, 3, 11, 13],
                   [10, 12, 3, 0, 14, 16],
                   [8, 18, 9, 11, 0, 6],
                   [15, 17, 8, 5, 19, 0]]

        for i in range(len(nodes)):
            for j in range(len(nodes)):
                edges = s_path.file_read("tester.dat")
                dijkstra.PriorityQueue.queue = []
                path, length = dijkstra.dijkstra(edges, nodes[i], nodes[j], False)
                self.assertEqual(lengths[i][j], length)

    def test_dijkstra_path(self):
        # Use the test file to generate all the paths and check them

        paths = [[["A"], ["A", "C", "B"], ["A", "C"], ["A", "C", "D"], ["A", "E"], ["A", "F"]],
                 [["B", "E", "A"], ["B"], ["B", "E", "A", "C"], ["B", "F", "D"], ["B", "E"], ["B", "F"]],
                 [["C", "A"], ["C", "B"], ["C"], ["C", "D"], ["C", "B", "E"], ["C", "A", "F"]],
                 [["D", "C", "A"], ["D", "C", "B"], ["D", "C"], ["D"], ["D", "C", "B", "E"], ["D", "C", "A", "F"]],
                 [["E", "A"], ["E", "A", "C", "B"], ["E", "A", "C"], ["E", "F", "D"], ["E"], ["E", "F"]],
                 [["F", "D", "C", "A"], ["F", "D", "C", "B"], ["F", "D", "C"], ["F", "D"], ["F", "D", "C", "B", "E"], ["F"]]
                 ]
        nodes = ["A", "B", "C", "D", "E", "F"]
        for i in range(len(nodes)):
            for j in range(len(nodes)):
                dijkstra.PriorityQueue.queue = []
                edges = s_path.file_read("tester.dat")
                path, length = dijkstra.dijkstra(edges, nodes[i], nodes[j], False)
                self.assertEqual(paths[i][j], path)


class TestMethodsTiming(unittest.TestCase):

    def test_timing(self):
        # Write test for timing all nodes in under 1 second
        edges = s_path.file_read("exmouth-links.dat")
        nodes = []
        for edge in edges:
            s_path.add_node(edge[0], nodes)
            s_path.add_node(edge[1], nodes)
        maxtime = 0

        for i in range(len(nodes)):
            for j in range(len(nodes)):
                dijkstra.PriorityQueue.queue = []
                t0 = time.time()
                edges = s_path.file_read("exmouth-links.dat")
                path, length = dijkstra.dijkstra(edges, nodes[i], nodes[j], False)
                t1 = time.time()
                total = t1 - t0
                if total > maxtime:
                    maxtime = total

        print(maxtime)


if __name__ == '__main__':
    unittest.main()
