def wave_path(start_node, end_node, graph):
    path = []
    weight_node = dict()
    d = 0
    weight_node[start_node] = 0
    for_algo = list(x for x in graph[start_node])
    new_for_algo = list()
    # Расскидываем веса нодам
    # HIXME нипонятно написанная хуята, но работает
    flag = True
    while flag:
        for neighbour in for_algo:
            if neighbour not in weight_node:
                weight_node[neighbour] = d + 1
                a = list(x for x in graph[neighbour])
                new_for_algo += (a)
            if neighbour == end_node:
                flag = False
        new_for_algo, for_algo = list(), new_for_algo
        d += 1
    # Находим путь
    this_node = end_node
    while this_node != start_node:
        weight = weight_node[this_node]
        try:
            for node in graph[this_node]:
                if weight_node[node] < weight:
                    path.append(this_node)
                    this_node = node
                    break
        except KeyError as err:
            print(f"\nwtf print {err}\n")
            print(f"{this_node=} ", end='')
            print(f"{graph[this_node]=}")
            break
    path.append(start_node)
    return path


if __name__ == "__main__":
    graph = {
        1 : [2, 4],
        2 : [1, 3, 5],
        3 : [2, 6],
        4 : [1, 5, 7],
        5 : [4, 2, 6, 8],
        6 : [3, 5, 9],
        7 : [4, 8],
        8 : [7, 5, 9],
        9 : [8, 6],
    }

    print(wave_path(1, 6, graph))