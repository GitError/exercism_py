def append(list1, list2):
    """Append all items from list2 to the end of list1."""
    return list1 + list2


def concat(lists):
    """Concatenate a series of lists into one flattened list."""
    result = []
    for lst in lists:
        result += lst
    return result


def filter(function, lst):
    """Filter items in the list based on the predicate function."""
    return [item for item in lst if function(item)]


def length(lst):
    """Return the total number of items in the list."""
    count = 0
    for _ in lst:
        count += 1
    return count


def map(function, lst):
    """Apply a function to each item in the list and return the results."""
    return [function(item) for item in lst]


def foldl(function, lst, initial):
    """Reduce the list from the left using the given function and initial value."""
    for item in lst:
        initial = function(initial, item)
    return initial


def foldr(function, lst, initial):
    """Reduce the list from the right using the given function and initial value."""
    for item in lst[::-1]:  # Use slicing instead of reversed() for simplicity
        initial = function(initial, item)
    return initial


def reverse(lst):
    """Return a list with all items in reversed order."""
    return lst[::-1]
