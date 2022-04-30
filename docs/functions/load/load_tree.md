# load.Tree

To load a tree file, use the **following function:**

> br4nch.**load**.**Tree**(*tree_file*, *attributes_file=""*)

**Required argument(s):**

- *tree_file* - The exported tree file path.

**Optional argument(s):**

- *attributes_file* - The exported attributes file path.

**Guide:**

> To import a exported tree file, specify the path of the tree file in the `tree_file` argument.
>
> ```python
> >>> br4nch.load.Tree(tree_file="D:/br4nch-MyTree/tree-MyTree.br4nch")
> ```
>
> To also import a exported attributes file, specify the path of the attributes file in the `attributes_file` argument.
>
> ```python
> >>> br4nch.load.Tree(tree_file="D:/br4nch-MyTree/tree-MyBranch.br4nch", attributes_file="D:/br4nch-MyBranch/attributes-MyTree.br4nch")
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- InstanceStringError
- DuplicateTreeError
- NotExistingTreeFileError
- InvalidTreeFileError
- NotExistingAttributesFileError
- InvalidAttributesFileError
