# Positions

## Adding the first layers

To add the first layer(s) to the created branch, specify the position '0' to indicate that the layers will be added to the first height.

Here's an example:

```python
>>> br4nch.add.branch(branch="Streaming", header="Movies & Series")
>>> br4nch.add.layer(branch="Streaming", layer=["Netflix", "Prime Video"], position="0")

>>> br4nch.display.branch(branch="Streaming")
Movies & Series
┣━ Netflix
┗━ Prime Video
```



## Adding sublayers

To add sublayers in parent layers. Follow the example below: 

For more information about operators, head to [operators](../guides/operators.md).

```python
>>> br4nch.add.branch(branch="Streaming", header="Movies & Series")

# Specifies the '0' position to create the layers to the first height.
>>> br4nch.add.layer(branch="Streaming", layer=["Netflix", "Prime Video"], position="0")

>>> br4nch.display.assist(branch="Streaming")
0: Movies & Series
┣━ 1: Netflix
┗━ 2: Prime Video

# Specifies the '1' and '2' positions to create the layers inside the 'Netflix' and 'Prime Video' layer.
>>> br4nch.add.layer(branch="Streaming", layer=["Movies", "Series"], position=["1", "2"])

>>> br4nch.display.assist(branch="Streaming")
0: Movies & Series
┣━ 1: Netflix
┃   ┣━ 1.1: Movies
┃   ┗━ 1.2: Series
┗━ 2: Prime Video
    ┣━ 2.1: Movies
    ┗━ 2.2: Series

# Specifies the '1.1' and '2.1' positions to create the layers inside the 'Movies' and 'Series' layer in both parent 'Netflix' and 'Prime Video' layers.
>>> br4nch.add.layer(branch="Streaming", layer=["The Hobbit"], position=["1.1", "2.1"])

>>> br4nch.display.assist(branch="Streaming")
0: Movies & Series
┣━ 1: Netflix
┃   ┣━ 1.1: Movies
┃   ┃   ┗━ 1.1.1: The Hobbit
┃   ┗━ 1.2: Series
┗━ 2: Prime Video
    ┣━ 2.1: Movies
    ┃   ┗━ 2.1.1: The Hobbit
    ┗━ 2.2: Series

# And so on..
>>> br4nch.add.layer(branch="Streaming", layer="Interstellar", position="1.1")
>>> br4nch.add.layer(branch="Streaming", layer=["Squid Game", "The Crown"], position="1.2")
>>> br4nch.add.layer(branch="Streaming", layer=["Tenet", "Parasite"], position="2.1")
>>> br4nch.add.layer(branch="Streaming", layer="The Walking Dead", position="2.2")

>>> br4nch.display.branch(branch="Streaming")
Movies & Series
┣━ Netflix
┃   ┣━ Movies
┃   ┃   ┣━ The Hobbit
┃   ┃   ┗━ Interstellar
┃   ┗━━ Series
┃       ┣━ Squid Game
┃       ┗━ The Crown
┗━━ Prime Video
    ┣━ Movies
    ┃   ┣━ The Hobbit
    ┃   ┣━ Tenet
    ┃   ┗━ Parasite
    ┗━ Series
        ┗━ The Walking Dead
```



## Branch assist

One of the many useful functions out there is the [branch_assist](../functions/display/display.assist.md) function. This function shows to which layer the corresponding position belongs.

Here's an example:

```python
>>> br4nch.add.branch(branch="Streaming", header="Movies & Series")
>>> br4nch.add.layer(branch="Streaming", layer=["Netflix", "Prime Video"], position="0")
>>> br4nch.add.layer(branch="Streaming", layer=["Movies", "Series"], position="*")
>>> br4nch.add.layer(branch="Streaming", layer=["The Hobbit"], position="*.1")

>>> br4nch.display.assist(branch="Streaming")
0: Movies & Series
┣━ 1: Netflix
┃   ┣━ 1.1: Movies
┃   ┃   ┗━ 1.1.1: The Hobbit
┃   ┗━ 1.2: Series
┗━ 2: Prime Video
    ┣━ 2.1: Movies
    ┃   ┗━ 2.1.1: The Hobbit
    ┗━ 2.2: Series
```

