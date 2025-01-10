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

        command = input()

        match command.split():
            case ["exit", "0"]:
                sys.exit(0)

            case ["echo", *args]:
                print(*args)

            case ["type", *args]:
                cmd = args[0]
                cmd_path = find_path(cmd)
                if cmd in builtin_commands:
                    print(f"{cmd} is a shell builtin")
                elif cmd_path:
                    print(f"{cmd} is {cmd_path}")
                else:
                    print(f"{cmd}: not found")

            case [*args]:
                cmd = args[0]
                cmd_path = find_path(cmd)
                if cmd_path:
                    # execute cmd and " ".join(args)
                    sp.run([cmd_path, *args[1:]], capture_output=True, text=True)
                else:
                    print(f"{command}: command not found")

            case _:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()
