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
> >>> br4nch.export.Text(tree="MyTree", output_folder="D:/MyOutput")
> # Path: D:/br4nch-MyBranch.txt
> ```
>
> The content of the file that we exported to a text file.
>
> ***file:** "D:/MyOutput/br4nch-WynncraftAPI.txt"*
>
> ```
> Movies & Series
> ┣━ Netflix
> ┃  ┣━ Movies
> ┃  ┃  ┗━ Interstellar
> ┃  ┗━ Series
> ┃     ┣━ Squid Game
> ┃     ┗━ The Crown
> ┗━ Prime Video
>    ┣━ Movies
>    ┃  ┣━ Tenet
>    ┃  ┗━ Parasite
>    ┗━ Series
>       ┗━ The Walking Dead
> ```
>
> To export multiple trees to a text file in the same function call, you can use a list for the `tree` argument.
>
> ```python
> >>> br4nch.export.Text(tree=["MyTree", "Stream"], output_folder="D:/MyOutput")
> # Path: D:\MyOutput\br4nch-MyBranch
> # Path: D:\MyOutput\br4nch-Stream
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- InstanceStringError
- NotExistingDirectoryError
- NotExistingTreeError

