def reduce(callback, iterable, start_value):
    accum = start_value
    for item in iterable:
        new_value = callback(item, accum)
        accum = new_value

    return accum

## Solution

my_list = [1, 2, 3, 4, 5]
sum_squares = lambda num, accum: num**2 + accum
print(reduce(sum_squares, my_list, 0))

