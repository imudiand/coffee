import web
import argparse

__all__ = ['parser']

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers()

web.init_parser(subparser)

def main():
  args = parser.parse_args()
  args.func(args)

if __name__ == "__main__":
  main()

