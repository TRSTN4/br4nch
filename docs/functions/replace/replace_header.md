# replace.Header

To replace a header, use the **following function:**

> br4nch.**replace**.**Header**(*tree*, *new_header*)

**Required argument(s):**

- *tree* - The name of tree(s) whose header will be replaced.
- *new_header* - The new name for the header(s).

**Guide:**

> To replace a header name, specify the tree name in the `tree` argument and the new header name in the `new_header` argument.
>
> ```python
> >>> br4nch.replace.Header(tree="MyTree", new_header="Replaced Header!")
> 
> >>> br4nch.display.Tree(tree="MyTree")
> Replaced Header!
> ┣━ ABCD
> ┃ˑˑ┣━ Just text
> ┃ˑˑ┗━ Two lines
> ┗━ Second layer
> ```
>
> To replace headers for multiple trees in the same function call, you can use a list for the `tree` argument.
>
> ```python
> >>> br4nch.replace.Header(branch=["TreeOne", "TreeTwo"], new_header="Replaced Header!")
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- InstanceStringError
- NotExistingTreeError
