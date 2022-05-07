#  Errors

## InstanceStringError

This error occurs when the given value in the specified argument is not an instance of a string.

**This error occurs in the following functions:**

[create.Tree](../functions/create/create_tree.md), [create.Node](../functions/create/create_node.md), [delete.Tree](../functions/delete/delete_tree.md), [delete.Node](../functions/delete/delete_node.md), [display.Tree](../functions/display/display_tree.md), [display.Assist](../functions/display/display_assist.md), [duplicate.Tree](../functions/duplicate/duplicate_tree.md), [duplicate.Node](../functions/duplicate/duplicate_node.md), [export.Tree](../functions/export/export_tree.md), [export.Text](../functions/export/export_text.md), [get.Tree](../functions/get/get_tree.md), [get.Node](../functions/get/get_node.md), [get.Position](../functions/get/get_position.md), [load.Folder](../functions/load/load_folder.md), [load.Json](../functions/load/load_json.md), [load.Tree](../functions/load/load_tree.md), [move.Node](../functions/move/move_node.md), [replace.Tree](../functions/replace/replace_tree.md), [replace.Header](../functions/replace/replace_header.md), [replace.Node](../functions/replace/replace_node.md), [reset.Symbol](../functions/reset/reset_symbol.md), [reset.Size](../functions/reset/reset_size.md), [set.Symbol](../functions/set/set_symbol.md), [set.Size](../functions/set/set_size.md)

**Example:**

> ```python
> >>> br4nch.add.Tree(tree=123, header="MyHeader")
> InstanceStringError: The tree argument: '123' must be an instance of a 'string' and not 'int'.
> ```
>

## InstanceBooleanError

This error occurs when the given value in the specified argument is not an instance of a boolean.

**This error occurs in the following functions:**

[display.Tree](../functions/display/display_tree.md), [duplicate.Tree](../functions/duplicate/duplicate_tree.md), [duplicate.Node](../functions/duplicate/duplicate_node.md), [export.Tree](../functions/export/export_tree.md), [get.Tree](../functions/get/get_tree.md), [get.Node](../functions/get/get_node.md), [get.Position](../functions/get/get_position.md), [load.Folder](../functions/load/load_folder.md), [reset.Symbol](../functions/reset/reset_symbol.md)

**Example:**

> ```python
> >>> br4nch.duplicate.Tree(new_tree="MyBranch", target_tree="MyHeader", attributes=123)
> InstanceBooleanError: The attributes argument: '123' must be an instance of a 'boolean'  and not 'int'.
> ```
>

## InstanceIntegerError

This error occurs when the given value in the specified argument is not an instance of a integer.

**This error occurs in the following function:**

[set.Size](../functions/set/set_size.md)

**Example:**

> ```python
> >>> br4nch.set.Size(tree="MyTree", size="123")
> InstanceIntegerError: The size argument: '123' must be an instance of a 'integer' and not 'str'.
> ```
>

## InvalidTreeNameError

This error occurs when the tree name uses characters other than letters and/or numbers.

**This error occurs in the following functions:**

[create.Tree](../functions/create/create_tree.md), [duplicate.Tree](../functions/duplicate/duplicate_tree.md), [load.Folder](../functions/load/load_folder.md), [load.Json](../functions/load/load_json.md), [replace.Tree](../functions/replace/replace_tree.md)

**Example:**

> ```python
> >>> br4nch.add.Tree(tree="%", header="MyHeader")
> InvalidTreeNameError: The tree name: '%' is not valid. Only numbers and/or letters may be used to add a tree.
> ```
>

## InvalidPositionError

This error occurs when the given position contains a character other than valid positions, operators and existing nodes.

**This error occurs in the following functions:**

[create.Node](../functions/create/create_node.md), [delete.Node](../functions/delete/delete_node.md), [duplicate.Node](../functions/duplicate/duplicate_node.md), [get.Position](../functions/get/get_position.md), [move.Node](../functions/move/move_node.md), [replace.Node](../functions/replace/replace_node.md)

**Example:**

> ```python
> >>> br4nch.add.Node(tree="MyTree", node="MyNode", parent="%")
> InvalidPositionError: The position: '#' is not valid. Only valid positions, operators and existing nodes  can be used to decide the position for the parent argument.
> ```
>

## InvalidSizeError

This error occurs when the given size is less than zero or greater than 20.

**This error occurs in the following function:**

[set.Size](../functions/set/set_size.md)

**Example:**

> ```python
> >>> br4nch.set.Size(tree="MyTree", size=21)
> InvalidSizeError: The sizes that can be used is '0-20'.
> ```
>

## InvalidTreeFileError

This error occurs when the specified tree file is invalid.

**This error occurs in the following function:**

[load.Tree](../functions/load/load_tree.md)

**Example:**

> ```python
> >>> br4nch.load.Tree(tree_file="D:/ThisBranchFileIsNotValid")
> InvalidTreeFileError: The file: 'D:/ThisBranchFileIsNotValid' is not valid as a branch file.
> ```
>

## InvalidAttributesFileError

This error occurs when the specified attributes file is invalid.

**This error occurs in the following function:**

[load.Tree](../functions/load/load_tree.md)

**Example:**

> ```python
> >>> br4nch.load.Tree(tree_file="D:/ThisBranchFileDoesNotExists", attributes_file="D:/ThisPackageFileIsNotValid")
> InvalidAttributesFileError: The file: 'D:/ThisPackageFileIsNotValid' is not valid as a package file.
> ```
>

## NotExistingTreeError

This error occurs when the specified tree does not exist.

**This error occurs in the following functions:**

[create.Node](../functions/create/create_node.md), [delete.Tree](../functions/delete/delete_tree.md), [delete.Node](../functions/delete/delete_node.md), [display.Tree](../functions/display/display_tree.md), [display.Assist](../functions/display/display_assist.md), [duplicate.Tree](../functions/duplicate/duplicate_tree.md), [duplicate.Node](../functions/duplicate/duplicate_node.md), [export.Tree](../functions/export/export_tree.md), [export.Text](../functions/export/export_text.md), [get.Node](../functions/get/get_node.md), [get.Position](../functions/get/get_position.md), [move.Node](../functions/move/move_node.md), [replace.Tree](../functions/replace/replace_tree.md), [replace.Header](../functions/replace/replace_header.md), [replace.Node](../functions/replace/replace_node.md), [reset.Symbol](../functions/reset/reset_symbol.md), [reset.Size](../functions/reset/reset_size.md), [set.Symbol](../functions/set/set_symbol.md), [set.Size](../functions/set/set_size.md)

**Example:**

> ```python
> >>> br4nch.add.Node(tree="MyNotExistingBranch", node="MyNode", position="Test")
> NotExistingTreeError: The tree: 'MyNotExistingBranch' does not exists.
> ```
>

## NotExistingDirectoryError

This error occurs when the given directory does not exist.

**This error occurs in the following functions:**

[export.Tree](../functions/export/export_tree.md), [export.Text](../functions/export/export_text.md), [load.Folder](../functions/load/load_folder.md)

**Example:**

> ```python
> >>> br4nch.export.Tree(tree="MyTree", output_folder="D:ThisDirectoryDoesNotExists")
> NotExistingDirectoryError: The directory: 'D:ThisDirectoryDoesNotExists' does not exist.
> ```
>

## NotExistingTreeFileError

This error occurs when the specified tree file location does not exist.

**This error occurs in the following function:**

[load.Tree](../functions/load/load_tree.md)

**Example:**

> ```python
> >>> br4nch.load.Tree(tree_file="D:/ThisBranchFileDoesNotExists")
> NotExistingTreeFileError: The branch file: 'D:/ThisBranchFileDoesNotExists!' does not exist.
> ```
>

## NotExistingAttributesFileError

This error occurs when the specified attributes file location does not exist.

**This error occurs in the following function:**

[load.Tree](../functions/load/load_tree.md)

**Example:**

> ```python
> >>> br4nch.load.Tree(tree_file="D:/br4nch-MyTree/tree-MyTree.br4nch", attributes_file="ThisPackageFileDoesNotExists!")
> NotExistingAttributesFileError: The attributes file: 'ThisPackageFileDoesNotExists!' does not exist.
> ```
>

## NotExistingJsonFileError

This error occurs when the specified json file location does not exist.

**This error occurs in the following function:**

[load.Json](../functions/load/load_json.md)

**Example:**

> ```python
> >>> br4nch.load.Json(tree_name="MyJsonTree", header="Json Tree", json_file="ThisJsonFileDoesNotExists!"))
> NotExistingJsonFileError: The json file: 'ThisJsonFileDoesNotExists!' does not exist.
> ```

## NotSizeableError

This error occurs when you use the function with modified symbols.

**This error occurs in the following function:**

[set.Size](../functions/set/set_size.md)

**Example:**

> ```python
> >>> br4nch.set.Size(tree="MyTree", size=2)
> NotSizeableError: You can only use the 'size' function with the default symbols.
> ```

## DuplicateTreeError

This error occurs when the specified tree name already exists.

**This error occurs in the following functions:**

[create.Tree](../functions/create/create_tree.md), [duplicate.Tree](../functions/duplicate/duplicate_tree.md), [load.Folder](../functions/load/load_folder.md), [load.Json](../functions/load/load_json.md), [load.Tree](../functions/load/load_tree.md), [replace.Tree](../functions/replace/replace_tree.md)

**Example:**

> ```python
> >>> br4nch.create.Tree(tree="MyTree", header="MyHeader")
> DuplicateTreeError: The tree: 'MyTree' already exists.
> ```
>

## RequiredSymbolChangeError

This error occurs when no symbols are changed.

**This error occurs in the following function:**

[set.Symbol](../functions/set/set_symbol.md)

**Example:**

> ```python
> >>> br4nch.set.Symbol(tree="MyTree")
> RequiredSymbolChangeError: Change at least one of the given symbols: 'line', 'split' or 'end'.
> ```
>

