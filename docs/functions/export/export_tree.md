# export.Tree

To export a tree, use the **following function:**

> br4nch.**export**.**Tree**(*tree*, *output_folder*, *attributes=False*)

**Required argument(s):**

- *tree* - The tree that will be exported to a br4nch file.
- *output_folder*  - The output folder for the br4nch file.

**Optional argument(s):**

- *attributes* - If this argument is True, then the size and symbols are copied and linked to the text file.

**Guide:**

> To export the output of the tree to a file, specify the tree in the `tree` argument and specify the path to export the file to, in the `output_folder  ` argument.
>
> ```python
> >>> br4nch.export.Tree(tree="MyTree", output_folder="D:/MyOutput")
> # Path: D:\MyOutput\br4nch-MyTree
> ```
>
> To also export the size and symbols, set the `attributes` argument to `True`.
>
> ```python
> >>> br4nch.export.Tree(tree="MyTree", output_folder="D:/MyOutput", attributes=True)
> # Path: D:\MyOutput\br4nch-MyTree
> ```
>
> To export multiple trees in the same function call, you can use a list for the `tree` argument.
>
> ```python
> >>> br4nch.export.Tree(tree=["MyTree", "Stream"], output_folder="D:/MyOutput")
> # Path: D:\MyOutput\br4nch-MyTree
> # Path: D:\MyOutput\br4nch-Stream
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- InstanceBooleanError
- InstanceStringError
- NotExistingDirectoryError
- NotExistingTreeError

