# export.Text

To export the tree output to a text file, use the **following function:**

> br4nch.**export**.**Text**(*tree*, *output_folder*)

**Required argument(s):**

- *tree* - The tree that will be exported to a text file.
- *output_folder* - The output directory for the text file.

**Guide:**

> To export the output of the tree to a text file, specify the tree in the `tree` argument and specify the path to export the file to in the `output_folder` argument.
>
> ```python
> >>> br4nch.export.Text(tree="Stream", output_folder="D:/MyOutput")
> # Path: D:/MyOutput/br4nch-Stream.txt
> ```
>
> The content of the file that we exported to a text file.
>
> ***file:** "D:/MyOutput/br4nch-Stream.txt"*
>
> ```
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┃ˑˑ┗━ Interstellar
> ┃ˑˑ┗━ Series
> ┃ˑˑˑˑˑ┣━ Squid Game
> ┃ˑˑˑˑˑ┗━ The Crown
> ┗━ Prime Video
> ˑˑˑ┣━ Movies
> ˑˑˑ┃ˑˑ┣━ Tenet
> ˑˑˑ┃ˑˑ┗━ Parasite
> ˑˑˑ┗━ Series
> ˑˑˑˑˑˑ┗━ The Walking Dead
> ```
>
> To export multiple trees to a text file in the same function call, you can use a list for the `tree` argument.
>
> ```python
> >>> br4nch.export.Text(tree=["MyTree", "Stream"], output_folder="D:/MyOutput")
> # Path: D:/MyOutput/br4nch-Stream.txt
> # Path: D:/MyOutput/br4nch-Stream.txt
> ```
>
> To export the output in multiple folders in the same function call, you can use a list for the `output_folder` argument.
>
> ```python
> >>> br4nch.export.Text(tree="MyTree", output_folder=["D:/MyOutput", "D:/DataOutput"])
> # Path: D:/MyOutput/br4nch-Stream.txt
> # Path: D:/DataOutput/br4nch-Stream.txt
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- InstanceStringError
- NotExistingDirectoryError
- NotExistingTreeError

