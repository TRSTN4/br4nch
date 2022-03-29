# delete.layer

To delete an layer, use the **following function:**

> br4nch.**delete**.**layer**(*branch*, *position*)

**Required argument(s):**

- *branch* - The name of the branch(es) to which the layer will be deleted.
- *position* - The position(s) where the layer(s) will be deleted.

**Guide:**

> To delete a layer, specify the position linked to the layer you want to delete.
>
> *For more information about positions, head to [positions](../../guides/positions.md).*
>
> ```python
> >>> br4nch.display.branch(branch="Board")
> Information
> ┣━ Animals
> ┃ˑˑ┣━ Dog
> ┃ˑˑ┗━ Cat
> ┣━ Food
> ┗━ Bread
> 
> >>> br4nch.delete.layer(branch="Board", position="1")
> 
> >>> br4nch.display.branch(branch="Board")
> Information
> ┣━ Food
> ┗━ Bread
> ```
>
> To delete the given position(s) in multiple branches in the same function call, you can use a list for the `branch` argument.
>
> ```python
> >>> br4nch.delete.layer(branch=["BranchOne", "BranchTwo"], position="1")
> ```
>
> To delete multiple positions in the same function call, you can use a list for the `position` argument.
>
> ```python
> >>> br4nch.delete.layer(branch="TestBranch", position=["1", "2.3", "3.1"])
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
For more information about errors, head to [errors](../../guides/errors.md).

- *InstanceStringError*
- *InvalidPositionError*
- *NotExistingBranchError*

