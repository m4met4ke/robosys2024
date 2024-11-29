#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Karen Otake
# SPDX-License-Identifier: BSD-3-Clause
import itertools


keyboard_input = input()
numbers = list(map(int, keyboard_input.split()))

permutations = list(itertools.permutations(numbers))

operators = ['+', '-', '*', '/']
operator_combinations = list(itertools.permutations(operators))

results = []

for perm in permutations:
    for ops in operator_combinations:
        expression = f"{perm[0]} {ops[0]} {perm[1]} {ops[1]} {perm[2]} {ops[2]} {perm[3]}"
        try:
            if eval(expression) == 0:
                results.append(expression + " = 0")
        except ZeroDivisonError:
            continue

for eq in results:
    print(eq)

