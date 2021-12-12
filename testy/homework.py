import argparse
import json
import os
from typing import List, Union
import pytest

current_dir = os.path.dirname(__file__)

def take_from_list(li: list, indices: Union[int, List[int]]):
    """
    This function returns list of elements for given indices.

    :param li: list of elements
    :param indices: single index or list of indices
    :return: list of elements selected using indices
    """
    if isinstance(indices, int):
        indices = [indices]
    if not isinstance(indices, list) or not all(isinstance(i, int) for i in indices):
        raise ValueError(f"Indices should be integer or list of integers, not {type(indices)}")
    for index in indices:
        if index >= len(li):
            raise IndexError(f"Index {index} is to big for list of length {len(li)}")
        if index < -len(li):
            raise IndexError(f"Index {index} is to small for list of length {len(li)}")

    return [li[i] for i in indices]


def calculate(in_file: str, out_file: str):
    with open(in_file, 'r') as f_p:
        if not os.path.exists(in_file):
            raise FileExistsError(f"File '{in_file}' doesn't exist")
        data = json.load(f_p)

    test_take_from_list()

    result = take_from_list(data["list"], data["indices"])

    if os.path.exists(out_file):
        raise FileExistsError(f"File '{out_file}' already exists")

    with open(out_file, 'w') as f_p:
        json.dump(result, f_p)

def test_take_from_list():
    lista = [i for i in range(10)]
    indeksy = [i for i in range(10)]
    assert take_from_list(lista, indeksy[::2]) == [lista[i] for i in range(len(lista)) if not i % 2]
    assert take_from_list([], []) == []
    assert take_from_list([1, 2, 4, 6], []) == []
    assert take_from_list([1], 0) == [1]
    assert take_from_list([1, 2], [-1]) == [2]
    assert take_from_list([1, 2], -2) == [1]

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", default=os.path.join(current_dir, "input.json"), nargs="?")
    parser.add_argument("output_file", default=os.path.join(current_dir, "output.json"), nargs="?")
    args = parser.parse_args()

    calculate(args.input_file, args.output_file)
