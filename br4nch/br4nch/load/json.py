# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.librarian import branches, output, uids, sizes, symbols, paint_branch, paint_header, paint_layer
from br4nch.utility.generator import generate_uid
from br4nch.utility.handler import DictionaryInstanceError, DuplicateBranchError


def arguments(branch, header, json):
    json = {branch: json}

    output.update({list(json)[0]: []})
    uids.update({list(json)[0]: []})
    sizes.update({list(json)[0]: 1})
    symbols.update({list(json)[0]: {"line": "┃", "split": "┣━━", "end": "┗━━"}})
    paint_branch.update({list(json)[0]: {}})
    paint_header.update({list(json)[0]: {}})
    paint_layer.update({list(json)[0]: {}})

    loop(branch, json)

    load_json(branch, header, json)


def loop(branch, value):
    previous_value = value

    for key, value in value.copy().items():
        if isinstance(value, list):
            copy_value = value
            previous_value.update({key: {}})
            value = previous_value

            for x in list(copy_value):
                previous_value[key].update({x: {}})

        if not isinstance(value, dict):
            previous_value.update({key: {value: {}}})

        previous_value[key + generate_uid(branch)] = previous_value.pop(key)

        if value and not isinstance(value, str) and not isinstance(value, list):
            loop(branch, value)


def load_json(branch, header, formatted_json):
    if not isinstance(formatted_json, dict):
        raise DictionaryInstanceError("branch", formatted_json)

    for branches_branch in list(branches):
        if list(formatted_json)[0].lower() == branches_branch.lower():
            raise DuplicateBranchError(list(formatted_json)[0])

    branches.update({branch: {header: list(formatted_json.values())[0]}})

