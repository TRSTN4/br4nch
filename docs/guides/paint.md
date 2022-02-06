# Paint

Keep in mind that **not every terminal** supports paint.

## List

Here is a list of all the possible paints that can be selected:

- Red
- Yellow
- Green
- Cyan
- Blue
- Magenta
- Black
- White
- Bold
- Underline

## How to use?

To add paint to a layer, use this guide.

**Guide:**

> To add paint to a layer, first specify the branch, the position of the layer to be painted, and the paint to be added.
>
> ```python
> >>> br4nch.set.paint.layer(branch="MyBranch", position="1", paint="blue")
> ```
>
> To add the paint to multiple branches in the same function call, you can use a list for the `branch` argument.
>
> ```python
> >>> br4nch.set.paint.layer(branch=["MyBranch", "Stream"], position="1", paint="blue")
> ```
>
> To add the paint to multiple positions in the same function call, you can use a list for the `position` argument.
>
> ```python
> >>> br4nch.set.paint.layer(branch="MyBranch", position=["1", "1.1"], paint="blue")
> ```
>
> To add multiple colors/specials to the paint in the same function call, you can use a list for the `paint` argument.
>
> ```python
> >>> br4nch.set.paint.layer(branch="MyBranch", position="1", paint=["blue", "bold"])
> ```

