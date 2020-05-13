from util import Stack
from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    stack = Stack()
    stack.push([starting_node])

    ancestors_graph = Graph()

    # looping through ancestors
    for element in ancestors:
        # setting the second item to child
        child = element[1]
        # setting the first item to parent
        parent = element[0]
        # add parent and child elements to graph
        ancestors_graph.add_vertex(child)
        ancestors_graph.add_vertex(parent)
        # add edges to graph, children point to parent
        ancestors_graph.add_edge(child, parent)
    # create a set of traversed vertices
    visited = set()

    # initiate ancestor path with an empty list
    ancestor_path = []

    # while stack is not empty:
    while stack.size() > 0:
        # pop the first vertex
        path = stack.pop()
        # if not visited
        if path[-1] not in visited:
            # compare the size of current path and ancestor path
            # if current path is bigger, set ancestor path to current path
            if len(path) > len(ancestor_path):
                ancestor_path = path
            # if both paths are the same size, compare the last numbers in both
            if len(path) == len(ancestor_path):
                # if the last number in path is bigger, set ancestor path to path
                if path[-1] < ancestor_path[-1]:
                    ancestor_path = path
            # mark curernt vertex as visted
            visited.add(path[-1])
            # check all neighbors
            for vertex in ancestors_graph.get_neighbors(path[-1]):
                new_path = list(path)
                new_path.append(vertex)
                stack.push(new_path)
    # if there is only one node in ancestor path, return -1
    if len(ancestor_path) == 1:
        return -1

    # return the earliest ancestor
    return ancestor_path[-1]
