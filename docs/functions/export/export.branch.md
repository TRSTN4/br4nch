# export.branch

To export an branch, use the **following function:**

> br4nch.**export**.**branch**(*branch*, *directory*, *package=False*)

**Required argument(s):**

- branch - The branch that will be exported to an file.
- directory  - The output directory for the branch file.

**Optional argument(s):**

- package - If this argument is 'True', then the size, symbols and paint will also be exported.

**Guide:**

> To export the output of the branch to a file, specify the branch in the `branch` argument and specify the path to export the file to, in the `directory` argument.
>
> ```python
> >>> br4nch.export.branch(branch="MyBranch", directory="D:/MyOutput")
> # Path: D:\MyOutput\br4nch-MyBranch
> ```
>
> To also export the size, symbols and paint, set the `package` argument to `True`.
>
> ```python
> >>> br4nch.export.branch(branch="MyBranch", directory="D:/MyOutput", package=True)
> # Path: D:\MyOutput\br4nch-MyBranch
> ```
>
> To export multiple branches in the same function call, you can use a list for the `branch` argument.
>
> ```python
> >>> br4nch.export.branch(branch=["MyBranch", "Stream"], directory="D:/MyOutput")
> # Path: D:\MyOutput\br4nch-MyBranch
> # Path: D:\MyOutput\br4nch-Stream
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- *InstanceStringError*
- *InstanceBooleanError*
- *NotExistingBranchError*
- *NotExistingDirectoryError*

