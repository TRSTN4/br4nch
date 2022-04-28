# get.Position

To display a position, use the **following function:**

> br4nch.**display**.**position**(*branch*, *position*, *beautify=True*)

**Required argument(s):**

- *branch* - The branch(es) to display an position for.
- *position* - The position(s) that are displayed.

**Optional argument(s):**

- *beautify* - If this argument is 'True', then the result will be displayed with a special branch format.

**Guide:**

> To print the layer of a position in a branch, specify the position in the `position` argument.
>
> *For more information about positions, head to [positions](../../guides/positions.md).*
>
> ```python
> >>> br4nch.display.layer(branch="Stream", layer="Squid Game")
> Get Position Result:
> ┗━ Branch: Stream
> ˑˑˑ┗━ Layer: Squid Game                  
> ˑˑˑˑˑˑ┗━ Position: 1.2.1
> ```
>
> To print the result without a branch structure in the result, set the `beautify` argument to `False`.
>
> ```python
> >>> br4nch.display.layer(branch="Stream", position="1.2.1", beautify=False)
> Squid Game
> ```
>
> To print the position(s) in multiple branches in the same function call, you can use a list for the `branch` argument.
>
> ```python
> >>> br4nch.display.layer(branch=["Stream"], ["Stream2"], position="2.1.1")
> Get Position Result:
> ┣━ Branch: Stream
> ┃ˑˑ┗━ Layer: The Walking Dead              
> ┃ˑˑˑˑˑ┗━ Position: 2.1.1
> ┗━ Branch: Stream2
> ˑˑˑ┗━ Layer: The Walking Dead                
> ˑˑˑˑˑˑ┗━ Position: 2.1.1
> ```
> 
>To print multiple positions in the same function call, you can use a list for the `position` argument.
> 
>```python
> >>> br4nch.display.layer(branch="Stream", position=["1.1.1", "1.2.1"])
> Get Position Result:
> ┗━ Branch: Stream
> ˑˑˑ┣━ Layer: Interstellar                 
> ˑˑˑ┃ˑˑ┗━ Position: 1.1.1
> ˑˑˑ┗━ Layer: Squid Game                  
> ˑˑˑˑˑˑ┗━ Position: 1.2.1
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- *InstanceStringError*
- *InstanceBooleanError*
- *InvalidPositionError*
- *NotExistingBranchError*
