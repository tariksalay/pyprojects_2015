"""Entry point for an incomplete historical coursework draft."""
import sys


def main():
    print("This stock exercise is incomplete: the input CSV files and their schema are missing. "
          "The original draft is preserved in legacy/Stocks.py.txt.", file=sys.stderr)
    return 2


if __name__ == '__main__':
    raise SystemExit(main())
