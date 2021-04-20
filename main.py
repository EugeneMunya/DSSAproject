"""This is main module used by interpreter to execute what it contains"""
from wrapper.helpers import read_items_from
from wrapper.sort_factory import get_sort_type, file_creator,asc_or_desc_order


ITEMS_FILE = 'wrapper/file_store/items.txt'
ORDER_BY_SIZE = 'wrapper/file_store/order_by_size.txt'
ORDER_BY_SEQUENCE = 'wrapper/file_store/order_by_sequence.txt'
ORDER_BY_PRIORITY = 'wrapper/file_store/order_by_priority.txt'
list_of_items = []
sorted_items = []
ITEM_PRIORITY = ''
ASC_DESC = False

if __name__ == "__main__":

    files = {
        "sequence": ORDER_BY_SEQUENCE,
        "size": ORDER_BY_SIZE,
        "priority": ORDER_BY_PRIORITY
    }

    list_of_items = read_items_from(ITEMS_FILE)
    user_input = input("Type sort type between sequence,size,priority: ").lower()
    order_type = input("Type ASC for ascending or DESC for descending: ").lower()
    try:
        ASC_DESC = asc_or_desc_order(order_type)
        sorted_items = get_sort_type(user_input)(list_of_items, ASC_DESC)
    except ValueError as err:
        print(err)
    for index, item in enumerate(sorted_items):
        if sorted_items[index].get_priority() == 2:
            ITEM_PRIORITY = 'HIGH'
        elif sorted_items[index].get_priority() == 1:
            ITEM_PRIORITY = 'MEDIUM'
        else:
            ITEM_PRIORITY = 'LOW'
        sorted_items[index].add_priority(ITEM_PRIORITY)

    if len(sorted_items) > 0:
        file = files.get(user_input)
        file_creator(file,sorted_items)
