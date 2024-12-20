#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Karen Otake
# SPDX-License-Identifier: BSD-3-Clause
import itertools
import sys


numbers = list(map(int, sys.argv[1:]))

def find_equations(numbers):
    permutations = list(itertools.permutations(numbers))

    operators = ['+', '-', '*', '/']
    operator_combinations = list(itertools.product(operators, repeat=3))

    results = []

    for perm in permutations:
        for ops in operator_combinations:
            expression = f"{perm[0]} {ops[0]} {perm[1]} {ops[1]} {perm[2]} {ops[2]} {perm[3]}"
            try:
                if eval(expression) == 0:
                    results.append(expression + " = 0")
            except ZeroDivisonError:
                continue
    
    return results

if len(numbers) != 4:
    print("エラー: 四つの数字を入力してください")
    print("例: python3 equal.py 1 2 3 4")
else:
    equations = find_equations(numbers) 

    if equations:
        result = "]  [".join(equations)
        print(f"[{result}]")
    else:
        #equationsが空の時
        print("等式は見つかりませんでした")

