def map_to_graph(level):
    graph = dict()
    node_count = 1

    # print(level)

    for x in range(len(level)):
        for y in range(len(level[0])):
            if not level[x][y].block:
                level[x][y].id = node_count
                node_count += 1

    for x in range(len(level)):
        for y in range(len(level[0])):
            if level[x][y].id != 0:
                graph[level[x][y].id] = []
                try:
                    if x - 1 >= 0:
                        if level[x - 1][y].id != 0:
                            graph[level[x][y].id].append(level[x - 1][y].id)
                except IndexError:
                    pass
                try:
                    if level[x + 1][y].id != 0:
                        graph[level[x][y].id].append(level[x + 1][y].id)
                except IndexError:
                    pass
                try:
                    if y - 1 >= 0:
                        if level[x][y - 1].id != 0:
                            graph[level[x][y].id].append(level[x][y - 1].id)
                except IndexError:
                    pass
                try:
                    if level[x][y + 1].id != 0:
                        graph[level[x][y].id].append(level[x][y + 1].id)
                except IndexError:
                    pass

    return graph


if __name__ == "__main__":
    level = [
        [1,1,1,1,1],
        [1,0,1,0,1],
        [1,0,1,1,1],
        [1,0,0,0,1],
        [1,1,1,1,1],
    ]

    graph = map_to_graph(level)

    for k in graph.keys():
        print(f"{k} is ", end='')
        for val in graph[k]:
            print(f"{val}", end=' ')
        print()

    print(level)