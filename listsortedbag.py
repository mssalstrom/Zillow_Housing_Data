"""
File: listbag.py
Author: Man-Chi Leung
"""

from listbag import ListBag


class ListSortedBag(ListBag):
    """An list-based bag implementation."""

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        ListBag.__init__(self, sourceCollection)

    def __contains__(self, item):
        """Returns True if item is in self, or False otherwise.
        Use binary search"""
        left = 0
        right = len(self) - 1
        visited_items = list()
        while left <= right:
            mid_point = (left + right) // 2
            visited_items.append(self.items[mid_point])
            if self.items[mid_point] == item:
                # print(f'Items visited: {visited_items}')
                return True
            elif self.items[mid_point] > item:
                right = mid_point - 1
            else:
                left = mid_point + 1
        # print(f'Items visited: {visited_items}')
        return False

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        new_bag = ListSortedBag(self)
        for item in other:
            new_bag.add(item)
        return new_bag

    def add(self, item):
        """Adds item to self."""
        if self.isEmpty():
            # print(f"Item added: {item} ", end='')
            self.items.append(item)
            # print("Item added at front")
        elif item >= self.items[len(self) - 1]:
            # print(f"Item added: {item} ", end='')
            self.items.append(item)
            # print("Item added at back end")
        else:
            # print(f"Item added: {item} ", end='')
            target_index = 0
            visited_items = list()
            while item > self.items[target_index]:
                visited_items.append(self.items[target_index])
                target_index += 1
            if item < self.items[target_index]:
                visited_items.append(self.items[target_index])
            self.items.insert(target_index, item)
            # print(f'Items visited: {visited_items}')

    def remove(self, item):
        """Removes item from self."""
        if item in self.items:
            target_index = 0
            visited_items = list()
            while item >= self.items[target_index]:
                visited_items.append(self.items[target_index])
                target_index += 1
            # print(f'Items visited: {visited_items}')
            self.items.remove(item)
