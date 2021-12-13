# br4nch: Data structure tree generator for Python

<p align="center">
    <a href="https://github.com/TRSTN4/br4nch/issues">
    <img src="https://img.shields.io/github/issues/TRSTN4/br4nch.svg?style=&label=Issues"
         alt="GitHub issues open">
    <a href="https://github.com/TRSTN4/br4nch/issues">
    <img src="https://img.shields.io/github/issues-closed/TRSTN4/br4nch.svg?style=&label=Issues"
         alt="GitHub issues closed">
    <a href="https://github.com/TRSTN4/br4nch/pulls">
    <img src="https://img.shields.io/github/issues-pr/TRSTN4/br4nch.svg?style=&label=Pull requests"
         alt="GitHub pull requests open">
    <a href="https://github.com/TRSTN4/br4nch/pulls">
    <img src="https://img.shields.io/github/issues-pr-closed/TRSTN4/br4nch.svg?style=&label=Pull requests"
         alt="GitHub pull requests closed">
</p>
<p align="center">
  <a href="#what-is-br4nch">About</a> •
  <a href="#installation">Installation</a> •
  <a href="#documentation">Documentation</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#got-a-question">Questions</a> •
  <a href="#support-me">Donate</a>
</p>



## What is br4nch?

**br4nch** is a data structure tree generator for Python.

Here is an example of the very basics of **br4nch**:

```python
>>> br4nch.add.branch(branch="Streaming", header="Movies & Series")
>>> br4nch.add.layer(branch="Streaming", layer=["Netflix", "Prime Video"], position="0")
>>> br4nch.add.layer(branch="Streaming", layer=["Movies", "Series"], position="*")
>>> br4nch.add.layer(branch="Streaming", layer="Interstellar", position="1.1")
>>> br4nch.add.layer(branch="Streaming", layer=["Squid Game", "The Crown"], position="1.2")
>>> br4nch.add.layer(branch="Streaming", layer=["Tenet", "Parasite"], position="2.1")
>>> br4nch.add.layer(branch="Streaming", layer="The Walking Dead", position="2.2")

>>> br4nch.display.branch(branch="Streaming")
Movies & Series
┣━ Netflix
┃  ┣━ Movies
┃  ┃  ┗━ Interstellar
┃  ┗━ Series
┃     ┣━ Squid Game
┃     ┗━ The Crown
┗━ Prime Video
   ┣━ Movies
   ┃  ┣━ Tenet
   ┃  ┗━ Parasite
   ┗━ Series
      ┗━ The Walking Dead
```

See [the documentation](https://docs.br4nch.com) for more examples.

## Installation

**b4nch** can be installed using pip:

```
pip install br4nch
```

## Documentation

Jump straight to the documentation:

https://docs.br4nch.com

## Contributing

Help in testing, development, documentation and other tasks is highly appreciated and useful to the project. There are tasks for contributors of all experience levels.

To get started with developing **br4nch**, see [CONTRIBUTING](https://github.com/TRSTN4/br4nch/blob/release/CONTRIBUTING.md).

## Got a question?

We are always happy to answer questions! Here are some good places to ask them:

- For general questions about **br4nch**, try [br4nch discussions](https://github.com/TRSTN4/br4nch/discussions)

If you're just getting started, [the documentation](https://docs.br4nch.com) can help answer questions.

If you think you've found a bug or want to request a feature:

- Search our [issue tracker](https://github.com/TRSTN4/br4nch/issues) to see if it's already been reported

To report a bug or request a feature:

- Report at our [issue tracker](https://github.com/TRSTN4/br4nch/issues)

## Support me?

If you enjoy using br4nch, you can support me here:

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/TRSTN4)

 
