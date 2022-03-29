# duplicate.layer

To duplicate a layer, use the **following function:**

> br4nch.**duplicate**.**layer**(*branch*, *duplicate*, *position*, *put=""*, *paint=False*, *delete=False*)

**Required argument(s):**

- *branch* - The branch(es) where the layer(s) to be copied are located.
- *duplicate* - The position(s) of the layer(s) to be duplicated.
- *position* - The position(s) where to add the duplicated layer(s).

**Optional argument(s):**

- *put* -  The branch(es) where the copied layer(s) will be placed at the chosen position(s).
- *paint* - If this argument is 'True', the paint is duplicated and linked to the duplicated layer(s).
- *delete* - If this argument is 'True', then the layer(s) in the original place will be deleted.

**Guide:**

> To copy a layer, specify the branch name, the layer you want to copy in the `duplicate` argument and specify the position to copy the layer(s) to in the `position` argument.
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
> >>> br4nch.duplicate.layer(branch="Stream", duplicate="1.1", position="2")
> 
> >>> br4nch.display.branch(branch="Stream")
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┗━ Series
> ┗━ Prime Video
> ˑˑˑ┗━ Movies
> ```
>
> To copy the layer(s) to another existing branch, specify the branch name the layer(s) should go to in the `put` argument.
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
> >>> br4nch.duplicate.layer(branch="Stream", duplicate="1.1", position="0", put="MyBranch")
> 
> >>> br4nch.display.branch(branch=["Stream", "MyBranch"])
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
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
> To take the paint from the copied layer(s) to the new position(s), set the `paint` argument to `True`.
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
> >>> br4nch.duplicate.layer(branch="Stream", duplicate="1.2", position="2", paint=True)
> 
> >>> br4nch.display.branch(branch="Stream")
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┗━ Series
> ┗━ Prime Video
> ˑˑˑ┣━ Movies
> ˑˑˑ┗━ Series
> ```
>
> To copy the layer(s) and then delete it directly from the original position(s), set the `delete` argument to `True`.
>
> ```python
> >>> br4nch.display.branch(branch="Stream")
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┗━ Series
> ┗━ Prime Video
> ˑˑˑ┣━ Movies
> ˑˑˑ┗━ Series
> 
> >>> br4nch.duplicate.layer(branch="Stream", duplicate="2", position="1", delete=True)
> 
> >>> br4nch.display.branch(branch="Stream")
> Movies & Series
> ┗━ Netflix
> ˑˑˑ┣━ Movies
> ˑˑˑ┣━ Series
> ˑˑˑ┗━ Prime Video
> ˑˑˑˑˑˑ┣━ Movies
> ˑˑˑˑˑˑ┗━ Series
> ```
>
> To duplicate the position(s) in multiple branches in the same function call, you can use a list for the `branch` argument.
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
> >>> br4nch.duplicate.layer(branch=["Cars", "Electronics"], duplicate="1.1", position="2")
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
> To duplicate multiple layers in the same function call, you can use a list for the `duplicate` argument.
>
> ```python
> >>> br4nch.display.branch(branch="Fruits")
> Fruits
> ┣━ Trees
> ┃ˑˑ┣━ Apple
> ┃ˑˑ┗━ Pear
> ┗━ Plant
> 
> >>> br4nch.duplicate.layer(branch="Fruits", duplicate=["1.1", "1,2"], position="2")
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
> To duplicate the layer(s) to multiple positions in the same function call, you can use a list for the `position` argument.
>
> ```python
> >>> br4nch.display.branch(branch="Board")
> Info
> ┣━ USA
> ┃ˑˑ┣━ LA
> ┃ˑˑ┗━ Texas
> ┗━ Netherlands
> 
> >>> br4nch.duplicate.layer(branch="Board", duplicate="1.2", position=["0", "2"])
> 
> >>> br4nch.display.branch(branch="Board")
> Info
> ┣━ USA
> ┃ˑˑ┣━ LA
> ┃ˑˑ┗━ Texas
> ┣━ Netherlands
> ┃ˑˑ┗━ Texas
> ┗━ Texas
> ```
>
> To duplicate multiple layers to multiple diffrent branches in the same function call, you can use a list for the `put` argument.
>
> ```python
> >>> br4nch.display.branch(branch=["Parks", "Food"])
> Fruits
> ┣━ Vacation
> ┃ˑˑ┣━ Apple
> ┃ˑˑ┗━ Pear
> ┗━ Games
> ˑˑˑ┗━ Go Park
> Food
> ┣━ Pie
> ┃ˑˑ┣━ Crumble
> ┃ˑˑ┗━ Cream
> ┗━ Fruit
> ˑˑˑ┣━ Apple
> ˑˑˑ┗━ Pear
> 
> >>> br4nch.duplicate.layer(branch="Parks", duplicate="2.1", position="0", put=["Parks", "Food"])
> 
> >>> br4nch.display.branch(branch=["Parks", "Food"])
> Fruits
> ┣━ Vacation
> ┃ˑˑ┣━ Apple
> ┃ˑˑ┗━ Pear
> ┣━ Games
> ┃ˑˑ┗━ Go Park
> ┗━ Go Park
> Food
> ┣━ Pie
> ┃ˑˑ┣━ Crumble
> ┃ˑˑ┗━ Cream
> ┣━ Fruit
> ┃ˑˑ┣━ Apple
> ┃ˑˑ┗━ Pear
> ┗━ Go Park
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- *InstanceStringError*
- *InstanceBooleanError*
- *InvalidPositionError*
- *NotExistingBranchError*
