def find_internal_nodes_num(tree):
    if not len(tree):
        return 0
    sorted_tree = sorted(set(tree), reverse=True)
    sorted_tree.pop()
    return len(sorted_tree)

