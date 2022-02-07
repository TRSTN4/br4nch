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
> ┃‎‎┣━ Movies
> ┃‎‎┗━ Series
> ┗━ Prime Video
> 
> >>> br4nch.duplicate.layer(branch="Stream", duplicate="1.1", position="2")
> 
> >>> br4nch.display.branch(branch="Stream")
> Movies & Series
> ┣━ Netflix
> ┃‎‎┣━ Movies
> ┃‎‎┗━ Series
> ┗━ Prime Video
> ‎‎‎┗━ Movies
> ```
>
> To copy the layer(s) to another existing branch, specify the branch name the layer(s) should go to in the `put` argument.
>
> ```python
> >>> br4nch.display.branch(branch=["Stream", "MyBranch"])
> Movies & Series
> ┣━ Netflix
> ┃‎‎┣━ Movies
> ┃‎‎┗━ Series
> ┗━ Prime Video
> ‎‎‎┗━ Movies
> My header
> ┗━ Grass
> ‎‎‎┗━ Dirt
> ‎‎‎‎‎‎┗━ Stone
> 
> >>> br4nch.duplicate.layer(branch="Stream", duplicate="1.1", position="0", put="MyBranch")
> 
> >>> br4nch.display.branch(branch="MyBranch")
> My header
> ┣━ Grass
> ┃‎‎┗━ Dirt
> ┃‎‎‎‎‎┗━ Stone
> ┗━ Movies
> ```
>
> To take the paint from the copied layer(s) to the new position(s), set the `paint` argument to `True`.
>
> ```python
> >>> br4nch.display.branch(branch="Stream")
> Movies & Series
> ┣━ Netflix
> ┃‎‎┣━ Movies
> ┃‎‎┗━ Series
> ┗━ Prime Video
> ‎‎‎┗━ Movies
> 
> >>> br4nch.duplicate.layer(branch="Stream", duplicate="1.2", position="2", paint=True)
> 
> >>> br4nch.display.branch(branch="Stream")
> Movies & Series
> ┣━ Netflix
> ┃‎‎┣━ Movies
> ┃‎‎┗━ Series
> ┗━ Prime Video
> ‎‎‎┣━ Movies
> ‎‎‎┗━ Series
> ```
>
> To copy the layer(s) and then delete it directly from the original position(s), set the `delete` argument to `True`.
>
> ```python
> >>> br4nch.display.branch(branch="Stream")
> Movies & Series
> ┣━ Netflix
> ┃‎‎┣━ Movies
> ┃‎‎┗━ Series
> ┗━ Prime Video
> ‎‎‎┣━ Movies
> ‎‎‎┗━ Series
> 
> >>> br4nch.duplicate.layer(branch="Stream", duplicate="2", position="1", delete=True)
> 
> >>> br4nch.display.branch(branch="Stream")
> Movies & Series
> ┗━ Netflix
> ‎‎‎┣━ Movies
> ‎‎‎┣━ Series
> ‎‎‎┗━ Prime Video
> ‎‎‎‎‎‎┣━ Movies
> ‎‎‎‎‎‎┗━ Series
> ```
>
> To duplicate the position(s) in multiple branches in the same function call, you can use a list for the `branch` argument.
>
> ```python
> >>> br4nch.display.branch(branch=["Cars", "Electronics"])
> Garage
> ┗━ Cars
> ‎‎‎┣━ Mercedes
> ‎‎‎┗━ BMW
> PC
> ┣━ Mouses
> ┃‎‎┣━ Microsoft
> ┃‎‎┗━ Razer
> ┗━ Keyboards
> ‎‎‎┣━ Steel Series
> ‎‎‎┗━ Omen
> 
> >>> br4nch.duplicate.layer(branch=["Cars", "Electronics"], duplicate="1.1", position="2")
> 
> >>> br4nch.display.branch(branch="Cars")
> Garage
> ┣━ Cars
> ┃‎‎┣━ Mercedes
> ┃‎‎┗━ BMW
> ┗━ Mercedes
> PC
> ┣━ Mouses
> ┃‎‎┣━ Microsoft
> ┃‎‎┗━ Razer
> ┣━ Keyboards
> ┃‎‎┣━ Steel Series
> ┃‎‎┗━ Omen
> ┗━ Microsoft
> ```
>
> To duplicate multiple layers in the same function call, you can use a list for the `duplicate` argument.
>
> ```python
> >>> br4nch.display.branch(branch="Fruits")
> Fruits
> ┣━ Trees
> ┃‎‎┣━ Apple
> ┃‎‎┗━ Pear
> ┗━ Plant
> 
> >>> br4nch.duplicate.layer(branch="Fruits", duplicate=["1.1", "1,2"], position="2")
> 
> >>> br4nch.display.branch(branch="Fruits")
> Fruits
> ┣━ Trees
> ┃‎‎┣━ Apple
> ┃‎‎┗━ Pear
> ┗━ Plant
> ‎‎‎┣━ Apple
> ‎‎‎┗━ Pear
> ```
>
> To duplicate the layer(s) to multiple positions in the same function call, you can use a list for the `position` argument.
>
> ```python
> >>> br4nch.display.branch(branch="Board")
> Info
> ┣━ USA
> ┃‎‎┣━ LA
> ┃‎‎┗━ Texas
> ┗━ Netherlands
> 
> >>> br4nch.duplicate.layer(branch="Board", duplicate="1.2", position=["0", "2"])
> 
> >>> br4nch.display.branch(branch="Board")
> Info
> ┣━ USA
> ┃‎‎┣━ LA
> ┃‎‎┗━ Texas
> ┣━ Netherlands
> ┃‎‎┗━ Texas
> ┗━ Texas
> ```
>
> To duplicate multiple layers to multiple diffrent branches in the same function call, you can use a list for the `put` argument.
>
> ```python
> >>> br4nch.display.branch(branch=["Parks", "Food"])
> Fruits
> ┣━ Vacation
> ┃‎‎┣━ Apple
> ┃‎‎┗━ Pear
> ┗━ Games
> ‎‎‎┗━ Go Park
> Food
> ┣━ Pie
> ┃‎‎┣━ Crumble
> ┃‎‎┗━ Cream
> ┗━ Fruit
> ‎‎‎┣━ Apple
> ‎‎‎┗━ Pear
> 
> >>> br4nch.duplicate.layer(branch="Parks", duplicate="2.1", position="0", put=["Parks", "Food"])
> 
> >>> br4nch.display.branch(branch=["Parks", "Food"])
> Fruits
> ┣━ Vacation
> ┃‎‎┣━ Apple
> ┃‎‎┗━ Pear
> ┣━ Games
> ┃‎‎┗━ Go Park
> ┗━ Go Park
> Food
> ┣━ Pie
> ┃‎‎┣━ Crumble
> ┃‎‎┗━ Cream
> ┣━ Fruit
> ┃‎‎┣━ Apple
> ┃‎‎┗━ Pear
> ┗━ Go Park
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
For more information about errors, head to [errors](../../guides/errors.md).

- *InstanceStringError*
- *InstanceBooleanError*
- *InvalidPositionError*
- *NotExistingBranchError*
