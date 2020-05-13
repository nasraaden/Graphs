from util import Stack
from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    ancestors_graph = Graph()

    # looping through ancestors
    for element in ancestors:
        # setting the first item to parent
        parent = element[0]
        # setting the second item to child
        child = element[1]
        # add parent and child elements to graph
        ancestors_graph.add_vertex(parent)
        ancestors_graph.add_vertex(child)
        # add edges to graph, children point to parent
        ancestors_graph.add_edge(parent, child)
    # create a set of traversed vertices

    # initiate ancestor path with an empty list
    ancestor_path = []
    # loop through the vertices in that ancestors graph
    for vertex in ancestors_graph.vertices:
        # call the dfs on the current vertex and the starting vertex
        current_path = ancestors_graph.dfs(vertex, starting_node)
        # if there is a current path
        if current_path is not None:
            # compare the length of the two paths
            # if it's greater, set the ancestor path to the current path
            # if it's the same, compare the parent values and return the smaller value
            if len(current_path) > len(ancestor_path):
                ancestor_path = current_path
            if len(current_path) == len(ancestor_path):
                if current_path[0] < ancestor_path[0]:
                    ancestor_path = current_path

    # if there is only one node in ancestor path, return -1
    if len(ancestor_path) == 1:
        return -1

    # return the earliest ancestor--the parent
    return ancestor_path[0]
