# move.layer

To move a layer, use the **following function:**

> br4nch.**move**.**layer**(*branch*, *move*, *position*, *put=""*, *paint=False*)

**Required argument(s):**

- branch - The branch(es) where the layer(s) to be moved are located.
- move - The position(s) of the layer(s) to be moved.
- position - The position where to add the moved layer(s).

**Optional argument(s):**

- put -  The branch where the copied layer(s) will be placed at the chosen position.
- paint - If this argument is 'True', the paint is copied and linked to the moved layer.

**Guide:**

> To move a layer, specify the branch name, the layer you want to move in the `move` argument and specify the position to move the layer(s) to in the `position` argument.
>
> *For more information about positions, head to [positions](../../guides/positions.md).*
>
> ```python
> >>> br4nch.display.branch(branch="Stream")
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┗━ Series
> ┗━ Prime Video
> 
> >>> br4nch.move.layer(branch="Stream", move="1.1", position="2")
> 
> >>> br4nch.display.branch(branch="Stream")
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┗━ Series
> ┗━ Prime Video
> ˑˑˑ┗━ Movies
> ```
>
> To move the layer(s) to another existing branch, specify the branch name the layer(s) should go to in the `put` argument.
>
> ```python
> >>> br4nch.display.branch(branch=["Stream", "MyBranch"])
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┗━ Series
> ┗━ Prime Video
> ˑˑˑ┗━ Movies
> My header
> ┗━ Grass
> ˑˑˑ┗━ Dirt
> ˑˑˑˑˑˑ┗━ Stone
> 
> >>> br4nch.move.layer(branch="Stream", move="1.1", position="0", put="MyBranch")
> 
> >>> br4nch.display.branch(branch=["Stream", "MyBranch"])
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┗━ Series
> ┗━ Prime Video
> ˑˑˑ┗━ Movies
> My header
> ┣━ Grass
> ┃ˑˑ┗━ Dirt
> ┃ˑˑˑˑˑ┗━ Stone
> ┗━ Movies
> ```
>
> To take the paint from the moved layer(s) to the new position(s), set the `paint` argument to `True`.
>
> ```python
> >>> br4nch.display.branch(branch="Stream")
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┗━ Series
> ┗━ Prime Video
> ˑˑˑ┗━ Movies
> 
> >>> br4nch.move.layer(branch="Stream", move="1.2", position="2", paint=True)
> 
> >>> br4nch.display.branch(branch="Stream")
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┗━ Movies
> ┗━ Prime Video
> ˑˑˑ┣━ Movies
> ˑˑˑ┗━ Series
> ```
>
> To move the position(s) in multiple branches in the same function call, you can use a list for the `branch` argument.
>
> ```python
> >>> br4nch.display.branch(branch=["Cars", "Electronics"])
> Garage
> ┗━ Cars
> ˑˑˑ┣━ Mercedes
> ˑˑˑ┗━ BMW
> PC
> ┣━ Mouses
> ┃ˑˑ┣━ Microsoft
> ┃ˑˑ┗━ Razer
> ┗━ Keyboards
> ˑˑˑ┣━ Steel Series
> ˑˑˑ┗━ Omen
> 
> >>> br4nch.move.layer(branch=["Cars", "Electronics"], move="1.1", position="2")
> 
> >>> br4nch.display.branch(branch="Cars")
> Garage
> ┣━ Cars
> ┃ˑˑ┣━ Mercedes
> ┃ˑˑ┗━ BMW
> ┗━ Mercedes
> PC
> ┣━ Mouses
> ┃ˑˑ┣━ Microsoft
> ┃ˑˑ┗━ Razer
> ┣━ Keyboards
> ┃ˑˑ┣━ Steel Series
> ┃ˑˑ┗━ Omen
> ┗━ Microsoft
> ```
>
> To move multiple layers in the same function call, you can use a list for the `move` argument.
>
> ```python
> >>> br4nch.display.branch(branch="Fruits")
> Fruits
> ┣━ Trees
> ┃ˑˑ┣━ Apple
> ┃ˑˑ┗━ Pear
> ┗━ Plant
> 
> >>> br4nch.move.layer(branch="Fruits", move=["1.1", "1,2"], position="2")
> 
> >>> br4nch.display.branch(branch="Fruits")
> Fruits
> ┣━ Trees
> ┃ˑˑ┣━ Apple
> ┃ˑˑ┗━ Pear
> ┗━ Plant
> ˑˑˑ┣━ Apple
> ˑˑˑ┗━ Pear
> ```
>

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- *InstanceStringError*
- *InstanceBooleanError*
- *InvalidPositionError*
- *NotExistingBranchError*
