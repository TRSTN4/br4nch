# br4nch.replace.Header

To replace a header, use the **following function:**

> br4nch.**replace**.**header**(*branch*, *replace*)

**Required argument(s):**

- *branch* - The name of branch(es) whose header is to be replaced.
- *replace* - The new name for the header(s).

**Guide:**

> To replace a header name, specify the branch name in the `branch` argument and the new header name in the `replace` argument.
>
> ```python
> >>> br4nch.replace.header(branch="MyBranch", replace="Replaced Header!")
> 
> >>> br4nch.display.branch(branch="ReplacedBranch")
> Replaced Header!
> ┣━ ABCD
> ┃ˑˑ┣━ Just text
> ┃ˑˑ┗━ Two lines
> ┗━ Second layer
> ```
>
> To replace headers for multiple branches in the same function call, you can use a list for the `branch` argument.
>
> ```python
> >>> br4nch.replace.header(branch=["BranchOne", "BranchTwo"], replace="Replaced Header!")
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- *InstanceStringError*
- *NotExistingBranchError*

