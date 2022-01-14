# delete.layer

To delete an layer, use the **following function:**

> br4nch.**delete**.**layer**(*branch*, *position*)

---

**Required argument(s):**
For more information about positions, head to [positions](../../guides/positions.md).

- *branch* - The name of the branch(es) to which the layer will be deleted.
- *position* - The position(s) where the layer(s) will be deleted.*

---

**Argument(s) supporting a list:**
Every argument in here supports a list.
Example: *position=["1.1", "2.2", "2.3"]*

- *branch*
- *position*

---

**Here's an example of the minimum/required arguments for this function:**

```python
# Deletes the layer attatched to the position '1' in the branch 'MyBranch'.
>>> br4nch.delete.layer(branch="MyBranch", position="1")
```

**Here's an example for beginners:**

```python
>>> br4nch.display.branch(branch="Board")
Information
┣━ Animals
┃  ┣━ Dog
┃  ┗━ Cat
┗━ Food
   ┗━ Bread
    
# To delete a layer, specify the position linked to the layer you want to delete.
>>> br4nch.delete.layer(branch="Board", position="1")

>>> br4nch.display.branch(branch="Board")
Information
┗━ Food
   ┗━ Bread
```

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

# Deletes the layer attatched to the position '1' in the branch 'Board'.
>>> br4nch.delete.layer(branch="Board", position="1")

# Prints the 'Board' branch.
>>> br4nch.display.branch(branch="Board")
Information
┗━ Food
   ┗━ Bread
```

---

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
For more information about errors, head to [errors](../../guides/errors.md).

- InstanceStringError
- InvalidPositionError
- NotExistingBranchError

---

