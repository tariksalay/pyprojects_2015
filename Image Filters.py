"""Apply grayscale or a reduced-blue vintage effect with Pillow."""
import argparse
from pathlib import Path
from PIL import Image, ImageOps


def grayscale_look(fname, outname):
    with Image.open(fname) as image:
        ImageOps.grayscale(image).convert('RGB').save(outname)


def vintage_look(fname, outname):
    with Image.open(fname) as image:
        red, green, blue = image.convert('RGB').split()
        Image.merge('RGB', (red, green, blue.point(lambda value: value // 2))).save(outname)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('destination', type=Path)
    parser.add_argument('--effect', choices=['grayscale', 'vintage'], default='grayscale')
    args = parser.parse_args()
    if args.source.resolve() == args.destination.resolve():
        parser.error('Choose a different output path to preserve the original image.')
    operation = grayscale_look if args.effect == 'grayscale' else vintage_look
    operation(args.source, args.destination)


if __name__ == '__main__':
    main()
