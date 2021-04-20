"""This is a class which represents an item object"""


class Item:
    """This is a class which represents an item object"""

    def __init__(self, sequence, size, priority):
        self.sequence = sequence
        self.size = size
        self.priority = priority

    def get_priority(self):
        """This is a method used to get an item priority"""
        return self.priority

    def add_priority(self, priority):
        """This is a method used to modify an existing priority"""
        self.priority = priority

    def get_item_string(self):
        """This is method used to display a item as one string"""
        sequence = self.sequence
        size = self.size
        priority = self.priority
        item_string = f'{sequence} {size} {priority}'
        return item_string

    def get_item_info(self):
        """This is a method used to display an item as an object"""
        info = {
            "sequence": self.sequence,
            "size": self.size,
            "priority": self.priority
        }
        return info
