#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Karen Otake
# SPDX-License-Identifier: BSD-3-Clause
import itertools


keyboard_input = input()
numbers = list(map(int, keyboard_input.split()))
print(numbers)

permutations = list(itertools.permutations(numbers))
print(permutations)

operators = ['+', '-', '*', '/']
Four_arithmetic_operations = list(itertools.permutations(operators))
print(Four_arithmetic_operations)

expression = f"{numbers[0]} {Four_arithmetic_operations[0]} {numbers[1]} {Four_arithmetic_operations[1]}{numbers[2]} {Four_arithmetic_operations[2]} {numbers[3]}"

print(expression)
