import sys
import os
import subprocess as sp
import shlex

BUILTINS = ["echo", "exit", "type", "pwd", "cd"]
PATH = os.environ.get('PATH')
HOME = os.environ.get('HOME')


def find_path(cmd):
    cmd_path = None
    paths = PATH.split(":")
    for path in paths:
        if os.path.isfile(f"{path}/{cmd}"):
            cmd_path = f"{path}/{cmd}"
    return cmd_path


def process_command(input_txt):
    _ = input_txt.split("'")
    return [x for x in _ if x.strip() != '']


def main():
    while True:
        sys.stdout.write("$ ")

        command_txt = input()
        command, *args = command_txt.split(" ")

        if command == 'exit' and args[0] == '0':
            sys.exit(0)

        if command == 'echo':
            echo_txt = command_txt[5:]
            if echo_txt.startswith("'") and echo_txt.endswith("'"):
                echo_txt = echo_txt[1:-1]
                echo_txt = "".join(echo_txt.split("'"))
                print(echo_txt)
            else:
                print(" ".join(shlex.split(echo_txt)))

        elif command == 'pwd':
            print(os.getcwd())

        elif command == 'cd':
            try:
                if args[0] == '~':
                    os.chdir(HOME)
                else:
                    os.chdir(*args)
            except FileNotFoundError:
                print(f"{command}: {args[0]}: No such file or directory")

        elif command == 'type':
            cmd = args[0]
            if cmd in BUILTINS:
                print(f"{cmd} is a shell builtin")
            elif find_path(cmd):
                print(f"{cmd} is {find_path(cmd)}")
            else:
                print(f"{cmd}: not found")

        else:
            if find_path(command):
                processed_args = process_command(command_txt[len(command) + 1:])
                sp.run(args=[command, *processed_args])
            else:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()