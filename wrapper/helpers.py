"""This is helper module contains all the helper functions"""

from wrapper.item import Item


def read_items_from(file: str):
    """This function is used to read data from a file
    and store the data in memory
    """
    list_of_items = []
    item_priority = 0
    try:
        with open(file, 'r') as items:
            for item in items:
                item_info = item.split(' ')
                if item_info[2] == 'HIGH':
                    item_priority = 2
                elif item_info[2] == 'MEDIUM':
                    item_priority = 1
                new_item = Item(item_info[0], item_info[1], item_priority)
                list_of_items.append(new_item)
    except FileNotFoundError as err:
        print(err)
    return list_of_items


def sort_by_sequence(unsorted_list: list, order_type:bool):
    """This is a function will order a list of items by sequence"""
    new_list = sorted(unsorted_list, key=lambda item: item.sequence, reverse=order_type)
    return new_list


def sort_by_size(unsorted_list: list,order_type:bool):
    """This is a function will order a list of items by size"""
    new_list = sorted(unsorted_list, key=lambda item: item.size, reverse=order_type)
    return new_list


def sort_by_priority(unsorted_list: list,order_type:bool):
    """This is a function will order a list of items by priority"""
    new_list = sorted(unsorted_list, key=lambda item: item.priority, reverse=order_type)
    return new_list
