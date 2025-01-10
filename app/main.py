import sys
import os

builtin_commands = ["echo", "exit", "type"]
PATH = os.environ.get('PATH')

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
                cmd_path = None
                paths = PATH.SPLIT(":")
                for path in paths:
                    if os.path.isfile(f"{path}/{cmd}"):
                        cmd_path = f"{path}/{cmd}"
                if cmd in builtin_commands:
                    print(f"{cmd} is a shell builtin")
                elif cmd_path:
                    print(f"{cmd} is {cmd_path}")
                else:
                    print(f"{cmd}: not found")

            case _:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()
