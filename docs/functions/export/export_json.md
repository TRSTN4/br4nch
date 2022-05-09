# export.Json

To export a tree structure to a json file, use the **following function:**

> br4nch.**export**.**Json**(*tree*, *output_folder*, *data_types=False*)

**Required argument(s):**

- *tree* - The tree that will be exported to a json file.
- *output_folder* - The output directory for the json file.

**Optional argument(s):**

- *data_types* - If this argument is True, then the 'string data types' will be converted into 'json data types'.

**Guide:**

> To export the structure of a tree into a json structure and export it to a json file, use the `tree` argument to specify the tree you want to format and the output location in the `output_folder` argument.
>
> ```python
> >>> br4nch.display.Tree(tree="MyData")
> Database
> ┣━ Users
> ┃  ┣━ Manager
> ┃  ┃  ┗━ Ben
> ┃  ┗━ Scientists
> ┃     ┣━ Jerry
> ┃     ┗━ Hank
> ┗━ Information
>    ┣━ Temperature
>    ┃  ┗━ 44
>    ┗━ Statements
>       ┣━ Content
>       ┃  ┗━ None
>       ┣━ Overheat
>       ┃  ┗━ False
>       ┗━ Active
>          ┗━ True
> 
> >>> br4nch.export.Json(tree="MyData", output_folder="D:/", data_types=False)
> # Path: D:/br4nch-MyData.json
> ```
>
> The content of the file that we exported to a json file.
>
> ***file:** "D:/br4nch-MyData.json"*
>
> ```json
> {
>     "Users": {
>         "Manager": "Ben",
>         "Scientists": [
>             "Jerry",
>             "Hank"
>         ]
>     },
>     "Information": {
>         "Temperature": "44",
>         "Statements": {
>             "Content": "None",
>             "Overheat": "False",
>             "Active": "True"
>         }
>     }
> }
> ```
>
> To convert the python 'string data types' to 'json data types' in the json file, set the `data_types` argument to `True`.
>
> ```python
> >>> br4nch.display.Tree(tree="MyData")
> Database
> ┣━ Users
> ┃  ┣━ Manager
> ┃  ┃  ┗━ Ben
> ┃  ┗━ Scientists
> ┃     ┣━ Jerry
> ┃     ┗━ Hank
> ┗━ Information
>    ┣━ Temperature
>    ┃  ┗━ 44
>    ┗━ Statements
>       ┣━ Content
>       ┃  ┗━ None
>       ┣━ Overheat
>       ┃  ┗━ False
>       ┗━ Active
>          ┗━ True
> 
> >>> br4nch.export.Json(tree="MyData", output_folder="D:/", data_types=False)
> # Path: D:/br4nch-MyData.json
> ```
>
> The content of the file that we exported to a json file.
>
> ***file:** "D:/br4nch-MyData.json"*
>
> ```json
> {
>     "Users": {
>         "Manager": "Ben",
>         "Scientists": [
>             "Jerry",
>             "Hank"
>         ]
>     },
>     "Information": {
>         "Temperature": 44,
>         "Statements": {
>             "Content": null,
>             "Overheat": false,
>             "Active": true
>         }
>     }
> }
> ```
>
> To export multiple trees to a json file in the same function call, you can use a list for the `tree` argument.
>
> ```python
> >>> br4nch.export.Json(tree=["MyData", "Stream"], output_folder="D:/")
> # Path: D:/br4nch-MyData.json
> # Path: D:/br4nch-Stream.json
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- InstanceStringError
- InstanceBooleanError
- NotExistingTreeError
- NotExistingDirectoryError

