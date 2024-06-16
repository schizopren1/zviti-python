
# Task 1: Create a generator to iterate over a list of numbers.
def number_generator(numbers):
    for num in numbers:
        yield num

numbers_gen = number_generator([1, 2, 3, 4])
print(list(numbers_gen))

# Task 2: Develop a generator that yields even numbers from a given range.
def even_number_generator(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            yield num

even_nums_gen = even_number_generator(1, 10)
print(list(even_nums_gen))

# Task 3: Implement a generator to yield odd numbers within a specified range.
def odd_number_generator(start, end):
    for num in range(start, end + 1):
        if num % 2 != 0:
            yield num

odd_nums_gen = odd_number_generator(1, 10)
print(list(odd_nums_gen))

# Task 4: Write a generator that produces Fibonacci numbers.
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibonacci_gen = fibonacci_generator()
print([next(fibonacci_gen) for _ in range(10)])

# Task 5: Create a generator that yields prime numbers up to a given limit.
def prime_number_generator(limit):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for num in range(2, limit + 1):
        if is_prime(num):
            yield num

prime_nums_gen = prime_number_generator(20)
print(list(prime_nums_gen))

# Task 6: Develop a generator to traverse a binary tree in pre-order.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pre_order_traversal(root):
    if root:
        yield root.val
        yield from pre_order_traversal(root.left)
        yield from pre_order_traversal(root.right)

tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
pre_order_gen = pre_order_traversal(tree)
print(list(pre_order_gen))

# Task 7: Implement a generator for in-order traversal of a binary tree.
def in_order_traversal(root):
    if root:
        yield from in_order_traversal(root.left)
        yield root.val
        yield from in_order_traversal(root.right)

in_order_gen = in_order_traversal(tree)
print(list(in_order_gen))

# Task 8: Write a generator for post-order traversal of a binary tree.
def post_order_traversal(root):
    if root:
        yield from post_order_traversal(root.left)
        yield from post_order_traversal(root.right)
        yield root.val

post_order_gen = post_order_traversal(tree)
print(list(post_order_gen))

# Task 9: Create a generator to traverse a graph using depth-first search (DFS).
def dfs_traversal(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            yield node
            visited.add(node)
            stack.extend(reversed(graph[node]))

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
dfs_gen = dfs_traversal(graph, 'A')
print(list(dfs_gen))

# Task 10: Develop a generator for breadth-first search (BFS) traversal of a graph.
from collections import deque

def bfs_traversal(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            yield node
            visited.add(node)
            queue.extend(graph[node])

bfs_gen = bfs_traversal(graph, 'A')
print(list(bfs_gen))

# Task 11: Implement a generator that yields the keys of a dictionary.
def dict_keys_generator(d):
    for key in d.keys():
        yield key

dict_keys_gen = dict_keys_generator({'a': 1, 'b': 2, 'c': 3})
print(list(dict_keys_gen))

# Task 12: Write a generator that yields the values of a dictionary.
def dict_values_generator(d):
    for value in d.values():
        yield value

dict_values_gen = dict_values_generator({'a': 1, 'b': 2, 'c': 3})
print(list(dict_values_gen))

# Task 13: Create a generator to iterate over key-value pairs of a dictionary.
def dict_items_generator(d):
    for item in d.items():
        yield item

dict_items_gen = dict_items_generator({'a': 1, 'b': 2, 'c': 3})
print(list(dict_items_gen))

# Task 14: Develop a generator that yields lines from a file one by one.
def file_lines_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

file_lines_gen = file_lines_generator('sample.txt')
print(list(file_lines_gen))

# Task 15: Implement a generator to iterate over words in a text file.
def file_words_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            for word in line.split():
                yield word

file_words_gen = file_words_generator('sample.txt')
print(list(file_words_gen))

# Task 16: Write a generator that yields characters from a string one by one.
def string_chars_generator(string):
    for char in string:
        yield char

string_chars_gen = string_chars_generator("Hello")
print(list(string_chars_gen))

# Task 17: Create a generator to yield unique elements from a list.
def unique_elements_generator(lst):
    seen = set()
    for item in lst:
        if item not in seen:
            yield item
            seen.add(item)

unique_elements_gen = unique_elements_generator([1, 2, 2, 3, 4, 4, 5])
print(list(unique_elements_gen))

# Task 18: Develop a generator that yields elements of a list in reverse order.
def reverse_list_generator(lst):
    for item in reversed(lst):
        yield item

reverse_list_gen = reverse_list_generator([1, 2, 3, 4, 5])
print(list(reverse_list_gen))

# Task 19: Implement a generator to yield the Cartesian product of two lists.
def cartesian_product_generator(lst1, lst2):
    for item1 in lst1:
        for item2 in lst2:
            yield (item1, item2)

cartesian_product_gen = cartesian_product_generator([1, 2], ['a', 'b'])
print(list(cartesian_product_gen))

# Task 20: Write a generator that yields permutations of a list.
from itertools import permutations

def permutations_generator(lst):
    for perm in permutations(lst):
        yield perm

permutations_gen = permutations_generator([1, 2, 3])
print(list(permutations_gen))

# Task 21: Create a generator to yield combinations of a list of elements.
from itertools import combinations

def combinations_generator(lst):
    for i in range(1, len(lst) + 1):
        for comb in combinations(lst, i):
            yield comb

combinations_gen = combinations_generator([1, 2, 3])
print(list(combinations_gen))

# Task 22: Develop a generator to iterate over a list of tuples.
def tuple_list_generator(tuples):
    for tup in tuples:
        yield tup

tuple_list_gen = tuple_list_generator([(1, 'a'), (2, 'b'), (3, 'c')])
print(list(tuple_list_gen))

# Task 23: Implement a generator that yields elements from multiple lists in parallel.
def parallel_lists_generator(*lists):
    for items in zip(*lists):
        yield items

parallel_lists_gen = parallel_lists_generator([1, 2], ['a', 'b'])
print(list(parallel_lists_gen))

# Task 24: Write a generator that yields elements from a nested list (flattening the list).
def flatten_list_generator(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_list_generator(item)
        else:
            yield item

flatten_list_gen = flatten_list_generator([[1, 2], [3, [4, 5]], 6])
print(list(flatten_list_gen))

# Task 25: Create a generator to yield elements from a nested dictionary.
def nested_dict_generator(d):
    for key, value in d.items():
        if isinstance(value, dict):
            yield from nested_dict_generator(value)
        else:
            yield (key, value)

nested_dict = {'a': {'b': 1, 'c': {'d': 2}}}
nested_dict_gen = nested_dict_generator(nested_dict)
print(list(nested_dict_gen))

# Task 26: Develop a generator to yield powers of 2 up to a given number.
def powers_of_two_generator(n):
    for i in range(n + 1):
        yield 2 ** i

powers_of_two_gen = powers_of_two_generator(10)
print(list(powers_of_two_gen))
# Task 27: Implement a generator that yields powers of a given base up to a specified limit.
def powers_of_base_generator(base, limit):
    power = 1
    while power <= limit:
        yield power
        power *= base

powers_of_base_gen = powers_of_base_generator(3, 81)
print(list(powers_of_base_gen))

# Task 28: Write a generator to yield the squares of numbers in a given range.
def squares_generator(start, end):
    for num in range(start, end + 1):
        yield num ** 2

squares_gen = squares_generator(1, 5)
print(list(squares_gen))

# Task 29: Create a generator to yield cubes of numbers in a specified range.
def cubes_generator(start, end):
    for num in range(start, end + 1):
        yield num ** 3

cubes_gen = cubes_generator(1, 5)
print(list(cubes_gen))

# Task 30: Develop a generator that yields factorials of numbers up to a given limit.
def factorials_generator(n):
    factorial = 1
    for i in range(n + 1):
        if i == 0:
            yield 1
        else:
            factorial *= i
            yield factorial

factorials_gen = factorials_generator(5)
print(list(factorials_gen))

# Task 31: Implement a generator to yield numbers in the Collatz sequence.
def collatz_sequence_generator(n):
    while n != 1:
        yield n
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    yield 1

collatz_gen = collatz_sequence_generator(10)
print(list(collatz_gen))

# Task 32: Write a generator that yields numbers in a geometric progression.
def geometric_progression_generator(initial, ratio, limit):
    current = initial
    while current <= limit:
        yield current
        current *= ratio

geometric_progression_gen = geometric_progression_generator(1, 2, 16)
print(list(geometric_progression_gen))

# Task 33: Create a generator to yield numbers in an arithmetic progression.
def arithmetic_progression_generator(initial, difference, limit):
    current = initial
    while current <= limit:
        yield current
        current += difference

arithmetic_progression_gen = arithmetic_progression_generator(1, 2, 10)
print(list(arithmetic_progression_gen))

# Task 34: Develop a generator that yields the running sum of a list of numbers.
def running_sum_generator(numbers):
    total = 0
    for num in numbers:
        total += num
        yield total

running_sum_gen = running_sum_generator([1, 2, 3, 4, 5])
print(list(running_sum_gen))

# Task 35: Implement a generator to yield the running product of a list of numbers.
def running_product_generator(numbers):
    product = 1
    for num in numbers:
        product *= num
        yield product

running_product_gen = running_product_generator([1, 2, 3, 4, 5])
print(list(running_product_gen))
