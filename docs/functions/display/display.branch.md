# display.branch

To display a branch, use the **following function:**

> br4nch.**display**.**branch**(*branch*, *delete=False*)

**Required argument(s):**

- *branch* - The branch(es) to display.

**Optional argument(s):**

- *delete* - If this argument is 'True', the branch(es) will be removed after it is printed.

**Guide:**

> Prints the branch given in the branch argument. In this example we will print the branch ˑStreamˑ.
>
> ```python
> >>> br4nch.display.branch(branch="Stream")
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┃ˑˑ┗━ Interstellar
> ┃ˑˑ┗━ Series
> ┃ˑˑˑˑˑ┣━ Squid Game
> ┃ˑˑˑˑˑ┗━ The Crown
> ┗━ Prime Video
> ˑˑˑ┣━ Movies
> ˑˑˑ┃ˑˑ┣━ Tenet
> ˑˑˑ┃ˑˑ┗━ Parasite
> ˑˑˑ┗━ Series
> ˑˑˑˑˑˑ┗━ The Walking Dead
> ```
>
> To print a branch and immediately delete it, specify the value 'True' in the ˑdeleteˑ argument.
>
> ```python
> >>> br4nch.display.branch(branch="Stream", delete=True)
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┃ˑˑ┗━ Interstellar
> ┃ˑˑ┗━ Series
> ┃ˑˑˑˑˑ┣━ Squid Game
> ┃ˑˑˑˑˑ┗━ The Crown
> ┗━ Prime Video
> ˑˑˑ┣━ Movies
> ˑˑˑ┃ˑˑ┣━ Tenet
> ˑˑˑ┃ˑˑ┗━ Parasite
> ˑˑˑ┗━ Series
> ˑˑˑˑˑˑ┗━ The Walking Dead
> 
> >>> br4nch.display.branch(branch="Stream")
> NotExistingBranchError: The branch: 'Stream' does not exists.
> ```
>
> To print multiple branches in the same function call, you can use a list for the ˑbranchˑ argument.
>
> ```python
> >>> br4nch.display.branch(branch=["Stream", "MyBranch"])
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┃ˑˑ┗━ Interstellar
> ┃ˑˑ┗━ Series
> ┃ˑˑˑˑˑ┣━ Squid Game
> ┃ˑˑˑˑˑ┗━ The Crown
> ┗━ Prime Video
> ˑˑˑ┣━ Movies
> ˑˑˑ┃ˑˑ┣━ Tenet
> ˑˑˑ┃ˑˑ┗━ Parasite
> ˑˑˑ┗━ Series
> ˑˑˑˑˑˑ┗━ The Walking Dead
> My header!
> ┣━ My Layer
> ┃ˑˑ┣━ Sublayer One
> ┃ˑˑ┃ˑˑ┗━ Last Layer
> ┃ˑˑ┗━ Sublayer Two
> ┃ˑˑˑˑˑ┗━ Last Layer
> ┗━ One
> ˑˑˑTwo
> ˑˑˑThree
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- *InstanceStringError*
- *InstanceBooleanError*
- *NotExistingBranchError*

