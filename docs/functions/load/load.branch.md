# load.branch

To load an branch, use the **following function:**

> br4nch.**load**.**branch**(*branch*, *package=""*)

**Required argument(s):**

- branch - The exported branch file path.

**Optional argument(s):**

- package - The exported package file path.

**Guide:**

> To import an exported branch file, specify the path of the branch file in the `branch` argument.
>
> ```python
> >>> br4nch.load.branch(branch="D:/br4nch-MyBranch/branch-MyBranch")
> ```
>
> To also import an exported package file, specify the path of the package file in the `package` argument.
>
> ```python
> >>> br4nch.load.branch(branch="D:/br4nch-MyBranch/branch-MyBranch", package="D:/br4nch-MyBranch/package-MyBranch")
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- *InvalidBranchNameError*
- *InvalidBranchFileError*
- *InvalidPackageFileError*
- *NotExistingBranchFileError*
- *NotExistingPackageFileError*
- *DuplicateBranchError*
