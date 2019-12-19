#  File: TopoSort.py

#  Description: Topographical Sorting of a Graph

#  Student's Name: Derek Wu

#  Student's UT EID: dw29924

#  Partner's Name: Victor Li

#  Partner's UT EID: vql83

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 2 December, 2019

#  Date Last Modified: 2 December, 2019


class Stack (object):
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek(self):
        return self.stack[-1]

    # check if the stack if empty
    def is_empty(self):
        return (len(self.stack) == 0)

    # return the number of elements in the stack
    def size(self):
        return (len(self.stack))


class Queue (object):
    def __init__(self):
        self.queue = []
        self.length = 0

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty(self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size(self):
        return (len(self.queue))
    # returns whether or not a item exists in in inQueue
    def inQueue(self, item):
         return item in self.queue

class Vertex (object):
    def __init__(self, label):
        self.label = label
        self.visited = False
        self.in_degree = 0


    # determine if a vertex was visited
    def was_visited(self):
        return self.visited

    # determine the label of the vertex
    def get_label(self):
        return self.label

    # string representation of the vertex
    def __str__(self):
        return str(self.label)


class Graph (object):
    def __init__(self):
        self.Vertices = []
        self.adjMat = []

    # check if a vertex is already in the graph
    def has_vertex(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (label == (self.Vertices[i]).get_label()):
                return True
        return False

    # given the label get the index of a vertex
    def get_index(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (label == (self.Vertices[i]).get_label()):
                return i
        return -1

    # add a Vertex with a given label to the graph
    def add_vertex(self, label):
        if (not self.has_vertex(label)):
            self.Vertices.append(Vertex(label))

        # add a new column in the adjacency matrix
        nVert = len(self.Vertices)
        for i in range(nVert - 1):
            (self.adjMat[i]).append(0)

        # add a new row for the new vertex
        new_row = []
        for i in range(nVert):
            new_row.append(0)
        self.adjMat.append(new_row)

    # add weighted directed edge to graph
    def add_directed_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight

    # add weighted undirected edge to graph
    def add_undirected_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # get edge weight between two vertices
    # return -1 if edge does not exist
    def get_edge_weight(self, fromVertexLabel, toVertexLabel):
        if self.has_vertex(fromVertexLabel) == False or self.has_vertex(toVertexLabel) == False:
            return -1
        else:
            fromVertexIndex = self.get_index(fromVertexLabel)
            toVertexIndex = self.get_index(toVertexLabel)
            edgeWeight = self.adjMat[fromVertexIndex][toVertexIndex]
            if edgeWeight == 0:
                return -1
            else:
                return edgeWeight

    # get a list of immediate neighbors that you can go to from a vertex
    # return a list of indices or an empty list if there are none
    def get_neighbors(self, vertexLabel):
        neighbors = []
        nVert = len(self.Vertices)
        vertexIndex = self.get_index(vertexLabel)
        for i in range(nVert):
            if self.adjMat[vertexIndex][i] != 0:
                neighbors.append(self.Vertices[i].label)
        return neighbors

    # return an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex(self, v):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                return i
        return -1

    # do a depth first search in a graph
    def dfs(self, v):
        # create the Stack
        theStack = Stack()

        # mark the vertex v as visited and push it on the Stack
        (self.Vertices[v]).visited = True
        print(self.Vertices[v])
        theStack.push(v)

        # visit all the other vertices according to depth
        while (not theStack.is_empty()):
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex(theStack.peek())
            if (u == -1):
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                print(self.Vertices[u])
                theStack.push(u)

        # the stack is empty, let us rest the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

    # determine if a directed graph has a cycle
    # this function should return a boolean and not print the result
    def has_cycle(self):
        for vertex in self.Vertices:
            theStack = Stack()
            vertex.visited = True
            theStack.push(vertex)

            while not (theStack.is_empty()):
                peekVertex = theStack.peek()
                vertexIndex = self.get_index(peekVertex)
                fromVertexLabel = peekVertex.get_label()
                toVertexLabel = vertex.get_label()
                if self.get_edge_weight(fromVertexLabel, toVertexLabel) != -1:
                    return True

                unvisitedVertexIndex = self.get_adj_unvisited_vertex(
                    vertexIndex)
                if unvisitedVertexIndex == -1:
                    unvisitedVertexIndex = theStack.pop()
                else:
                    self.Vertices[unvisitedVertexIndex].visited = True
                    theStack.push(self.Vertices[unvisitedVertexIndex])

        for vertex in self.Vertices:
            vertex.visited = False

        return False

    # # return a list of vertices after a topological sort
    # # this function should not print the list
    def toposort (self):
        output = []
        theQueue = Queue()
        self.in_degree()
        if not (self.has_cycle()):
            for i in range(len(self.Vertices)):
                temp = []
                for vertex in self.Vertices:
                    if vertex.in_degree == 0 and not theQueue.inQueue(vertex.get_label()):
                        temp.append(vertex.get_label())
                temp.sort()
                for i in temp:
                    neighbors = self.get_neighbors(i)
                    from_idx = self.get_index(i)
                    for j in neighbors:
                        self.adjMat[from_idx][self.get_index(j)] = 0
                for i in range(len(temp)):
                    theQueue.enqueue(temp[i])                
                self.in_degree()
        for i in range(theQueue.size()):
            output.append(theQueue.dequeue())
        return output

    
    # find the in degrees of all the vertices 
    def in_degree(self):
        nVert = len(self.Vertices)
        for i in range(nVert):
            count = 0
            for j in range(nVert):
                if (self.adjMat[j][i] != 0):
                    count += 1
            self.Vertices[i].in_degree = count
    
    # delete an edge from the adjacency matrix
    # delete a single edge if the graph is directed
    # delete two edges if the graph is undirected
    def delete_edge(self, fromVertexLabel, toVertexLabel):
        fromVertexIndex = self.get_index(fromVertexLabel)
        toVertexIndex = self.get_index(toVertexLabel)
        # checks and see if the graph is undirected or directed
        if self.adjMat[fromVertexIndex][toVertexIndex] == self.adjMat[toVertexIndex][fromVertexIndex]:
            self.adjMat[fromVertexIndex][toVertexIndex] = 0
            self.adjMat[toVertexIndex][fromVertexIndex] = 0
        else:
            self.adjMat[fromVertexIndex][toVertexIndex] = 0

    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def delete_vertex(self, vertexLabel):
        vertexIndex = self.get_index(vertexLabel)
        del self.Vertices[vertexIndex]
        # delete column
        for row in self.adjMat:
            del row[vertexIndex]
        # delete row
        del self.adjMat[vertexIndex]

    def print_adjMat(self, num_vertices):
        print("\nAdjacency Matrix")
        for i in range(num_vertices):
            for j in range(num_vertices):
                print(self.adjMat[i][j], end=" ")
            print()
        print()


def main():
    # create the Graph object
    theGraph = Graph()

    # oepn the file for reading
    in_file = open("./topo.txt", "r")

    # read the number of vertices
    num_vertices = int((in_file.readline()).strip())

    # read all the Vertices and add them the Graph
    for i in range(num_vertices):
        vertex = (in_file.readline()).strip()
        theGraph.add_vertex(vertex)

    # read the number of edges
    num_edges = int((in_file.readline()).strip())

    # read the edges and add them to the adjacency matrix
    for i in range(num_edges):
        edge = (in_file.readline()).strip()
        edge = edge.split()
        start = theGraph.get_index(edge[0])
        finish = theGraph.get_index(edge[1])
        weight = 1
        theGraph.add_directed_edge(start, finish, weight)

    # test if a directed graph has a cycle
    if (theGraph.has_cycle()):
        print("The Graph has a cycle.")
    else:
        print("The Graph does not have a cycle.")

    # test topological sort
    if (not theGraph.has_cycle()):
        vertex_list = theGraph.toposort()
        print ("\nList of vertices after toposort")
        print (vertex_list)


main()
