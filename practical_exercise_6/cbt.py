def num_nodes(lst):
    if len(lst) == 1:
        return 1
    else:
        left_node = lst[0]
        right_node = lst[2]
        return num_nodes(left_node) + num_nodes(right_node) + 1
