# delete.branch

To delete a branch, use the **following function:**

> br4nch.**delete**.**branch**(*branch*)

---

**Required argument(s):**

- *branch* - The name of the branch(es) that will be deleted.

---

**Argument(s) supporting a list:**
Every argument in here supports a list.
Example: *branch=["MyFirstBranch", "MySecondBranch"]*

- *branch*

---

**Here's an example of the minimum/required arguments for this function:**

```python
# Deletes the branch 'MyBranch'.
>>> br4nch.delete.branch(branch="MyBranch")
```

---

**Here's an example for beginners:**

```python
# To delete a branch, specify the name of the branch in the branch argument.
>>> br4nch.delete.branch(branch="MyBranch")

# You can also delete multiple branches at once by making a list and specifying it in the branch argument.
>>> br4nch.delete.branch(branch=["BranchOne", "BranchTwo"])
```

---

**Here's an example when the function is used in a real situation:**

```python
# Creates the 'Board' branch.
>>> br4nch.create.branch(branch="Board", header="Information")

# Creates multiple layers in the 'Board' branch.
>>> br4nch.create.layer(branch="Board", layer=["Animals", "Food"], position="0")
>>> br4nch.create.layer(branch="Board", layer=["Dog", "Cat"], position="1")
>>> br4nch.create.layer(branch="Board", layer="Bread", position="2")

# Prints the 'Board' branch.
>>> br4nch.display.branch(branch="Board")
Information
┣━ Animals
┃  ┣━ Dog
┃  ┗━ Cat
┗━ Food
   ┗━ Bread

# Deletes the branch 'Board'.
>>> br4nch.delete.branch(branch="Board")

# Prints the 'Board' branch.
>>> br4nch.display.branch(branch="Board")
NotExistingBranchError: The branch: 'Board' does not exists.
```

---

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
For more information about errors, head to [errors](../../guides/errors.md).

- InstanceStringError
- NotExistingBranchError

---
