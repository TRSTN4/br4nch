# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.librarian import branches, output, uids, sizes, symbols, paint_branch, paint_header, paint_layer
from br4nch.utility.generator import generate_uid
from br4nch.utility.handler import DictionaryInstanceError, DuplicateBranchError, StringInstanceError


def arguments(branch, header, json):
    """Gets the arguments and parses them to the 'LoadJson' class."""
    LoadJson(branch, header, json)


class LoadJson:
    def __init__(self, argument_branch, argument_header, argument_json):
        """Gets the arguments and parses them to the 'task_manager' function."""
        self.task_manager(argument_branch, argument_header, argument_json)

    def task_manager(self, argument_branch, argument_header, argument_json):
        if not isinstance(argument_branch, str):
            raise StringInstanceError("branch", argument_branch)

        if not isinstance(argument_header, str):
            raise StringInstanceError("header", argument_header)

        if not isinstance(argument_json, dict):
            raise DictionaryInstanceError("json", argument_json)

        for branches_branch in list(branches):
            if argument_branch.lower() == branches_branch.lower():
                raise DuplicateBranchError(argument_branch)

        self.illegal_values_manager(argument_branch, argument_json)

        output.update({argument_branch: []})
        uids.update({argument_branch: []})
        sizes.update({argument_branch: 1})
        symbols.update({argument_branch: {"line": "┃", "split": "┣━━", "end": "┗━━"}})
        paint_branch.update({argument_branch: {}})
        paint_header.update({argument_branch: {}})
        paint_layer.update({argument_branch: {}})

        self.change_layer_uid(argument_branch, {argument_branch: argument_json})

        branches.update({argument_branch: {argument_header: argument_json}})

    def illegal_values_manager(self, branch, value):
        previous_value = value

        for layer, value in value.items():
            if isinstance(value, list):
                copy_value = value
                previous_value.update({layer: {}})
                value = previous_value

                for x in list(copy_value):
                    previous_value[layer].update({x: {}})

            if not isinstance(value, dict):
                previous_value.update({layer: {value: {}}})

            if value and not isinstance(value, str) and not isinstance(value, list):
                self.illegal_values_manager(branch, value)

    def change_layer_uid(self, branch, value):
        """
        Value dictionary loop:
          - Generates a new UID for the copied 'layer' variable. Then the old layer is deleted and replaced with the new
            generated layer with the new UID.

          - Checks if the current value of 'layer' exists in the branch's 'paint_layer' list. Then it is checked whether
            the variable 'argument_paint' is true. If the value exists in the list and the 'argument_paint' is true,
            then the newly generated layer with UID is added to the list with the value of the value of the variable
            'layer'.
          - If the current value of 'layer' does not exist in the branch's 'paint_layer' list. Then the newly generated
            layer with UID is added to the list with the value of an empty string.

          - If there is a value of the 'value' variable, the 'change_layer_uid' function will be called again with the
            new value of the 'value' variable as argument.
        """
        previous_value = value

        for layer, value in value.copy().items():
            previous_value[layer + generate_uid(branch)] = previous_value.pop(layer)

            if value:
                self.change_layer_uid(branch, value)
