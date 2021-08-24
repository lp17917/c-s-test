This project is for the City Science tech test and generates the shortest path between two point on the supplied data file

It goes about doing this by first taking the name of the file and the origin and destination
The program then reads the file and generates a list of edges and nodes, it checks whether the origin and destination
exists and then performs Dijkstra's algorithm on it.
This is done using a priority queue of the adjacent edges and uses this to then calculate the path

The tests.py and tester.dat both serve to test parts of the program such as the algorithm itself and the reading of
the file. It can be run by simply running the tests.py file with the command:

python .\tests.py

This will also give the longest time for any two nodes to have the shortest path calculated as it generates every path
possible to and from every node.

Since the program uses only built-in python functions all that is needed to build and run the project is python 3.
It can be run using the command:

python .\s_path.py <file> <origin <destination>

To use debug mode add any character after the destination node which will display things such as the current state of
the priority queue

The shortest path algorithm used within the code is Dijkstra algorithm https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm