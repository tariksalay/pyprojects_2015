# Code and artifact reference

[Overview](../README.md) · [Walkthrough](PROJECT_GUIDE.md) · [Development guide](DEVELOPMENT.md)

This reference describes the files on this branch. Function names are navigation aids; the walkthrough explains how their inputs, state, and outputs fit together.

## Python modules

### [Amusement Park Tram.py](../Amusement%20Park%20Tram.py)

Model a park, stops, tourists, and tram movement.

- `randstart(num_lots)`
- `ParkingLot` — `__init__`, `__str__`, `__repr__`, `register_tourist`, `report`, `get_on_tram`
- `Park` — `__init__`, `print_state`, `step`, `simulate`, `__str__`, `report`
- `Tram` — `__init__`, `__str__`, `get_on`, `get_off`, `move`
- `Tourist` — `__init__`, `__str__`, `direction`, `set_arrived`
- `main()`

### [Image Filters.py](../Image%20Filters.py)

Create grayscale and reduced-blue vintage images with Pillow.

- `grayscale_look(fname, outname)`
- `vintage_look(fname, outname)`
- `main()`

### [LostLuggage.py](../LostLuggage.py)

Run the historical stochastic airport/luggage simulation.

- `main()`

### [Sentiment Analysis.py](../Sentiment%20Analysis.py)

Collect the ratings of reviews containing each requested word and summarize occurrence-level statistics.

- `menu(options, prompt)`
- `get_valid_name(prompt)`
- `findscore(lines, word)`
- `average(numbers)`
- `standard_deviation(scores)`
- `process_list(list_of_words, review_file)`
- `report(results, sort_key, asc=True)`
- `main()`

### [SliceProgram.py](../SliceProgram.py)

Run the interactive string-slicing exercise.

- `main()`

### [Stocks.py](../Stocks.py)

Explain that the original stock exercise is incomplete and exit with status 2.

- `main()`

### [Transposition.py](../Transposition.py)

Apply and reverse the even/odd-character permutation on UTF-8 files.

- `transpose(message)`
- `untranspose(message)`
- `transform_file(source, destination, decode=False)`

## Historical artifact

[legacy/Stocks.py.txt](../legacy/Stocks.py.txt) preserves the incomplete original stock source as text. It is not imported or presented as a working program. Other legacy data files must be supplied only where the development guide calls for them.

## Checks and setup

[Tests](../tests/) contains the focused checks described in the [development guide](DEVELOPMENT.md). Consult that guide for dependencies, commands, and the boundary between automated validation and untested integrations.
