# Paint

Keep in mind that not every terminal supports colors.

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

To add paint to a layer, use this method.

Here's an example:

```python
>>> br4nch.set.paint.layer(branch="MyBranch", position="1", paint="blue")
```

You can also select more paint than one, a list can help with that:

```python
>>> br4nch.set.paint.layer(branch="MyBranch", position="1", paint=["blue", "bold"])
```

