import itertools as it

a = [[1,2,3], [4,5,[444, 55],6], ["Hello", [0,23, 32]]]

new_list = []

for el in a:
    pass


def flatten_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

print(flatten_list(a))