# load.Json

To load a json file, use the **following function:**

> br4nch.**load**.**Json**(*new_tree*, *header*, *json_file*)

**Required argument(s):**

- *new_tree* - The name for the new tree(s) that will be created for the imported json file.
- *header* - The header name for the tree(s).
- *json_file* - The path of the json file that will be imported.

**Guide:**

> The content of the file that we are going to display in a tree structure.
>
> ***file:** "d:/JsonFile.json"*
>
> ```json
> {
>    "widget":{
>       "debug":"on",
>       "window":{
>          "title":"Sample Konfabulator Widget",
>          "name":"main_window",
>          "width":500,
>          "height":500
>       },
>       "image":{
>          "src":"Images/Sun.png",
>          "name":"sun1",
>          "hOffset":250,
>          "vOffset":250,
>          "alignment":"center"
>       },
>       "text":{
>          "data":"Click Here",
>          "size":36,
>          "style":"bold",
>          "name":"text1",
>          "hOffset":250,
>          "vOffset":100,
>          "alignment":"center",
>          "onMouseUp":"sun1.opacity = (sun1.opacity / 100) * 90;"
>       }
>    }
> }
> ```
>
> To display the json content in a tree form, specify the name of the tree in the `new_tree` argument, the header name in the `header` argument and final the json file path in the `json_file` argument.
>
> ```python
> >>> br4nch.load.Json(new_tree="JsonTree", header="My Json Tree", json_file="d:/JsonFile.json")
> 
> >>> br4nch.display.Tree(tree="JsonTree")
> My Json Tree
> ┗━ widget
> ˑˑˑ┣━ image
> ˑˑˑ┃ˑˑ┣━ src
> ˑˑˑ┃ˑˑ┃ˑˑ┗━ Images/Sun.png
> ˑˑˑ┃ˑˑ┣━ name
> ˑˑˑ┃ˑˑ┃ˑˑ┗━ sun1
> ˑˑˑ┃ˑˑ┣━ hOffset
> ˑˑˑ┃ˑˑ┃ˑˑ┗━ 250
> ˑˑˑ┃ˑˑ┣━ vOffset
> ˑˑˑ┃ˑˑ┃ˑˑ┗━ 250
> ˑˑˑ┃ˑˑ┗━ alignment
> ˑˑˑ┃ˑˑˑˑˑ┗━ center
> ˑˑˑ┗━ text
> ˑˑˑˑˑˑ┣━ data
> ˑˑˑˑˑˑ┃ˑˑ┗━ Click Here
> ˑˑˑˑˑˑ┣━ size
> ˑˑˑˑˑˑ┃ˑˑ┗━ 36
> ˑˑˑˑˑˑ┣━ style
> ˑˑˑˑˑˑ┃ˑˑ┗━ bold
> ˑˑˑˑˑˑ┣━ name
> ˑˑˑˑˑˑ┃ˑˑ┗━ text1
> ˑˑˑˑˑˑ┣━ hOffset
> ˑˑˑˑˑˑ┃ˑˑ┗━ 250
> ˑˑˑˑˑˑ┣━ vOffset
> ˑˑˑˑˑˑ┃ˑˑ┗━ 100
> ˑˑˑˑˑˑ┣━ alignment
> ˑˑˑˑˑˑ┃ˑˑ┗━ center
> ˑˑˑˑˑˑ┗━ onMouseUp
> ˑˑˑˑˑˑˑˑˑ┗━ sun1.opacity = (sun1.opacity / 100) * 90;
> ```
>
> To load multiple trees with the json content in the same function call, you can use a list for the `new_tree` argument.
>
> ```python
> >>> br4nch.load.Json(new_tree=["FirstTree", "SecondTree"], header="My Json Tree", json_file="d:/JsonFile.json")
> 
> >>> br4nch.display.Tree(tree=["FirstTree", "SecondTree"])
> My Json Tree
> ┗━ widget
> ˑˑˑ┣━ image
> ˑˑˑ┃ˑˑ┣━ src
> ˑˑˑ┃ˑˑ┃ˑˑ┗━ Images/Sun.png
> ˑˑˑ┃ˑˑ┣━ name
> ˑˑˑ┃ˑˑ┃ˑˑ┗━ sun1
> ˑˑˑ┃ˑˑ┣━ hOffset
> ˑˑˑ┃ˑˑ┃ˑˑ┗━ 250
> ˑˑˑ┃ˑˑ┣━ vOffset
> ˑˑˑ┃ˑˑ┃ˑˑ┗━ 250
> ˑˑˑ┃ˑˑ┗━ alignment
> ˑˑˑ┃ˑˑˑˑˑ┗━ center
> ˑˑˑ┗━ text
> ˑˑˑˑˑˑ┣━ data
> ˑˑˑˑˑˑ┃ˑˑ┗━ Click Here
> ˑˑˑˑˑˑ┣━ size
> ˑˑˑˑˑˑ┃ˑˑ┗━ 36
> ˑˑˑˑˑˑ┣━ style
> ˑˑˑˑˑˑ┃ˑˑ┗━ bold
> ˑˑˑˑˑˑ┣━ name
> ˑˑˑˑˑˑ┃ˑˑ┗━ text1
> ˑˑˑˑˑˑ┣━ hOffset
> ˑˑˑˑˑˑ┃ˑˑ┗━ 250
> ˑˑˑˑˑˑ┣━ vOffset
> ˑˑˑˑˑˑ┃ˑˑ┗━ 100
> ˑˑˑˑˑˑ┣━ alignment
> ˑˑˑˑˑˑ┃ˑˑ┗━ center
> ˑˑˑˑˑˑ┗━ onMouseUp
> ˑˑˑˑˑˑˑˑˑ┗━ sun1.opacity = (sun1.opacity / 100) * 90;
> My Json Tree
> ┗━ widget
> ˑˑˑ┣━ image
> ˑˑˑ┃ˑˑ┣━ src
> ˑˑˑ┃ˑˑ┃ˑˑ┗━ Images/Sun.png
> ˑˑˑ┃ˑˑ┣━ name
> ˑˑˑ┃ˑˑ┃ˑˑ┗━ sun1
> ˑˑˑ┃ˑˑ┣━ hOffset
> ˑˑˑ┃ˑˑ┃ˑˑ┗━ 250
> ˑˑˑ┃ˑˑ┣━ vOffset
> ˑˑˑ┃ˑˑ┃ˑˑ┗━ 250
> ˑˑˑ┃ˑˑ┗━ alignment
> ˑˑˑ┃ˑˑˑˑˑ┗━ center
> ˑˑˑ┗━ text
> ˑˑˑˑˑˑ┣━ data
> ˑˑˑˑˑˑ┃ˑˑ┗━ Click Here
> ˑˑˑˑˑˑ┣━ size
> ˑˑˑˑˑˑ┃ˑˑ┗━ 36
> ˑˑˑˑˑˑ┣━ style
> ˑˑˑˑˑˑ┃ˑˑ┗━ bold
> ˑˑˑˑˑˑ┣━ name
> ˑˑˑˑˑˑ┃ˑˑ┗━ text1
> ˑˑˑˑˑˑ┣━ hOffset
> ˑˑˑˑˑˑ┃ˑˑ┗━ 250
> ˑˑˑˑˑˑ┣━ vOffset
> ˑˑˑˑˑˑ┃ˑˑ┗━ 100
> ˑˑˑˑˑˑ┣━ alignment
> ˑˑˑˑˑˑ┃ˑˑ┗━ center
> ˑˑˑˑˑˑ┗━ onMouseUp
> ˑˑˑˑˑˑˑˑˑ┗━ sun1.opacity = (sun1.opacity / 100) * 90;
> ```
>

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- InstanceStringError
- InvalidTreeNameError
- DuplicateTreeError
- NotExistingJsonFileError

