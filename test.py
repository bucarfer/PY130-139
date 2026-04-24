l1 = [None, "APPLE", 2, [1, 2], None]

list_no_none = list(filter(lambda item: item is not None, l1))
print(list_no_none)