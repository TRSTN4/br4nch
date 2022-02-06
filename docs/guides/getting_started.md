**

> First we need to create a branch, we will call the branch `MyBranch` and the name of the header will be `My Header!`.
>
> ```python
> >>> br4nch.create.branch(branch="MyBranch", header="My Header!")
> ```

> To print the result of the branch created so far, specify the name of the branch you want to print. In this case the branch `MyBranch`.
>
> ```python
> >>> br4nch.display.branch(branch="MyBranch")
> My custom header!
> ```

> To create a layer to the branch, first specify the branch where the layer should be created the name of the layer you want to create (we use the name `Hello World!`) and the position where the layer must be created. The position `0` indicates that the layer is created at the first height.
>
> ```python
> >>> br4nch.create.layer(branch="MyBranch", layer="Hello World!", position="0")
> ```
>
> *You can also create multiple layers at once by making a list and specifying it in the layer argument.*
>
> ```python
> >>> br4nch.create.layer(branch="TestBranch", layer=["Apple", "Pear"], position="0")
> 
> >>> br4nch.display.branch(branch="TestBranch")
> Test branch
> ┣━ Apple
> ┗━ Pear
> ```

> To create a sublayer in for example the layer `Hello World!`, adjust the position to `1`. This is because the `Hello World!` layer in place one is in the first height.
>
> ```python
> >>> br4nch.create.layer(branch="MyBranch", layer=["Checklist", "Tree"], position="1")
> 
> >>> br4nch.display.branch(branch="MyBranch")
> My custom header!
> ┗━ Hello World!
> ‎‎‎┣━ Checklist
> ‎‎‎┗━ Tree
> ```
>
> *You can also create multiple layers at once by making a list and specifying it in the layer argument.*
>
> ```python
> >>> br4nch.create.layer(branch="TestBranch", layer="Plant", position=["1", "2"])
> 
> >>> br4nch.display.branch(branch="TestBranch")
> Test branch
> ┣━ Apple
> ┃‎‎┗━ Plant
> ┗━ Pear
> ‎‎‎┗━ Plant
> ```
>
> *Hulp nodig met de posities? gebruik dan de function `display.assist` .*
>
> ```python
> >>> br4nch.display.assist(branch="MyBranch")
> 0: My custom header!
> ┣━ 1: Hello World!
> ┃‎‎┣━ 1.1: Checklist
> ┃‎‎┗━ 1.2: Tree
> ┣━ 2: Apple
> ┗━ 3: Pear
> ```

> To create another sublayer in for example the layer `Tree`, adjust the position to `1.2`. (See example above).
>
> ```python
> >>> br4nch.create.layer(branch="MyBranch", layer="Birds", position="1.2")
> 
> >>> br4nch.display.branch(branch="MyBranch")
> My custom header!
> ┣━ Hello World!
> ┃‎‎┣━ Checklist
> ┃‎‎┗━ Tree
> ┃‎‎‎‎‎┗━ Birds
> ┣━ Apple
> ┗━ Pear
> ```
>

