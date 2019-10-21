import argparse

#tutorial: https://docs.python.org/3/howto/argparse.html#id1

parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number.", type=int) 	#required argument
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="count", default=0)

args = parser.parse_args()
answer = args.square**2

if args.verbose >= 2:
	print(f"The square of {args.square} equals {answer}")
elif args.verbose == 1:
	print(f"{args.square}² == {answer}")
else:
	print(answer)