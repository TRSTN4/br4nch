# export.txt

To export the branch output to an txt file, use the **following function:**

> br4nch.**export**.**txt**(*branch*, *directory*)

**Required argument(s):**

- branch - The branch that will be exported to an txt file.
- directory  - The output directory for the txt file.

**Guide:**

> To export the output of the branch to a txt file, specify the branch in the `branch` argument and specify the path to export the file to in the `directory` argument.
>
> ```python
> >>> br4nch.export.txt(branch="MyBranch", directory="D:/MyOutput")
> # Path: D:/br4nch-MyBranch.txt
> ```
>
> To export multiple branches to an txt file in the same function call, you can use a list for the `branch` argument.
>
> ```python
> >>> br4nch.export.txt(branch=["MyBranch", "Stream"], directory="D:/MyOutput")
> # Path: D:\MyOutput\br4nch-MyBranch
> # Path: D:\MyOutput\br4nch-Stream
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
For more information about errors, head to [errors](../../guides/errors.md).

- *InstanceStringError*
- *NotExistingBranchError*
- *NotExistingDirectoryError*

