# Positions

It is recommended to use operators. For more information about operators, head to [operators](../guides/operators.md).

## Adding the first layers

**Guide:**

> To add the first layer(s) to the created branch, specify the position `0` to indicate that the layer(s) will be added to the first height.
>
> ```python
> >>> br4nch.add.layer(branch="Stream", layer="Netflix", position="0")
> 
> >>> br4nch.display.branch(branch="Stream")
> Movies & Series
> ┗━ Netflix
> ```
>

## Adding sublayers

**Guide:**

> Specifies the `1` and `2` positions to create the layers inside the `Netflix` and `Prime Video` layer.
>
> ```python
> >>> br4nch.add.layer(branch="Streaming", layer=["Movies", "Series"], position=["1", "2"])
> 
> >>> br4nch.display.assist(branch="Streaming")
> 0: Movies & Series
> ┣━ 1: Netflix
> ┃  ┣━ 1.1: Movies
> ┃  ┗━ 1.2: Series
> ┗━ 2: Prime Video
>    ┣━ 2.1: Movies
>    ┗━ 2.2: Series
> ```
>
> Specifies the `1.1` and `2.1` positions to create the layers inside the `Movies and Series` layer in both parent `Netflix` and `Prime Video` layers.
>
> ```python
> >>> br4nch.add.layer(branch="Streaming", layer=["The Hobbit"], position=["1.1", "2.1"])
> 
> >>> br4nch.display.assist(branch="Streaming")
> 0: Movies & Series
> ┣━ 1: Netflix
> ┃  ┣━ 1.1: Movies
> ┃  ┃  ┗━ 1.1.1: The Hobbit
> ┃  ┗━ 1.2: Series
> ┗━ 2: Prime Video
>    ┣━ 2.1: Movies
>    ┃  ┗━ 2.1.1: The Hobbit
>    ┗━ 2.2: Series
> ```
>
> And so on..
>
> ```python
> >>> br4nch.add.layer(branch="Streaming", layer="Interstellar", position="1.1")
> >>> br4nch.add.layer(branch="Streaming", layer=["Squid Game", "The Crown"], position="1.2")
> >>> br4nch.add.layer(branch="Streaming", layer=["Tenet", "Parasite"], position="2.1")
> >>> br4nch.add.layer(branch="Streaming", layer="The Walking Dead", position="2.2")
> 
> >>> br4nch.display.branch(branch="Streaming")
> Movies & Series
> ┣━ Netflix
> ┃  ┣━ Movies
> ┃  ┃  ┣━ The Hobbit
> ┃  ┃  ┗━ Interstellar
> ┃  ┗━ Series
> ┃     ┣━ Squid Game
> ┃     ┗━ The Crown
> ┗━ Prime Video
>    ┣━ Movies
>    ┃  ┣━ The Hobbit
>    ┃  ┣━ Tenet
>    ┃  ┗━ Parasite
>    ┗━ Series
>       ┗━ The Walking Dead
> ```

## Branch assist

**Guide:**

> One of the many useful functions out there is the [branch_assist](../functions/display/display.assist.md) function. This function shows to which layer the corresponding position belongs.
>
> ```python
> >>> br4nch.display.assist(branch="Stream")
> 0: Movies & Series
> ┣━ 1: Netflix
> ┃  ┣━ 1.1: Movies
> ┃  ┃  ┣━ 1.1.1: The Hobbit
> ┃  ┃  ┗━ 1.1.2: Interstellar
> ┃  ┗━ 1.2: Series
> ┃     ┣━ 1.2.1: Squid Game
> ┃     ┗━ 1.2.2: The Crown
> ┗━ 2: Prime Video
>    ┣━ 2.1: Movies
>    ┃  ┣━ 2.1.1: The Hobbit
>    ┃  ┣━ 2.1.2: Tenet
>    ┃  ┗━ 2.1.3: Parasite
>    ┗━ 2.2: Series
>       ┗━ 2.2.1: The Walking Dead
> ```
>

