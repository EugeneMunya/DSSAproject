"""This module contains sorting functions
it returns a sorting function depending on user requirement
"""

from wrapper.helpers import sort_by_sequence, sort_by_size, sort_by_priority


def get_sort_type(sort_by):
    """This is a function will return a sorting function
     depending on the user sorting requirement
     """
    sort_types = {
        "sequence": sort_by_sequence,
        "size": sort_by_size,
        "priority": sort_by_priority
    }
    if sort_by in sort_types.keys():
        return sort_types[sort_by]
    raise ValueError('Allowed to sort by sequence,size and priority only')


def asc_or_desc_order(order_type:str):
    """
    This function will used to direct the order of output
    whether is ascending or descending
    """
    if order_type == 'asc':
        return False
    if order_type == 'desc':
        return True
    raise ValueError('Wrong order type')


def file_creator(file_name, data):
    """This function will used to create order output files"""
    try:
        with open(file_name, 'w') as file:
            for item in data:
                file.write(f'{str(item.get_item_string())}\n')
    except FileNotFoundError as err:
        print(err)
