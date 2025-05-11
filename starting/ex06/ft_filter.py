def ft_filter(function, iterable):
    """ft_filter function that filters elements from an iterable based on a function.

    Args:
        function (callable): A function that returns True or False.
        iterable (iterable): An iterable to filter.

    Returns:
        generator: A generator yielding filtered elements.
    """
    arr = []
    for item in iterable:
        if function(item):
            arr.append(item)
    return arr