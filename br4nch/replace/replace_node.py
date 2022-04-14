# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from br4nch.utility.utility_librarian import existing_trees, existing_uids, existing_paint_nodes
from br4nch.utility.utility_handler import InstanceStringError, NotExistingTreeError
from br4nch.utility.utility_generator import UtilityGenerator
from br4nch.utility.utility_positioner import UtilityPositioner


class ReplaceNode:
    def __init__(self, tree, node, parent):
        self.trees = tree
        self.node = node
        self.parents = parent

        self.validate_arguments()
        self.replace_node()

    def validate_arguments(self):
        if not isinstance(self.trees, list):
            self.trees = [self.trees]

        for index in range(len(self.trees)):
            if not isinstance(self.trees[index], str):
                raise InstanceStringError("tree", self.trees[index])

            if self.trees[index].lower() not in list(map(str.lower, existing_trees)):
                raise NotExistingTreeError(self.trees[index])

            for existing_tree in list(existing_trees):
                if self.trees[index].lower() == existing_tree.lower():
                    self.trees[index] = existing_tree

        if "*" in self.trees:
            self.trees.clear()
            for existing_tree in list(existing_trees):
                self.trees.append(existing_tree)

        if not isinstance(self.node, str):
            raise InstanceStringError("node", self.node)

        while True:
            if self.node and self.node[-1] == "\n":
                self.node = self.node[:-1]
            else:
                break

        if not isinstance(self.parents, list):
            self.parents = [self.parents]

    def replace_node(self):
        for tree in self.trees:
            for parent in UtilityPositioner(tree, self.parents.copy()):
                child = self.get_nodes(parent, existing_trees[tree][list(existing_trees[tree])[0]])
                if child:
                    for parent_node, child_nodes in child.items():
                        parent_node_uid = self.node + UtilityGenerator(tree)
                        existing_uids[tree].remove(parent_node[-10:])
                        existing_paint_nodes[tree][parent_node_uid] = existing_paint_nodes[tree].pop(parent_node)

                        index = list(child_nodes).index(parent_node)
                        child_nodes[parent_node_uid] = child_nodes.pop(parent_node)

                        for number in list(child_nodes)[index:-1]:
                            child_nodes[number] = child_nodes.pop(number)
                            existing_paint_nodes[tree][number] = existing_paint_nodes[tree].pop(number)

    def get_nodes(self, parent, child):
        count = 0
        for parent_node, child_nodes in child.items():
            count = count + 1

            if count == int(parent[0]):
                if len(parent) == 1:
                    return {parent_node: child}
                else:
                    if child_nodes:
                        parent.pop(0)
                        return self.get_nodes(parent, child_nodes)
