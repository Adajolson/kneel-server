class Order():
    """Class that defines the properties for a order object"""
    def __init__(self, id, metalId, sizeId, styleId, typeId, timestamp):
        self.id = id
        self.metalId = metalId
        self.sizeId = sizeId
        self.styleId = styleId
        self.typeId = typeId
        self.timestamp = timestamp
        