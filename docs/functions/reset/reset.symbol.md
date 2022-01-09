# reset.symbol

To reset one or multiple symbol(s), use the **following function:**

> br4nch.**reset**.**symbol**(*branch*, *line=True*, *split=True*, *end=True*)

**Required arguments:**

- branch - This is the argument where you specify the branch(es) whose symbol(s) should be reset.

**Optional arguments:**

- line - If this argument is 'True', the line symbol is reset to the default line symbol.
- split - If this argument is 'True', the split symbol is reset to the default split symbol.
- end - If this argument is 'True', the end symbol is reset to the default end symbol.

Here's an example:

```python
>>> br4nch.reset.symbol(branch="MyBranch")
```

Here's an second example:

```python
>>> br4nch.reset.symbol(branch="MyBranch", line=False, end=False)
```

**Possible errors:**

These are the errors that may pop up when the function is used incorrectly. For more information about errors, head to [errors](../../guides/errors.md).

- InstanceStringError
- InstanceBooleanError
- NotExistingBranchError

