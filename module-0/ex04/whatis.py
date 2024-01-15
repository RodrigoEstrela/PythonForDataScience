import sys

if (len(sys.argv) - 1 == 0):
	sys.exit(1)

try:
	assert len(sys.argv) - 1 == 1, "more than one argument is provided"
	argument = sys.argv[1]
	number = int(argument)
	if (number % 2 == 0):
		print("I'm Even.")
	else:
		print("I'm Odd.")
except AssertionError as e:
	print(f"AssertionError: {e}")
	sys.exit(1)
except ValueError as e:
	print(f"AssertionError: argument is not an integer")
	sys.exit(1)

