import itertools


keyboard_input = input()
numbers = list(map(int, keyboard_input.split()))
print(numbers)

permutations = list(itertools.permutations(numbers))
print(permutations)

