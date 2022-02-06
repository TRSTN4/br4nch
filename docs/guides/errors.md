#  Errors

## InstanceStringError

This error occurs when the given value in the specified argument is not an instance of a string.

**This error occurs in the following functions:**

[add.branch](../functions/add/add.branch.md), [add.layer](../functions/add/add.layer.md), [duplicate.branch](../functions/duplicate/duplicate.branch.md), [duplicate.layer](../functions/duplicate/duplicate.layer.md), [move.layer](../functions/move/move.layer.md), [replace.branch](../functions/replace/replace.branch.md), [replace.header](../functions/replace/replace.header.md), [replace.layer](../functions/replace/replace.layer.md), [delete.branch](../functions/delete/delete.branch.md), [delete.layer](../functions/delete/delete.layer.md), [set.size](../functions/set/set.size.md), [set.symbol](../functions/set/set.symbol.md), [set.paint.branch](../functions/set/paint/set.paint.branch.md), [set.paint.header](../functions/set/paint/set.paint.header.md), [set.paint.layer](../functions/set/paint/set.paint.layer.md), [reset.size](../functions/reset/reset.size.md), [reset.symbol](../functions/reset/reset.symbol.md), [reset.paint.branch](../functions/reset/paint/reset.paint.branch.md), [reset.paint.header](../functions/reset/paint/reset.paint.header.md), [reset.paint.layer](../functions/reset/paint/reset.paint.layer.md), [export.branch](../functions/export/export.branch.md), [export.txt](../functions/export/export.txt.md), [display.assist](../functions/display/display.assist.md), [display.branch](../functions/display/display.branch.md), [display.layer](../functions/display/display.layer.md), [display.position](../functions/display/display.position.md)

Here's an example:

```python
>>> br4nch.add.branch(branch=123, header="MyHeader")
InstanceStringError: The branch argument: '123' must be an instance of a 'string' and not 'int'.
```

## InstanceBooleanError

This error occurs when the given value in the specified argument is not an instance of a boolean.

**This error occurs in the following functions:**

[duplicate.branch](../functions/duplicate/duplicate.branch.md), [duplicate.layer](../functions/duplicate/duplicate.layer.md), [move.layer](../functions/move/move.layer.md), [reset.symbol](../functions/reset/reset.symbol.md), [export.branch](../functions/export/export.branch.md), [display.branch](../functions/display/display.branch.md), [display.layer](../functions/display/display.layer.md), [display.position](../functions/display/display.position.md)

Here's an example:

```python
>>> br4nch.duplicate.branch(branch="MyBranch", name="MyHeader", package=123)
InstanceBooleanError: The package argument: '123' must be an instance of a 'boolean'  and not 'int'.
```

## InstanceIntegerError

This error occurs when the given value in the specified argument is not an instance of a integer.

**This error occurs in the following functions:**

[set.size](../functions/set/set.size.md), [display.assist](../functions/display/display.assist.md)

Here's an example:

```python
>>> br4nch.set.size(branch="MyBranch", size="123")
InstanceIntegerError: The size argument: '123' must be an instance of a 'integer' and not 'str'.
```

## InvalidBranchNameError

This error occurs when the branch name uses characters other than letters and/or numbers.

**This error occurs in the following functions:**

[add.branch](../functions/add/add.branch.md), [replace.branch](../functions/replace/replace.branch.md), [load.branch](../functions/load/load.branch.md)

Here's an example:

```python
>>> br4nch.add.branch(branch="#MyBranch#", header="MyHeader")
InvalidBranchNameError: The branch name: '#MyBranch#' is not valid. Only numbers and/or letters may be used to add a branch.
```

## InvalidPositionError

This error occurs when the given position contains a character other than a number and/or operator.

**This error occurs in the following functions:**

[add.layer](../functions/add/add.layer.md), [duplicate.layer](../functions/duplicate/duplicate.layer.md), [move.layer](../functions/move/move.layer.md), [replace.layer](../functions/replace/replace.layer.md), [delete.layer](../functions/delete/delete.layer.md), [set.paint.layer](../functions/set/paint/set.paint.layer.md), [reset.paint.layer](../functions/reset/paint/reset.paint.layer.md), [display.position](../functions/display/display.position.md)

Here's an example:

```python
>>> br4nch.add.layer(branch="MyBranch", layer="MyLayer", position="#")
InvalidPositionError: The position: '#' is not valid. Only numbers and operators may be used to add a position to the pos argument.
```

## InvalidSizeError

This error occurs when the given size is less than zero or greater than 20.

**This error occurs in the following functions:**

[set.size](../functions/set/set.size.md), [display.assist](../functions/display/display.assist.md)

Here's an example:

```python
>>> br4nch.set.size(branch="MyBranch", size=21)
InvalidSizeError: The sizes that can be used is '0-20'.
```

## InvalidBranchFileError

This error occurs when the specified branch file is invalid. e.g. the file is missing an official br4nch ID.

**This error occurs in the following function:**

[load.branch](../functions/load/load.branch.md)

Here's an example:

```python
>>> br4nch.load.branch(branch="D:/ThisBranchFileIsNotValid")
InvalidBranchFileError: The file: 'D:/ThisBranchFileIsNotValid' is not valid as a branch file.
```

## InvalidPackageFileError

This error occurs when the specified package file is invalid. e.g. the file is missing an official br4nch ID.

**This error occurs in the following function:**

[load.branch](../functions/load/load.branch.md)

Here's an example:

```python
>>> br4nch.load.branch(branch="D:/branch-MyBranch", package="D:/ThisPackageFileIsNotValid")
InvalidPackageFileError: The file: 'D:/ThisPackageFileIsNotValid' is not valid as a package file.
```

## NotExistingBranchError

This error occurs when the specified branch does not exist.

**This error occurs in the following functions:**

[add.branch](../functions/add/add.branch.md), [add.layer](../functions/add/add.layer.md), [duplicate.branch](../functions/duplicate/duplicate.branch.md), [duplicate.layer](../functions/duplicate/duplicate.layer.md), [move.layer](../functions/move/move.layer.md), [replace.branch](../functions/replace/replace.branch.md), [replace.header](../functions/replace/replace.header.md), [replace.layer](../functions/replace/replace.layer.md), [delete.branch](../functions/delete/delete.branch.md), [delete.layer](../functions/delete/delete.layer.md), [set.size](../functions/set/set.size.md), [set.symbol](../functions/set/set.symbol.md), [set.paint.branch](../functions/set/paint/set.paint.branch.md), [set.paint.header](../functions/set/paint/set.paint.header.md), [set.paint.layer](../functions/set/paint/set.paint.layer.md), [reset.size](../functions/reset/reset.size.md), [reset.symbol](../functions/reset/reset.symbol.md), [reset.paint.branch](../functions/reset/paint/reset.paint.branch.md), [reset.paint.header](../functions/reset/paint/reset.paint.header.md), [reset.paint.layer](../functions/reset/paint/reset.paint.layer.md), [export.branch](../functions/export/export.branch.md), [export.txt](../functions/export/export.txt.md), [display.assist](../functions/display/display.assist.md), [display.branch](../functions/display/display.branch.md), [display.layer](../functions/display/display.layer.md), [display.position](../functions/display/display.position.md)

Here's an example:

```python
>>> br4nch.add.layer(branch="D:/MyNotExistingBranch", layer="MyLayer", position="0")
NotExistingBranchError: The branch: 'MyNotExistingBranch' does not exists.
```

## NotExistingDirectoryError

This error occurs when the given directory does not exist.

**This error occurs in the following functions:**

[export.branch](../functions/export/export.branch.md), [export.txt](../functions/export/export.txt.md)

Here's an example:

```python
>>> br4nch.export.branch(branch="MyBranch", directory="D:ThisDirectoryDoesNotExists")
NotExistingDirectoryError: The directory: 'D:ThisDirectoryDoesNotExists' does not exist.
```

## NotExistingBranchFileError

This error occurs when the specified branch file location does not exist.

**This error occurs in the following function:**

[load.branch](../functions/load/load.branch.md)

Here's an example:

```python
>>> br4nch.load.branch(branch="D:/ThisBranchFileDoesNotExists")
NotExistingBranchFileError: The branch file: 'D:/ThisBranchFileDoesNotExists!' does not exist.
```

## NotExstingPackageFileError

This error occurs when the specified package file location does not exist.

**This error occurs in the following function:**

[load.branch](../functions/load/load.branch.md)

Here's an example:

```python
>>> br4nch.load.branch(branch="D:/branch-MyBranch", package="ThisPackageFileDoesNotExists!")
NotExistingPackageFileError: The package file: 'ThisPackageFileDoesNotExists!' does not exist.
```

## NotExistingPaintError

This error occurs when the specified paint does not exist.

**This error occurs in the following functions:**

[set.paint.branch](../functions/set/paint/set.paint.branch.md), [set.paint.header](../functions/set/paint/set.paint.header.md), [set.paint.layer](../functions/set/paint/set.paint.layer.md)

Here's an example:

```python
>>> br4nch.set.paint.branch(branch="MyBranch", paint="RandomColor")
NotExistingPaintError: The paint: 'RandomColor' does not exists.
```

## MaximumPaintSlotsError

This error occurs when more than three paint slots are used

**This error occurs in the following functions:**

[set.paint.branch](../functions/set/paint/set.paint.branch.md), [set.paint.header](../functions/set/paint/set.paint.header.md), [set.paint.layer](../functions/set/paint/set.paint.layer.md)

Here's an example:

```python
>>> br4nch.set.paint.branch(branch="MyBranch", paint=["red", "yellow", "green", "cyan"])
MaximumPaintSlotsError: The maximum paint slots that can be used is '3'.
```

## DuplicateBranchError

This error occurs when the specified branch name already exists.

**This error occurs in the following functions:**

[add.branch](../functions/add/add.branch.md), [replace.branch](../functions/replace/replace.branch.md), [load.branch](../functions/load/load.branch.md)

Here's an example:

```python
>>> br4nch.add.branch(branch="MyBranch", header="MyHeader2")
DuplicateBranchError: The branch: 'MyBranch' already exists.
```

## RequiredSymbolCangeError

This error occurs when no symbols are changed.

**This error occurs in the following function:**

[set.symbol](../functions/set/set.symbol.md)

Here's an example:

```python
>>> br4nch.set.symbol(branch="Database")
RequiredSymbolChangeError: Change at least one of the given symbols: 'line', 'split' or 'end'.
```

