# Development and validation

Use Python 3.11 or 3.12. Install `requirements.txt` for the image exercises. All exercise modules can now be imported without starting interactive prompts.

```sh
python -m unittest discover -s tests -v
python Transposition.py input.txt encoded.txt
python Transposition.py encoded.txt decoded.txt --decode
python "Image Filters.py" input.png output.png --effect grayscale
python "Image Filters.py" input.png vintage.png --effect vintage
python "Amusement Park Tram.py"
python SliceProgram.py
python LostLuggage.py
python "Sentiment Analysis.py"
```

Sentiment analysis still needs your own `movieReviews.txt` with a numeric rating followed by review text on each line. It now matches whole words, handles unseen words, and calculates population standard deviation rather than variance. Transposition preserves all lines and line endings; it is a learning cipher, not secure encryption. Image processing accepts RGB, grayscale, and RGBA input through Pillow.

The tram uses valid distinct start/destination lots and unloads all passengers arriving at a stop. Slice-game integer retries and negative-index ranges were corrected. `Stocks.py` remains an incomplete exercise: the original malformed draft is archived verbatim as `legacy/Stocks.py.txt`; its launcher explains the missing dataset/schema instead of pretending to calculate returns.

Tests cover file roundtrips, Unicode/newlines, image pixels, sentiment edge cases, valid tram journeys, and import safety. Simulation probability design and every interactive-input path have not been comprehensively redesigned.
