# create.branch

To create a new branch, use the **following function:**

> br4nch.**create**.**branch**(*branch*, *header*)

---

**Required argument(s):**

- *branch* - The name of the new branch(es) that will be created.
- *header* - The header name for the branch.

---

**Argument(s) supporting a list:**
Every argument in here supports a list.
Example: *branch=["MyFirstBranch", "MySecondBranch"]*

- *branch*

---

**Here's an example of the minimum/required argument(s) for this function:**

```python
# Creates the branch 'MyBranch' and the header 'MyHeader'.
>>> br4nch.create.branch(branch="MyBranch", header="MyHeader")
```

**Here's an example for beginners:**

```python
# To create a branch you need to name the branch, we name the branch 'MyBranch'. You also have to create a header, we name the header 'My custom header!'.
>>> br4nch.create.branch(branch="MyBranch", header="My custom header!")

# You can also create multiple branches at once by making a list and specifying it in the branch argument.
>>> br4nch.create.branch(branch=["BranchOne", "BranchTwo"], header="MyHeader")
```

---

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
For more information about errors, head to [errors](../../guides/errors.md).

- InstanceStringError

- InvalidBranchNameError
- NotExistingBranchError
- DuplicateBranchError

---

