class Vertex:
    """
    The Vertex class represents node in graphs
    :param id: Unique identifier of vertex
    :param attr: Properties of vertex
    """

    def __init__(self, id, attributes={}):
        self.id = id
        self.attributes = attributes
