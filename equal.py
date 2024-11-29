#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Karen Otake
# SPDX-License-Identifier: BSD-3-Clause
import itertools


keyboard_input = input()
numbers = list(map(int, keyboard_input.split()))
print(numbers)

permutations = list(itertools.permutations(numbers))
print(permutations)

