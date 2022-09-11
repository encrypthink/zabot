from pathlib import Path
from modules.databases.database import Database
from modules.commander.src.actions.creator import Creator
from modules.commander.src.actions.tester import Tester
from modules.commander.src.actions.runner import Runner


class Console(Database):

    version = "0.1 beta"

    def __init__(self, command):
        super().__init__()
        self.__router(command)

    def __router(self, command):
        if command[0] in ["-help", "--h"]:
            return self.__helps()
        elif command[0] in ["-version", "--v"]:
            return self.__version()
        elif command[0] in ["create", "testing", "run"]:
            return self.__command_check(command)

    def __helps(self):
        file_help = Path("modules/commander/help.txt")
        if file_help.is_file():
            open_help_file = open(file_help, "r")
            print(open_help_file.read())
        else:
            print("file not found")

    def __version(self):
        print("ZaBot version {}".format(self.version))

    def __command_check(self, command):
        if len(command) > 1:
            arguments = command[1].split(":")
            if command[0] == "create":
                Creator(args1=arguments[0], args2=arguments[1])
            elif command[0] == "testing":
                Tester(args1=arguments[0], args2=arguments[1])
            elif command[0] == "run":
                Runner(args1=arguments[0])
        else:
            print("Incomplete command, please recheck your '{}' command must have arguments after it.".format(command[0]))