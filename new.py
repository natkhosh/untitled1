
class Node:
    def __init__(self, prev_node=None, next_node=None, data=None):
        """
        Конструктор узла
        :param prev_node: int or str
        :param next_node: type(self)
        :param data: type(self)
        """
        if prev_node is not None and not isinstance(prev_node, type(self)):
            raise TypeError('prev_node must be Node or None')

        if next_node is not None and not isinstance(next_node, type(self)):
            raise TypeError('next_node must be Node or None')

        self.prev_node = ref(prev_node) if prev_node is not None else None
        self.next_node = next_node
        self.data = data

    def __str__(self):
        return self.data
