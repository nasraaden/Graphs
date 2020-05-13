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

    ancestor_path = []

    # while stack is not empty:
    while stack.size() > 0:
        # pop the first vertex
        path = stack.pop()
        # if not visited
        if path[-1] not in visited:
            # compare the size of path
            if len(path) > len(ancestor_path):
                ancestor_path = path
            if len(path) == len(ancestor_path):
                if path[-1] < ancestor_path[-1]:
                    ancestor_path = path
                # mark as visted
            visited.add(path[-1])
            # push all neighbors
            for vertex in ancestors_graph.get_neighbors(path[-1]):
                new_path = list(path)
                new_path.append(vertex)
                stack.push(new_path)

    print('PATH:', ancestor_path)
    if len(ancestor_path) == 1:
        return -1

    return ancestor_path[-1]
