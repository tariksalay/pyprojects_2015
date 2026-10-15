"""Reversible odd/even character transposition for text files; not encryption."""
import argparse
from pathlib import Path


def transpose(message):
    return message[::2] + message[1::2]


def untranspose(message):
    middle = (len(message) + 1) // 2
    left, right = message[:middle], message[middle:]
    return ''.join(left[i:i+1] + right[i:i+1] for i in range(middle))


def transform_file(source, destination, decode=False):
    source, destination = Path(source), Path(destination)
    if source.resolve() == destination.resolve():
        raise ValueError('Choose a different output file to preserve the input.')
    transform = untranspose if decode else transpose
    with source.open(encoding='utf-8', newline='') as stream:
        lines = stream.read().splitlines(keepends=True)
    with destination.open('w', encoding='utf-8', newline='') as stream:
        for line in lines:
            text = line.rstrip('\r\n')
            ending = line[len(text):]
            stream.write(transform(text) + ending)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('destination', type=Path)
    parser.add_argument('--decode', action='store_true')
    args = parser.parse_args()
    transform_file(args.source, args.destination, args.decode)
