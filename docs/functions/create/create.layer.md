# create.layer

To create a new layer, use the **following function:**

> br4nch.**create**.**layer**(*branch*, *layer*, *position*)

**Required argument(s):**

- *branch* - The name of the branch(es) where the layer(s) will be created.
- *layer* - The name for the layer(s).
- *position* - The position(s) where the layer(s) in the branch(es) are created.

**Guide:**

> To add a new layer to a branch, first indicate in which branch the layer should be created, We use the branch `MyBranch`. Then you specify the name of the layer(s) you want to create, you also need to specify the position where the layer should be created in the branch. 
>
> *For more information about positions, head to [positions](../../guides/positions.md).*
>
> ```python
> >>> br4nch.create.layer(branch="MyBranch", layer="My Layer", position="0")
> 
> >>> br4nch.display.branch(branch="MyBranch")
> My header!
> ┗━ My Layer
> ```
>
> You can also use `\n` in a layer name.
>
> ```python
> >>> br4nch.create.layer(branch="MyBranch", layer="One\nTwo\nThree", position="0")
> 
> >>> br4nch.display.branch(branch="MyBranch")
> My header!
> ┣━ My Layer
> ┗━ One
>    ‎  Two
>    ‎  Three
> ```
>
> To create the layer(s) in multiple branches in the same function call, you can use a list for the `branch` argument.
>
> ```python
> >>> br4nch.create.layer(branch=["ZooA", "ZooB"], layer="Animals", position="0")
> 
> >>> br4nch.display.branch(branch=["ZooA", "ZooB"])
> Zoo Alpha
> ┗━ Animals
> Zoo Beta
> ┗━ Animals
> ```
>
> To create multiple layer(s) in the same function call, you can use list for the `layer` argument.
>
> ```python
> >>> br4nch.create.layer(branch="MyBranch", layer=["Sublayer One", "Sublayer Two"], position="1")
> 
> >>> br4nch.display.branch(branch="MyBranch")
> My header!
> ┣━ My Layer
> ┃  ┣━ Sublayer One
> ┃  ┗━ Sublayer Two
> ┗━ One
>    ‎  Two
>    ‎  Three
> ```
>
> To create the layer(s) for multiple position in the same function call, you can use a list for the `position` argument.
>
> ```python
> >>> br4nch.create.layer(branch="MyBranch", layer="Last Layer", position=["1.1", "1.2"])
> 
> >>> br4nch.display.branch(branch="MyBranch")
> My header!
> ┣━ My Layer
> ┃  ┣━ Sublayer One
> ┃  ┃  ┗━ Last Layer
> ┃  ┗━ Sublayer Two
> ┃	  ┗━ Last Layer
> ┗━ One
>    ‎‎‎Two
>    ‎‎‎Three
> ```
>

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
For more information about errors, head to [errors](../../guides/errors.md).

- *InstanceStringError*
- *InvalidPositionError*
- *NotExistingBranchError*

