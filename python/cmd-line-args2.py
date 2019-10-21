import argparse

"""
tutorial: https://docs.python.org/3/howto/argparse.html#id1
docs    : https://docs.python.org/3/library/argparse.html#module-argparse
"""

parser = argparse.ArgumentParser(description="Calculate X to the power of Y")
group = parser.add_mutually_exclusive_group()
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
#user is only allowed to use or -v or -q
group.add_argument("-v", "--verbose", action="count", default=0)
group.add_argument("-q", "--quiet", action="store_true")

args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
	print(f"Running {__file__}")
	print(f"{args.x} to the {args.y} == {answer}")
else:
	print(f"{args.x}^{args.y} == {answer}")