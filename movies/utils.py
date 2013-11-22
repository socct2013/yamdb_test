""" A set of utils specific to the Movies app. Mainly implemented for algorithms for a Bacon Number."""


def bfs(graph, start, end):
    queue = list()
    queue.append([start])
    while queue:
        path = queue.pop(0)
        node = path[-1]
        # Path found
        if node == end:
            return path
        for adj in graph.get(node, []):
            new_path = list(path)
            new_path.append(adj)
            queue.append(new_path)