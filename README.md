# Python Programming Exercises

**Python · File processing · Text statistics · Images · Simulation · OOP**

A collection of early standalone Python exercises with focused repairs and tests. The programs cover reversible text transformations, image effects, review-word statistics, console games, and simple simulations.

## What this project demonstrates

- File/image processing with explicit inputs and outputs.
- Small object models and state transitions.
- Edge-case repairs while retaining historical coursework context.

## Start here

| Read | Use it for |
| --- | --- |
| [Project walkthrough](docs/PROJECT_GUIDE.md) | Purpose, workflow, repository map, and a concrete example |
| [Code and artifact reference](docs/CODE_REFERENCE.md) | Important files, functions, classes, and their responsibilities |
| [Development guide](docs/DEVELOPMENT.md) | Setup, configuration, commands, tests, and remaining limitations |

## Explore locally

Use Python 3.11 or 3.12 in a virtual environment.

```sh
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python Transposition.py input.txt encoded.txt
python "Image Filters.py" input.png output.png --effect grayscale
```

Other exercises use console prompts; sentiment analysis requires your own review file.

## Validation and scope

Five test groups cover Unicode/newline roundtrips, image pixels/modes, sentiment edge cases, tram behavior, and import safety. Every simulation assumption or interactive input path has not been redesigned. The stock exercise remains explicitly incomplete.



---

[GitHub profile](https://github.com/tariksalay) · [Portfolio](https://tariksalay.github.io/) · [Earlier README](README_HISTORY.md)

The earlier README is preserved as historical context; the guides above describe this branch's implementation.
