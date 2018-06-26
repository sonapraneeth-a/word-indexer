from commandline import parse_args
import sys

command_line = "-i \"./input-text-files/cnn-notes\" -o \"index.html\" --debug".split()

# arguments = " ".join(sys.argv[1:])
# args = parse_args(args=arguments)
args = parse_args(args=command_line)

print(args)