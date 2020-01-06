class Node:
    def __init__(self, parent=None, pos=None):
        self.parent = parent
        self.pos = pos
        self.f = 0  # Total cost
        self.g = 0  # Dist. between current and start
        self.h = 0  # Heuristic

    def _calculate_h(self, end_node):
        self.h = ((self.pos[0] - end_node.pos[0]) ** 2) + \
            ((self.pos[1] - end_node.pos[1]) ** 2)

    def _calculate_g(self, curr_node):
        self.g = curr_node.g + 1

    def _calculate_f(self):
        self.f = self.g + self.h

    def update_values(self, curr_node, end_node):
        self._calculate_g(curr_node)
        self._calculate_h(end_node)
        self._calculate_f()

    def __eq__(self, other):
        return self.pos == other.pos
