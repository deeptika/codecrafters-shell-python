import sys

builtin_commands = ["echo", "exit", "type"]

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
                if cmd in builtin_commands:
                    print(f"{cmd} is a shell builtin")
                else:
                    print(f"{command}: command not found")
            case _:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()
