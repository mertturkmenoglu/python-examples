from algorithms.a_star.Node import Node


def _is_valid_move(grid, node_pos):
    row_count = len(grid)
    col_count = len(grid[0])

    # Is it on board?
    if (node_pos[0] > (row_count - 1) or
            node_pos[0] < 0 or
            node_pos[1] > (col_count - 1) or
            node_pos[1] < 0):
        return False

    # Can we move here?
    if grid[node_pos[0]][node_pos[1]] != 0:
        return False

    return True


def a_star(grid, start, end):
    start_node = Node(None, start)
    end_node = Node(None, end)

    open_list = []
    closed_list = []

    open_list.append(start_node)
    loop_count = 0
    max_loop_count = (len(grid) // 2) ** 10

    while len(open_list) > 0 and loop_count < max_loop_count:
        loop_count += 1

        # Find minimum cost node on open list
        curr_node = open_list[0]
        curr_index = 0

        for i, e in enumerate(open_list):
            if e.f < curr_node.f:
                curr_node = e
                curr_index = i

        open_list.pop(curr_index)
        closed_list.append(curr_node)

        # Find a path
        if curr_node == end_node:
            path = []
            curr = curr_node

            while curr is not None:
                path.append(curr.pos)
                curr = curr.parent

            return path[::-1]

        children = []
        moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for move in moves:
            node_pos = (curr_node.pos[0] + move[0], curr_node.pos[1] + move[1])

            if not _is_valid_move(grid, node_pos):
                continue

            new_node = Node(curr_node, node_pos)
            children.append(new_node)

        for child in children:
            if child in closed_list:
                continue

            child.update_values(curr_node, end_node)

            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            open_list.append(child)

    return None
