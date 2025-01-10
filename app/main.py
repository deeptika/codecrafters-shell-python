import sys
import os
import subprocess as sp

builtin_commands = ["echo", "exit", "type"]
PATH = os.environ.get('PATH')


def find_path(cmd):
    cmd_path = None
    paths = PATH.split(":")
    for path in paths:
        if os.path.isfile(f"{path}/{cmd}"):
            cmd_path = f"{path}/{cmd}"
    return cmd_path


def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")

        command, *args = input().split(" ")

        if command == 'exit' and args[0] == '1':
            sys.exit(0)

        if command == 'echo':
            print(*args)

        elif command == 'type':
            cmd = args[0]
            if cmd in builtin_commands:
                print(f"{cmd} is a shell builtin")
            elif find_path(cmd):
                print(f"{find_path(cmd)} is a shell builtin")
            else:
                print(f"{cmd}: not found")

        else:
            if find_path(command):
                sp.run(args=[find_path(command), *args])
            else:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()
