# Python Data Structures

This document provides an overview of Python's fundamental data structures: lists, tuples, sets, and dictionaries. Understanding these structures is crucial for efficient data manipulation and program design.

## 1. Lists (`list`)

*   **Definition:** Ordered, mutable (changeable) sequences of items. Items can be of different data types.
*   **Syntax:** Enclosed in square brackets `[]`, items are separated by commas.
    ```python
    my_list = [1, "hello", 3.14, True]
    ```
*   **Key Characteristics:**
    *   **Ordered:** Items maintain their insertion order.
    *   **Mutable:** You can add, remove, or modify items after the list is created.
    *   **Heterogeneous:** Can hold items of different data types within the same list.
    *   **Duplicates Allowed:** Can contain multiple occurrences of the same item.
    *   **Indexed:** Items are accessed using their index (0 for the first item, 1 for the second, etc.). Negative indices can be used to access elements from the end of the list (-1 is the last element).

*   **Common Operations:**
    *   **Accessing items:** `my_list[0]` (first item), `my_list[-1]` (last item), `my_list[1:3]` (slicing)
    *   **Adding items:**
        *   `append(item)`: Adds an item to the end of the list.
        *   `insert(index, item)`: Inserts an item at a specific index.
        *   `extend(iterable)`: Appends items from another iterable (e.g., another list, tuple).
    *   **Removing items:**
        *   `remove(item)`: Removes the first occurrence of an item.
        *   `pop(index)`: Removes and returns the item at a specific index (defaults to the last item if no index is given).
        *   `del my_list[index]`: Deletes the item at a specific index (or a slice).
        *   `clear()`: Removes all items from the list.
    *   **Modifying items:** `my_list[index] = new_value`
    *   **Searching:**
        *   `index(item)`: Returns the index of the first occurrence of an item.
        *   `count(item)`: Returns the number of times an item appears in the list.
    *   **Sorting:**
        *   `sort()`: Sorts the list in place (modifies the original list).
        *   `sorted(my_list)`: Returns a new sorted list (leaves the original list unchanged).
    *   **List Comprehensions:** A concise way to create new lists based on existing iterables.
        ```python
        squares = [x**2 for x in range(10)] # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
        even_numbers = [x for x in range(20) if x % 2 == 0] # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
        ```
*   **Use Cases:**
    *   Storing collections of items that might change over time.
    *   Implementing stacks, queues, and other data structures.
    *   Working with sequences of data, such as lines in a file or records from a database.

*   **Deep Dive:**
    *   **Memory Allocation:** Lists in Python are implemented as dynamically resizable arrays. This means that the list can grow or shrink in size as needed. When you append an item to a list, Python might need to allocate a larger block of memory to accommodate the new item. This can lead to occasional performance overhead if the list needs to be resized frequently.
    *   **Time Complexity:**
        *   Accessing an element by index: O(1) (constant time)
        *   Inserting/deleting an element at the beginning of the list: O(n) (linear time, as it may require shifting other elements)
        *   Appending/popping an element from the end of the list: O(1) (amortized constant time, thanks to dynamic resizing)
        *   Searching for an element: O(n) (linear time, in the worst case)
    *   **Copying Lists:**
        *   **Shallow copy:** `new_list = my_list` creates a new reference to the *same* list object. Changes to `new_list` will also affect `my_list`, and vice versa.
        *   **Deep copy:** `new_list = my_list.copy()` or `new_list = list(my_list)` or `import copy; new_list = copy.deepcopy(my_list)` creates a completely independent copy of the list. Changes to `new_list` will not affect `my_list`. Deep copy is needed when the list contains mutable objects as elements (e.g. other lists).
    *   **List slicing advanced:** Slices can be used for more than just reading. You can also use slices to modify a list: `my_list[1:3] = [10, 20]` will replace the elements at index 1 and 2 with 10 and 20. You can also use slices to insert or delete items: `my_list[1:1] = [100, 200]` will insert 100 and 200 at index 1, and `del my_list[1:3]` will delete elements from index 1 up to (but not including) 3.

## 2. Tuples (`tuple`)

*   **Definition:** Ordered, *immutable* (unchangeable) sequences of items. Items can be of different data types.
*   **Syntax:** Enclosed in parentheses `()`, items are separated by commas.
    ```python
    my_tuple = (1, "hello", 3.14, True)
    ```
    Note: A tuple with a single item must have a trailing comma: `my_tuple = (1,)`
*   **Key Characteristics:**
    *   **Ordered:** Items maintain their insertion order.
    *   **Immutable:** Once a tuple is created, you cannot change its items.
    *   **Heterogeneous:** Can hold items of different data types within the same tuple.
    *   **Duplicates Allowed:** Can contain multiple occurrences of the same item.
    *   **Indexed:** Items are accessed using their index (0 for the first item, 1 for the second, etc.). Negative indices are allowed.

*   **Common Operations:**
    *   **Accessing items:** `my_tuple[0]`, `my_tuple[-1]`, `my_tuple[1:3]` (slicing)
    *   **Concatenation:** You can create a new tuple by concatenating existing tuples using the `+` operator.
    *   **Tuple packing and unpacking:**
        ```python
        # Packing
        my_tuple = 1, 2, 3
        # Unpacking
        a, b, c = my_tuple
        print(a, b, c) # Output: 1 2 3
        ```
    *   **Counting and finding index:** `count(item)`, `index(item)`

*   **Use Cases:**
    *   Representing fixed collections of items that should not be modified.
    *   Returning multiple values from a function.
    *   Using as keys in dictionaries (since they are immutable).
    *   Situations where data integrity is crucial.

*   **Deep Dive:**
    *   **Immutability:** The key difference from lists. Immutability means the tuple's memory location and the references to the objects it contains cannot be changed after creation.
    *   **Memory Efficiency:** Tuples are generally more memory-efficient than lists because their size is fixed. Python can pre-allocate the required memory.
    *   **Performance:** Tuples can be slightly faster than lists for operations that don't involve modification (e.g., iteration, access).
    *   **Hashing:** Tuples are hashable (meaning they can be used as keys in dictionaries or elements in sets), while lists are not. This is due to their immutability.
    *   **Tuple Comprehensions (Generator Expressions):** While you can't create a tuple using direct tuple comprehension syntax like `(x for x in range(10))`, this expression creates a *generator expression*, which is a different type of object (an iterator). You can convert it to a tuple: `my_tuple = tuple(x for x in range(10))`. Generator expressions are memory-efficient because they generate values on demand rather than storing them all in memory at once.

## 3. Sets (`set`)

*   **Definition:** An unordered collection of *unique* items.
*   **Syntax:** Enclosed in curly braces `{}`, items are separated by commas.
    ```python
    my_set = {1, 2, 3, 4, 5}
    ```
    Note: To create an empty set, use `my_set = set()`, not `my_set = {}` (which creates an empty dictionary).
*   **Key Characteristics:**
    *   **Unordered:** Items do not have a specific order. The order in which items are stored is not guaranteed and may change.
    *   **Unique:** Sets automatically remove duplicate items.
    *   **Mutable:** You can add and remove items after the set is created.
    *   **Heterogeneous:** Can hold items of different data types (as long as they are hashable).
    *   **Not Indexed:** You cannot access items using an index.

*   **Common Operations:**
    *   **Adding items:** `add(item)`, `update(iterable)` (adds multiple items)
    *   **Removing items:** `remove(item)` (raises an error if item is not found), `discard(item)` (does nothing if item is not found), `pop()` (removes and returns an arbitrary item), `clear()`
    *   **Set operations:**
        *   **Union:** `set1 | set2` or `set1.union(set2)` (all items from both sets)
        *   **Intersection:** `set1 & set2` or `set1.intersection(set2)` (items present in both sets)
        *   **Difference:** `set1 - set2` or `set1.difference(set2)` (items in set1 but not in set2)
        *   **Symmetric difference:** `set1 ^ set2` or `set1.symmetric_difference(set2)` (items in either set1 or set2, but not both)
        *   **Subset:** `set1 <= set2` or `set1.issubset(set2)` (True if all items in set1 are also in set2)
        *   **Superset:** `set1 >= set2` or `set1.issuperset(set2)` (True if all items in set2 are also in set1)
    *   **Membership testing:** `item in my_set` (efficient O(1) lookup)

*   **Use Cases:**
    *   Removing duplicate items from a collection.
    *   Performing mathematical set operations (union, intersection, difference, etc.).
    *   Efficiently checking for membership.

*   **Deep Dive:**
    *   **Hashing:** Sets are implemented using hash tables. This is why items in a set must be hashable (immutable) – to ensure consistent hashing.
    *   **Time Complexity:**
        *   Adding/removing an element: O(1) (average case, thanks to hashing)
        *   Checking for membership: O(1) (average case)
        *   Set operations (union, intersection, etc.): O(min(len(set1), len(set2))) in average case
    *   **Frozen Sets:** `frozenset` is an immutable version of a set. You can't add or remove items from a frozen set after it's created. Frozen sets are hashable and can be used as keys in dictionaries or elements in other sets.
    *   **Set Comprehensions:** Similar to list comprehensions, you can create sets using a concise syntax:
        ```python
        even_squares = {x**2 for x in range(10) if x % 2 == 0} # {0, 4, 16, 36, 64}
        ```

## 4. Dictionaries (`dict`)

*   **Definition:** An unordered (in Python versions before 3.7) collection of key-value pairs.
*   **Syntax:** Enclosed in curly braces `{}`, key-value pairs are separated by colons `:`, and pairs are separated by commas.
    ```python
    my_dict = {"name": "Alice", "age": 30, "city": "New York"}
    ```
*   **Key Characteristics:**
    *   **Unordered (until Python 3.7):** In Python versions before 3.7, dictionaries were unordered. In Python 3.7 and later, dictionaries preserve insertion order.
    *   **Mutable:** You can add, remove, or modify key-value pairs after the dictionary is created.
    *   **Keys must be unique and hashable:** Keys must be immutable objects (e.g., strings, numbers, tuples).
    *   **Values can be of any data type:** Values can be mutable or immutable.

*   **Common Operations:**
    *   **Accessing values:** `my_dict["name"]` (using the key)
    *   **Adding/modifying key-value pairs:** `my_dict["occupation"] = "Engineer"` (adds a new key-value pair or modifies an existing value)
    *   **Removing key-value pairs:** `del my_dict["age"]`, `my_dict.pop("city")` (removes and returns the value), `my_dict.clear()`
    *   **Checking for key existence:** `"name" in my_dict`
    *   **Iterating:**
        *   `for key in my_dict:` (iterates over keys)
        *   `for value in my_dict.values():` (iterates over values)
        *   `for key, value in my_dict.items():` (iterates over key-value pairs)
    *   **Dictionary views:** `my_dict.keys()`, `my_dict.values()`, `my_dict.items()` return view objects, which are dynamic "views" of the dictionary's contents. If the dictionary changes, the view objects reflect those changes.
    *   **`get(key, default)`:** Returns the value associated with the key, or a default value if the key is not found. This prevents `KeyError` exceptions.
    *   **`setdefault(key, default)`:** If the key is present in the dictionary, returns its value. If not, inserts the key with a value of default and returns default.
    *   **`update(other_dict)`:** Updates the dictionary with the key-value pairs from another dictionary or iterable of key-value pairs.

*   **Use Cases:**
    *   Representing mappings between keys and values (e.g., configuration settings, data records).
    *   Implementing caches.
    *   Counting frequencies of items.
    *   Storing structured data.

*   **Deep Dive:**
    *   **Hashing:** Dictionaries are implemented using hash tables. This allows for very fast (O(1) on average) key lookups.
    *   **Time Complexity:**
        *   Accessing, inserting, deleting a key-value pair: O(1) (average case, thanks to hashing)
        *   Iterating through keys, values, or items: O(n) (linear time)
    *   **Key Hashability:** Keys must be hashable. This means they must be immutable and have a `__hash__()` method that returns the same value for equal objects.
    *   **Dictionary Comprehensions:** Similar to list and set comprehensions, you can create dictionaries using a concise syntax:
        ```python
        squares_dict = {x: x**2 for x in range(10)}
        ```
    *   **Ordered Dictionaries (collections.OrderedDict):** Before Python 3.7, if you needed a dictionary that preserved insertion order, you could use `collections.OrderedDict` from the `collections` module. While regular dictionaries are ordered in Python 3.7+, `OrderedDict` still exists and offers some additional features, such as the ability to move an item to the beginning or end.
    *   **Merging Dictionaries:** You can merge dictionaries using the `**` operator (dictionary unpacking):
        ```python
        dict1 = {"a": 1, "b": 2}
        dict2 = {"c": 3, "d": 4}
        merged_dict = {**dict1, **dict2} # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        ```
        If there are overlapping keys, the values from the dictionary on the right will overwrite the values from the dictionary on the left.
    *   **Dictionary Views are Dynamic:** As mentioned earlier, the view objects returned by `keys()`, `values()`, and `items()` are dynamic. This means that if you add or remove items from the dictionary after creating the view, the view will reflect those changes. This can be very useful for efficiency in some scenarios, but it also means you need to be careful when iterating over a view while modifying the dictionary.
