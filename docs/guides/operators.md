# Operators

## Combinator - /

The operator 'Combinator' is used to perform multiple position actions at the same height as the current position.

Here's an example:

```python
>>> br4nch.add.branch(branch="Streaming", header="Movies & Series")
>>> br4nch.add.layer(branch="Streaming", layer=["Netflix", "Prime Video"], position="0")

# Using the '/'/'combinator' operator.
>>> br4nch.add.layer(branch="Streaming", layer=["Movies", "Series"], position="1/2")

>>> br4nch.display.branch(branch="Streaming")
Movies & Series
┣━ Netflix
┃  ┣━ Movies
┃  ┗━ Series
┗━ Prime Video
   ┣━ Movies
   ┗━ Series

# Using the '/'/'combinator' operator followed by a position.
>>> br4nch.add.layer(branch="Streaming", layer=["The Hobbit"], position="1/2.1")

>>> br4nch.display.branch(branch="Streaming")
Movies & Series
┣━━ Netflix
┃   ┣━━ Movies
┃   ┃   ┗━━ The Hobbit
┃   ┗━━ Series
┗━━ Prime Video
    ┣━━ Movies
    ┃   ┗━━ The Hobbit
    ┗━━ Series
```



## Selector - *

The operator 'selector' is used to include all positions at the same height as the current position.

Here's an example:

```python
>>> br4nch.add.branch(branch="Streaming", header="Movies & Series")
>>> br4nch.add.layer(branch="Streaming", layer=["Netflix", "Prime Video"], position="0")

# Using the '*'/'selector' operator.
>>> br4nch.add.layer(branch="Streaming", layer=["Movies", "Series"], position="*")

>>> br4nch.display.branch(branch="Streaming")
Movies & Series
┣━ Netflix
┃  ┣━ Movies
┃  ┗━ Series
┗━ Prime Video
   ┣━ Movies
   ┗━ Series

# Using the '*'/'selector' operator followed by a position.
>>> br4nch.add.layer(branch="Streaming", layer=["The Hobbit"], position="*.1")

>>> br4nch.display.branch(branch="Streaming")
Movies & Series
┣━━ Netflix
┃   ┣━━ Movies
┃   ┃   ┗━━ The Hobbit
┃   ┗━━ Series
┗━━ Prime Video
    ┣━━ Movies
    ┃   ┗━━ The Hobbit
    ┗━━ Series
```

The operator can also be used for example to display all branches.

```python
>>> br4nch.display.branch(branch="*")
```



## Inclusor - >

The operator 'inclusor' is used to include all positions between two values at the same height as the current position.

Here's an example:

```python
>>> br4nch.add.branch(branch="MyBranch", header="My Header")
>>> br4nch.add.layer(branch="MyBranch", layer=["Layer One", "Layer Two", "Layer Three"], position="0")

# Using the '>'/'inclusor' operator followed by a position.
>>> br4nch.add.layer(branch="MyBranch", layer=["Sub Layer"], position="2>3")

>>> br4nch.display.branch(branch="MyBranch")
My Header
┣━━ Layer One
┣━━ Layer Two
┃   ┗━━ Sub Layer
┗━━ Layer Three
    ┗━━ Sub Layer

# Using the '>'/'inclusor' operator followed by a position.
>>> br4nch.add.layer(branch="MyBranch", layer=["Final Layer"], position="2>3.1")

>>> br4nch.display.branch(branch="MyBranch")
My Header
┣━━ Layer One
┣━━ Layer Two
┃   ┗━━ Sub Layer
┃       ┗━━ Final Layer
┗━━ Layer Three
    ┗━━ Sub Layer
        ┗━━ Final Layer
```



## Exclusor - <

The operator 'exclusor' is used to avoid using all positions between two values at the same height as the current position.

Here's an example:

```python
>>> br4nch.add.branch(branch="MyBranch", header="My Header")
>>> br4nch.add.layer(branch="MyBranch", layer=["Layer One", "Layer Two", "Layer Three"], position="0")

>>> br4nch.add.layer(branch="MyBranch", layer=["Sub Layer"], position="2<3")

# Using the '<'/'exclusor' operator followed by a position.
>>> br4nch.display.branch(branch="MyBranch")
My Header
┣━ Layer One
┃   ┗━ Sub Layer
┣━ Layer Two
┗━ Layer Three

# Using the '<'/'exclusor' operator followed by a position.
>>> br4nch.add.layer(branch="MyBranch", layer=["Final Layer"], position="2<3.1")

>>> br4nch.display.branch(branch="MyBranch")
My Header
┣━ Layer One
┃   ┗━ Sub Layer
┃       ┗━ Final Layer
┣━ Layer Two
┗━ Layer Three
```



## Combinations

Combinations can also be made with positions and operators together in the same height of the position. The 'combinator' operator is used for this.

**Here is an list for example:**

- */1
- 1>2/5>6
- 1<2/3
- 2/3/5/6
- 2/5>7/9

