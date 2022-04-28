![logo](https://raw.githubusercontent.com/TRSTN4/br4nch/release/assets/images/logo.png)

`br4nch` is a Data Structure Tree Builder for Python. It is built in 100%/Pure Python, which means it does not use 3rd party libraries. We **listen** to our users in [issues](https://github.com/TRSTN4/br4nch/issues), Discord [channel](https://discord.gg/gKASxGEEUC) *and all over the Internet* to create a **fast**, **flexible** and **friendly** Data Structure Tree Builder.

## 👀 Basic Usage

You can easily make a simple branch. We recommend reading [Getting Started](guides/getting_started.md). To create more complex branches that can even be automated, we recommend reading the entire documentation.

```python
# Creates the branch with the header.
>>> br4nch.create.Tree(tree="MyBranch", header="My Header")

# Adds multiple layers.
>>> br4nch.create.Node(tree="MyBranch", node="Hello World!")
>>> br4nch.create.Node(tree="MyBranch", node=["Sub-layer 1", "Sub-layer 1"],
                       parent="Hello World!")

# Prints the branch.
>>> br4nch.display.Tree(tree="MyBranch")
My Header
┗━ Hello World!
ˑˑˑ┣━ Sub layer 1
ˑˑˑ┗━ Sub layer 2
```

## ⚙️ Installation

Install `br4nch` with the `pip install` command:

```
pip install br4nch
```

## 🎯 Features

- [Create](https://docs.br4nch.com/functions/create)
- [Duplicate](https://docs.br4nch.com/functions/duplicate)
- [Move](https://docs.br4nch.com/functions/move)
- [Replace](https://docs.br4nch.com/functions/replace)
- [Delete](https://docs.br4nch.com/functions/delete)
- [Set](https://docs.br4nch.com/functions/set)
- [Reset](https://docs.br4nch.com/functions/reset)
- [Load](https://docs.br4nch.com/functions/load)
- [Export](https://docs.br4nch.com/functions/export)
- [Get](https://docs.br4nch.com/functions/get)
- [Display](https://docs.br4nch.com/functions/display)

## 👍 Contribute

If you want to say **thank you** and/or support the active development of `br4nch`:

1. Add a [GitHub Star](https://github.com/TRSTN4/br4nch/stargazers) to the project.
2. Tweet about the project [on your Twitter](https://twitter.com/intent/tweet?text=br4nch%3A%20Data%20Structure%20Tree%20Builder%20for%20Python.%20br4nch%20is%20built%20on%20pure%20%23python.%20That%20means%20that%20it%20does%20not%20require%20any%20other%20libary.%20Its%20designed%20to%20ease%20things%20up%20for%20fast%20data%20structure%20development%F0%9F%9A%80%20https%3A%2F%2Fgithub.com%2FTRSTN4%2Fbr4nch%20%20).
3. Support the project by donating a [cup of coffee](https://www.buymeacoffee.com/TRSTN4).

## ☕ Support

`br4nch` is an open source project that runs on donations to pay the bills e.g. our domain name. If you want to support `br4nch`, you can ☕ [**buy a coffee here**](https://www.buymeacoffee.com/TRSTN4).

## ⚠️ License

`br4nch` is free and open-source software licensed under the [GPL-3.0 License](https://github.com/TRSTN4/br4nch/blob/release/LICENSE).
