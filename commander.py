import sys
from modules.commander.console import Console

argument_list = sys.argv[1:]

first_params = [
    "--h",
    "-help", 
    "--v", 
    "-version",
    "create", 
    "testing",
    "run"
]

if argument_list[0] in first_params:
    Console(argument_list)
else:
    print("Your command not recognized")