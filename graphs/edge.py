class Edge:
    """ 
    Initializes edge with source and target 
    :param source: origin point
    :param target: end pint
    """

    def __init__(self, source, target):
        self.source = source
        self.targer = target
        self.edge = (source, target)

    def get_id(self):
        """
        Returns tupla (source, target) to identify Edge
        """
        return self.edge
