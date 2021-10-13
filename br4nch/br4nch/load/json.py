# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.librarian import branches, output, uids, sizes, symbols, paint_branch, paint_header, paint_layer
from br4nch.utility.generator import get_uid
from br4nch.utility.handler import DictionaryInstanceError, DuplicateBranchError


def arguments(branch, json):
    json = {branch: json}
    loop(json)
    load_json(json)


def loop(value):
    previous_value = value

    for key, value in value.items():
        if isinstance(value, list):
            copy_value = value
            previous_value.update({key: {}})
            value = previous_value

            for x in list(copy_value):
                previous_value[key].update({x: {}})

        if not isinstance(value, dict):
            previous_value.update({key: {value: {}}})

        if value and not isinstance(value, str) and not isinstance(value, list):
            loop(value)


def load_json(formatted_json):
    if not isinstance(formatted_json, dict):
        raise DictionaryInstanceError("branch", formatted_json)

    for branches_branch in list(branches):
        if list(formatted_json)[0].lower() == branches_branch.lower():
            raise DuplicateBranchError(list(formatted_json)[0])

    branches.update({list(formatted_json)[0]: list(formatted_json.values())[0]})
    output.update({list(formatted_json)[0]: []})
    uids.update({list(formatted_json)[0]: []})
    sizes.update({list(formatted_json)[0]: 1})
    symbols.update({list(formatted_json)[0]: {"line": "┃", "split": "┣━━", "end": "┗━━"}})
    paint_branch.update({list(formatted_json)[0]: {}})
    paint_header.update({list(formatted_json)[0]: {}})
    paint_layer.update({list(formatted_json)[0]: {}})
