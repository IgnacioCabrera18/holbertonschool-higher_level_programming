#!/usr/bin/python3

""""""


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        num_items = len(iterable)
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(num_items))

    def remove(self, item):
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        if index == -1:
            popped_item = self[index]
        else:
            popped_item = self[index]
        print("Popped [{}] from the list.".format(popped_item))
        return super().pop(index)
