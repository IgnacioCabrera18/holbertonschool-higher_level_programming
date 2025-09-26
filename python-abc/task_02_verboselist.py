#!/usr/bin/python3

""""""


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        num_items = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{num_items}] items.")

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        if index == -1:
            popped_item = self[index]
        else:
            popped_item = self[index]
        print(f"Popped [{popped_item}] from the list.")
        return super().pop(index)
