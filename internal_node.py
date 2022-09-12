def find_internal_nodes_num(tree):
    if not len(tree):
        return 0
    sorted_tree = set(tree)
    return len(sorted_tree) - 1

