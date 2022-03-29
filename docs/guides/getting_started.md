# Getting Started

## Step 1

**Guide:**

> First we need to create a branch, we will call the branch `MyBranch` and the name of the header will be `My Header!`.
>
> ```python
> >>> br4nch.create.branch(branch="MyBranch", header="My Header!")
> ```

## Step 2

**Guide:**

> To print the result of the branch created so far, specify the name of the branch you want to print. In this case the branch `MyBranch`.
>
> ```python
> >>> br4nch.display.branch(branch="MyBranch")
> My custom header!
> ```

## Step 3

**Guide:**

> To create a layer to the branch, first specify the branch where the layer should be created, the name of the layer you want to create (we use the name `Hello World!`) and the position where the layer must be created. The position `0` indicates that the layer is created at the first height.
>
> *For more information about positions, head to [positions](../guides/positions.md).*
>
> ```python
> >>> br4nch.create.layer(branch="MyBranch", layer="Hello World!", position="0")
> 
> >>> br4nch.display.branch(branch="MyBranch")
> My custom header!
> ┗━ Hello World!
> ```
>
> To create multiple layer in the same function call, you can use list for the `layer` argument.
>
> ```python
> >>> br4nch.create.layer(branch="MyBranch", layer=["Apple", "Pear"], position="0")
> 
> >>> br4nch.display.branch(branch="MyBranch")
> My custom header!
> ┣━ Hello World!
> ┣━ Apple
> ┗━ Pear
> ```

## Step 4

**Guide:**

> To create a sublayer in for example the layer `Hello World!`, adjust the position to `1`. This is because the `Hello World!` layer is in place `1` in the first height.
>
> ```python
> >>> br4nch.create.layer(branch="MyBranch", layer="Tree", position="1")
> 
> >>> br4nch.display.branch(branch="MyBranch")
> My custom header!
> ┣━ Hello World!
> ┃ˑˑ┗━ Tree
> ┣━ Apple
> ┗━ Pear
> ```
>
> To create an layer at  multiple positions in the same function call, you can use list for the `position` argument.
>
> ```python
> >>> br4nch.create.layer(branch="MyBranch", layer="Plant", position=["2", "3"])
> 
> >>> br4nch.display.branch(branch="MyBranch")
> My custom header!
> ┣━ Hello World!
> ┃ˑˑ┗━ Tree
> ┣━ Apple
> ┃ˑˑ┗━ Plant
> ┗━ Pear
> ˑˑˑ┗━ Plant
> ```
>
> *Need help with the positions? then use the function `display.assist` .*
>
> ```python
> >>> br4nch.display.assist(branch="MyBranch")
> 0: My custom header!
> ┣━ 1: Hello World!
> ┃ˑˑ┗━ 1.1: Tree
> ┣━ 2: Apple
> ┃ˑˑ┗━ 2.1: Plant
> ┗━ 3: Pear
> ˑˑˑ┗━ 3.1: Plant
> ```

## Step 5

**Guide:**

> To create another sublayer in for example the layer `Tree`, adjust the position to `1.1`. (See example above).
>
> ```python
> >>> br4nch.create.layer(branch="MyBranch", layer="Birds", position="1.1")
> 
> >>> br4nch.display.branch(branch="MyBranch")
> My custom header!
> ┣━ Hello World!
> ┃ˑˑ┗━ Tree
> ┃ˑˑˑˑˑ┗━ Birds
> ┣━ Apple
> ┃ˑˑ┗━ Plant
> ┗━ Pear
> ˑˑˑ┗━ Plant
> ```
>

