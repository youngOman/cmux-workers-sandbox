"""統一命令列入口（沙盒用）。

用法：
    python3 cli.py mean 1 2 3
    python3 cli.py median 1 2 3
    python3 cli.py slug "Hello World"
"""

import argparse
import sys

from stats import mean, median
from textutil import slugify


def _number(s):
    try:
        return int(s)
    except ValueError:
        pass
    try:
        return float(s)
    except ValueError:
        raise argparse.ArgumentTypeError(f"不是數字：{s!r}")


def build_parser():
    parser = argparse.ArgumentParser(prog="cli.py", description="沙盒工具命令列入口")
    sub = parser.add_subparsers(dest="command", required=True)

    for name, func in (("mean", mean), ("median", median)):
        p = sub.add_parser(name, help=f"計算 {name}")
        p.add_argument("numbers", nargs="+", type=_number)
        p.set_defaults(func=func)

    p = sub.add_parser("slug", help="把文字轉成 slug")
    p.add_argument("text")
    p.set_defaults(func=slugify)
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "slug":
        print(args.func(args.text))
    else:
        print(args.func(args.numbers))
    return 0


if __name__ == "__main__":
    sys.exit(main())
