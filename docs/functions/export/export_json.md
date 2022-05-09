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
> ┃ˑˑ┣━ Manager
> ┃ˑˑ┃ˑˑ┗━ Ben
> ┃ˑˑ┗━ Scientists
> ┃ˑˑˑˑˑ┣━ Jerry
> ┃ˑˑˑˑˑ┗━ Hank
> ┗━ Information
> ˑˑˑ┣━ Temperature
> ˑˑˑ┃ˑˑ┗━ 44
> ˑˑˑ┗━ Statements
> ˑˑˑˑˑˑ┣━ Content
> ˑˑˑˑˑˑ┃ˑˑ┗━ None
> ˑˑˑˑˑˑ┣━ Overheat
> ˑˑˑˑˑˑ┃ˑˑ┗━ False
> ˑˑˑˑˑˑ┗━ Active
> ˑˑˑˑˑˑˑˑˑ┗━ True
> 
> >>> br4nch.export.Json(tree="MyData", output_folder="D:/MyOutput", data_types=False)
> # Path: D:/MyOutput/br4nch-MyData.json
> ```
>
> The content of the file that we exported to a json file.
>
> ***file:** "D:/br4nch-MyData.json"*
>
> ```json
> {
> ˑˑˑ"Users":{
> ˑˑˑˑˑˑ"Manager":"Ben",
> ˑˑˑˑˑˑ"Scientists":[
>    ˑˑˑˑˑˑˑˑˑ"Jerry",
>    ˑˑˑˑˑˑˑˑˑ"Hank"
> ˑˑˑˑˑˑ]
> ˑˑˑ},
> ˑˑˑ"Information":{
> ˑˑˑˑˑˑ"Temperature":"44",
> ˑˑˑˑˑˑ"Statements":{
>    ˑˑˑˑˑˑˑˑˑ"Content":"None",
>    ˑˑˑˑˑˑˑˑˑ"Overheat":"False",
>    ˑˑˑˑˑˑˑˑˑ"Active":"True"
> ˑˑˑˑˑˑ}
> ˑˑˑ}
> }
> ```
>

> If there is a duplicate node in the tree, a number is added to each duplicate node in the json file.
>
> ```json
> {
> ˑˑˑ"Test#1":[
> ˑˑˑˑˑˑ"ABC",
> ˑˑˑˑˑˑ123
> ˑˑˑ],
> ˑˑˑ"Test#2":[
> ˑˑˑˑˑˑ"Hey",
> ˑˑˑˑˑˑ"Hai"
> ˑˑˑ]
> }
> ```
>

> To convert the python 'string data types' to 'json data types' in the json file, set the `data_types` argument to `True`.
>
> ```python
> >>> br4nch.display.Tree(tree="MyData")
> Database
> ┣━ Users
> ┃ˑˑ┣━ Manager
> ┃ˑˑ┃ˑˑ┗━ Ben
> ┃ˑˑ┗━ Scientists
> ┃ˑˑˑˑˑ┣━ Jerry
> ┃ˑˑˑˑˑ┗━ Hank
> ┗━ Information
> ˑˑˑ┣━ Temperature
> ˑˑˑ┃ˑˑ┗━ 44
> ˑˑˑ┗━ Statements
> ˑˑˑˑˑˑ┣━ Content
> ˑˑˑˑˑˑ┃ˑˑ┗━ None
> ˑˑˑˑˑˑ┣━ Overheat
> ˑˑˑˑˑˑ┃ˑˑ┗━ False
> ˑˑˑˑˑˑ┗━ Active
> ˑˑˑˑˑˑˑˑˑ┗━ True
> 
> >>> br4nch.export.Json(tree="MyData", output_folder="D:/MyOutput", data_types=False)
> # Path: D:/MyOutput/br4nch-MyData.json
> ```
>
> The content of the file that we exported to a json file.
>
> ***file:** "D:/br4nch-MyData.json"*
>
> ```json
> {
> ˑˑˑ"Users":{
> ˑˑˑˑˑˑ"Manager":"Ben",
> ˑˑˑˑˑˑ"Scientists":[
> ˑˑˑˑˑˑˑˑˑ"Jerry",
> ˑˑˑˑˑˑˑˑˑ"Hank"
> ˑˑˑˑˑˑ]
> ˑˑˑ},
> ˑˑˑ"Information":{
> ˑˑˑˑˑˑ"Temperature":44,
> ˑˑˑˑˑˑ"Statements":{
> ˑˑˑˑˑˑˑˑˑ"Content":null,
> ˑˑˑˑˑˑˑˑˑ"Overheat":false,
> ˑˑˑˑˑˑˑˑˑ"Active":true
> ˑˑˑˑˑˑ}
> ˑˑˑ}
> }
> ```
>

> To export multiple trees to a json file in the same function call, you can use a list for the `tree` argument.
>
> ```python
> >>> br4nch.export.Json(tree=["MyData", "Stream"], output_folder="D:/MyOutput")
> # Path: D:/MyOutput/br4nch-MyData.json
> # Path: D:/MyOutput/br4nch-Stream.json
> ```
>

> To export the output in multiple folders in the same function call, you can use a list for the `output_folder` argument.
>
> ```python
> >>> br4nch.export.Json(tree="MyData", output_folder=["D:/MyOutput", "D:/DataOutput"])
> # Path: D:/MyOutput/br4nch-MyData.json
> # Path: D:/DataOutput/br4nch-MyData.json
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- InstanceStringError
- InstanceBooleanError
- NotExistingTreeError
- NotExistingDirectoryError

