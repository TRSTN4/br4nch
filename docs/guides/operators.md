# Operators

## Combinator - /

The operator 'Combinator' is used to perform multiple position actions at the same height as the current position.

**Guide:**

> Using the `/`/`combinator` operator.
>
> ```python
> >>> br4nch.display.branch(branch="Stream")
> Movies & Series
> ┣━ Netflix
> ┗━ Prime Video
> 
> >>> br4nch.add.layer(branch="Stream", layer=["Movies", "Series"], position="1/2")
> 
> >>> br4nch.display.branch(branch="Stream")
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┗━ Series
> ┗━ Prime Video
>    ˑˑˑ┣━ Movies
>    ˑˑˑ┗━ Series
> ```
>
> Using the `/`/`combinator` operator followed by a position.
>
> ```python
> >>> br4nch.display.branch(branch="Stream")
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┗━ Series
> ┗━ Prime Video
>    ˑˑˑ┣━ Movies
>    ˑˑˑ┗━ Series
> 
> >>> br4nch.add.layer(branch="Stream", layer=["The Hobbit"], position="1/2.1")
> 
> >>> br4nch.display.branch(branch="Stream")
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┃ˑˑ┗━ The Hobbit
> ┃ˑˑ┗━ Series
> ┗━ Prime Video
>    ˑˑˑ┣━ Movies
>    ˑˑˑ┃ˑˑ┗━ The Hobbit
>    ˑˑˑ┗━ Series
> ```

## Selector - *

The operator 'selector' is used to include all positions at the same height as the current position.

**Guide**

> Using the `*`/`selector` operator.
>
> ```python
> >>> br4nch.display.branch(branch="Stream")
> Movies & Series
> ┣━ Netflix
> ┗━ Prime Video
> 
> >>> br4nch.add.layer(branch="Stream", layer=["Movies", "Series"], position="*")
> 
> >>> br4nch.display.branch(branch="Stream")
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┗━ Series
> ┗━ Prime Video
>    ˑˑˑ┣━ Movies
>    ˑˑˑ┗━ Series
> ```
>
> Using the `*`/`selector` operator followed by a position.
>
> ```python
> >>> br4nch.display.branch(branch="Stream")
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┗━ Series
> ┗━ Prime Video
>    ˑˑˑ┣━ Movies
>    ˑˑˑ┗━ Series
> 
> >>> br4nch.add.layer(branch="Stream", layer=["The Hobbit"], position="*.1")
> 
> >>> br4nch.display.branch(branch="Stream")
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┃ˑˑ┗━ The Hobbit
> ┃ˑˑ┗━ Series
> ┗━ Prime Video
>    ˑˑˑ┣━ Movies
>    ˑˑˑ┃ˑˑ┗━ The Hobbit
>    ˑˑˑ┗━ Series
> ```
>
> The `selector` operator can also be used to define all existing branches.
>
> For example to display all branches.
>
> ```python
> >>> br4nch.display.branch(branch="*")
> ```
>
> For example to create an layer in all branches on the position `0`.
>
> ```python
> >>> br4nch.add.layer(branch="*", layer="Test", position="0")
> ```

## Inclusor - >

The operator 'inclusor' is used to include all positions between two values at the same height as the current position.

**Guide:**

> Using the `>`/`inclusor` operator followed by a position.
>
> ```python
> >>> br4nch.display.branch(branch="MyBranch")
> My Header
> ┣━ Layer One
> ┣━ Layer Two
> ┗━ Layer Three
> 
> >>> br4nch.add.layer(branch="MyBranch", layer=["Sub Layer"], position="2>3")
> 
> >>> br4nch.display.branch(branch="MyBranch")
> My Header
> ┣━ Layer One
> ┣━ Layer Two
> ┃ˑˑ┗━ Sub Layer
> ┗━ Layer Three
>    ˑˑˑ┗━ Sub Layer
> ```
>
> And
>
> ```python
> >>> br4nch.display.branch(branch="MyBranch")
> My Header
> ┣━ Layer One
> ┣━ Layer Two
> ┃ˑˑ┗━ Sub Layer
> ┗━ Layer Three
>    ˑˑˑ┗━ Sub Layer
> 
> >>> br4nch.add.layer(branch="MyBranch", layer=["Final Layer"], position="2>3.1")
> 
> >>> br4nch.display.branch(branch="MyBranch")
> My Header
> ┣━ Layer One
> ┣━ Layer Two
> ┃ˑˑ┗━ Sub Layer
> ┃ˑˑˑˑˑ┗━ Final Layer
> ┗━ Layer Three
>    ˑˑˑ┗━ Sub Layer
>    ˑˑˑˑˑˑ┗━ Final Layer
> ```

## Exclusor - <

The operator 'exclusor' is used to avoid using all positions between two values at the same height as the current position.

**Guide:**

> Using the `<`/`exclusor` operator followed by a position.
>
> ```python
> >>> br4nch.display.branch(branch="MyBranch")
> My Header
> ┣━ Layer One
> ┣━ Layer Two
> ┗━ Layer Three
> 
> >>> br4nch.add.layer(branch="MyBranch", layer=["Sub Layer"], position="2<3")
> 
> >>> br4nch.display.branch(branch="MyBranch")
> My Header
> ┣━ Layer One
> ┃ˑˑ┗━ Sub Layer
> ┣━ Layer Two
> ┗━ Layer Three
> ```
>
> And
>
> ```python
> >>> br4nch.display.branch(branch="MyBranch")
> My Header
> ┣━ Layer One
> ┃ˑˑ┗━ Sub Layer
> ┣━ Layer Two
> ┗━ Layer Three
> 
> >>> br4nch.add.layer(branch="MyBranch", layer=["Final Layer"], position="2<3.1")
> 
> >>> br4nch.display.branch(branch="MyBranch")
> My Header
> ┣━ Layer One
> ┃ˑˑ┗━ Sub Layer
> ┃ˑˑˑˑˑ┗━ Final Layer
> ┣━ Layer Two
> ┗━ Layer Three
> ```

## Combinations

Combinations can also be made with positions and operators together in the same height of the position. The 'combinator' operator is used for this.

**Here is an list for example:**

- */1
- 1>2/5>6
- 1<2/3
- 2/3/5/6
- 2/5>7/9

