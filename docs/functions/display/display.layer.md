# display.layer

To display a layer, use the **following function:**

> br4nch.**display**.**layer**(*branch*, *layer*, *sensitive=False*, *beautify=True*)

**Required argument(s):**

- *branch* - The branch(es) to display the layer(s) for.
- *layer* - The layer(s) that are displayed.

**Optional argument(s):**

- *sensitive* - If this argument is 'True', then the filled in layer must be case-sensitive.
- *beautify* - If this argument is 'True', then the result will be displayed with a special branch format.

**Guide:**

> To print the layer of a position in a branch, specify the name of the layer in the `layer` argument.
>
> ```python
> >>> br4nch.display.layer(branch="Stream", layer="Squid Game")
> Get Position Result:
> ┗━ Branch: Stream
> ˑˑˑ┗━ Layer: Squid Game                  
> ˑˑˑˑˑˑ┗━ Position: 1.2.1
> ```
>
> To make the name of the layer case-sensitive, set the `sensitive` argument to True.
>
> ```python
> >>> br4nch.display.layer(branch="Stream", layer="squid game", sensitive=True)
> ```
>
> To print the result without a branch structure in the result, set the `beautify` argument to ˑFalseˑ.
>
> ```python
> >>> br4nch.display.layer(branch="Stream", layer="Squid Game", beautify=False)
> 1.2.1
> ```
>
> To print the position(s) in multiple branches in the same function call, you can use a list for the `branch` argument.
>
> ```python
> >>> br4nch.display.layer(branch=["Stream"], ["Stream2"], layer="The Walking Dead")
> Get Position Result:
> ┣━ Branch: Stream
> ┃ˑˑ┗━ Layer: The Walking Dead              
> ┃ˑˑˑˑˑ┗━ Position: 2.1.1
> ┗━ Branch: Stream2
> ˑˑˑ┗━ Layer: The Walking Dead                
> ˑˑˑˑˑˑ┗━ Position: 2.1.1
> ```
> 
>To print multiple positions in the same function call, you can use a list for the `layer` argument.
> 
>```python
> >>> br4nch.display.layer(branch="Stream", layer=["Interstellar", "Squid Game"])
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
- *NotExistingBranchError*

