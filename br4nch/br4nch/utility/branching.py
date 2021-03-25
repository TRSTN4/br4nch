# Creates the branching part of the code.
def branching(action, extender):
    # Stores three spaces in a row.
    space_x3 = " " * 3

    # Stores all actions to variables.
    header_end = "\n╻"
    module_multi = "┃\n┣━━"
    module_end = "┃\n┗━━"
    subject_multi = extender + space_x3 + "┃\n" + extender + space_x3 + "┣━━"
    subject_multi_last = extender + space_x3 + "┃\n" + extender + space_x3 + "┣━━"
    subject_end = extender + space_x3 + "┃\n" + extender + space_x3 + "┗━━"
    subject_end_last = extender + space_x3 + "┃\n" + extender + space_x3 + "┗━━"
    object_multi = extender + space_x3 + "┃\n" + extender + space_x3 + "┣━━"
    object_end = extender + space_x3 + "┃\n" + extender + space_x3 + "┗━━"

    # Saves all the actions in a list.
    branching_action = [header_end, module_multi, module_end, subject_multi, subject_multi_last, subject_end,
                        subject_end_last, object_multi, object_end]

    # Saves all the action ids in a list.
    branching_id = ["header_end", "module_multi", "module_end", "subject_multi", "subject_multi_last",
                    "subject_end", "subject_end_last", "object_multi", "object_end"]

    # Checks if the action list has any value.
    if action:
        # Loops through total length of the branching action list.
        for number in range(len(branching_action)):
            # Checks if the parsed action is equal to a id in the id list.
            if action == branching_id[number]:
                # Returns the requested action.
                return branching_action[number]
